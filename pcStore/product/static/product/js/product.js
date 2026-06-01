// product/static/product/js/product.js

document.addEventListener('DOMContentLoaded', () => {

    // ==========================================
    // 1. ГАЛЕРЕЯ И ХАРАКТЕРИСТИКИ
    // ==========================================
    window.toggleSpecs = function() {
        const short = document.getElementById('specs-short');
        const full = document.getElementById('specs-full');
        const btn = document.getElementById('toggle-specs');
        if (!btn) return;

        if (full.classList.contains('d-none')) {
            full.classList.remove('d-none');
            short.classList.add('d-none');
            btn.textContent = 'Свернуть';
        } else {
            full.classList.add('d-none');
            short.classList.remove('d-none');
            btn.textContent = 'Развернуть все характеристики';
        }
    };

    window.changeMainImage = function(thumb, src) {
        const mainImg = document.getElementById('mainImage');
        if (mainImg) {
            mainImg.src = src;
            document.querySelectorAll('.thumbnail').forEach(t => t.style.borderColor = 'transparent');
            thumb.style.borderColor = '#0d6efd';
        }
    };

    // ==========================================
    // 2. ФОРМА ОТЗЫВА (Звёзды и Валидация)
    // ==========================================
    const stars = document.querySelectorAll('.rating-star');
    const ratingInput = document.getElementById('ratingInput');

    stars.forEach(star => {
        star.addEventListener('click', function() {
            const val = parseInt(this.dataset.value);
            ratingInput.value = val;
            stars.forEach(s => {
                const sVal = parseInt(s.dataset.value);
                s.className = `bi bi-star${sVal <= val ? '-fill' : ''} rating-star`;
                s.style.color = sVal <= val ? '#ffc107' : '#e0e0e0';
            });
            document.getElementById('rating-error')?.classList.add('d-none');
        });
    });

    const reviewForm = document.getElementById('reviewForm');
    if (reviewForm) {
        reviewForm.addEventListener('submit', function(e) {
            const rating = ratingInput.value;
            const comment = document.querySelector('textarea[name="comment"]')?.value.trim();
            let error = false;

            if (!rating) {
                document.getElementById('rating-error').classList.remove('d-none');
                error = true;
            }
            if (!comment) {
                const err = document.getElementById('comment-error');
                err.classList.remove('d-none');
                error = true;
            }
            if (error) {
                e.preventDefault();
                return false;
            }
        });
    }

    document.getElementById('hasIssue')?.addEventListener('change', function() {
        document.getElementById('issueBlock')?.classList.toggle('d-none', !this.checked);
    });

    // ==========================================
    // 3. DRAG & DROP ФАЙЛОВ
    // ==========================================
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('attachmentInput');
    const fileList = document.getElementById('fileList');

    if (dropZone) {
        dropZone.addEventListener('click', () => fileInput?.click());
        dropZone.addEventListener('dragover', e => {
            e.preventDefault();
            dropZone.style.borderColor = '#0d6efd';
            dropZone.style.background = '#f8f9fa';
        });
        dropZone.addEventListener('dragleave', () => {
            dropZone.style.borderColor = '#dee2e6';
            dropZone.style.background = '#fff';
        });
        dropZone.addEventListener('drop', e => {
            e.preventDefault();
            dropZone.style.borderColor = '#dee2e6';
            dropZone.style.background = '#fff';
            handleFiles(e.dataTransfer.files);
        });
    }

    function handleFiles(files) {
        if (!fileList) return;
        fileList.innerHTML = '';
        const dt = new DataTransfer();
        Array.from(files).slice(0, 5).forEach(f => {
            if (['image/jpeg', 'image/png', 'video/mp4'].includes(f.type)) {
                dt.items.add(f);
                const div = document.createElement('div');
                div.innerHTML = f.type.startsWith('image/')
                    ? `<img src="${URL.createObjectURL(f)}" style="width:60px;height:60px;object-fit:cover;border-radius:8px;">`
                    : `<video src="${URL.createObjectURL(f)}" style="width:80px;height:50px;object-fit:cover;border-radius:8px;" controls></video>`;
                fileList.appendChild(div);
            }
        });
        if (fileInput) fileInput.files = dt.files;
    }

    // ==========================================
    // 4. ДЕЛЕГИРОВАНИЕ СОБЫТИЙ (Лайки и Комментарии)
    // ==========================================
    document.addEventListener('click', async function(e) {
        const voteBtn = e.target.closest('.vote-btn');
        if (voteBtn) {
            e.preventDefault();
            const id = voteBtn.dataset.id;
            const vote = voteBtn.dataset.vote;
            const csrf = document.querySelector('[name=csrfmiddlewaretoken]')?.value;

            try {
                const res = await fetch('/catalog/review/vote/', {
                    method: 'POST',
                    headers: { 'X-CSRFToken': csrf, 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: `review_id=${id}&vote=${vote}`
                });
                const data = await res.json();
                if (res.ok) {
                    document.querySelector(`.vote-likes-${id}`).textContent = data.likes;
                    document.querySelector(`.vote-dislikes-${id}`).textContent = data.dislikes;
                }
            } catch(err) { console.error('Vote error:', err); }
        }
    });

    document.addEventListener('submit', async function(e) {
        const commentForm = e.target.closest('.comment-form');
        if (commentForm) {
            e.preventDefault();
            const input = commentForm.querySelector('input[type="text"]');
            if (!input) return;
            const text = input.value.trim();
            if (text.length < 2) return;

            const reviewId = commentForm.dataset.review;
            const csrf = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
            const btn = commentForm.querySelector('button');
            const oldText = btn.innerHTML;
            btn.disabled = true; btn.innerHTML = '...';

            try {
                const res = await fetch('/catalog/review/comment/', {
                    method: 'POST',
                    headers: { 'X-CSRFToken': csrf, 'Content-Type': 'application/json' },
                    body: JSON.stringify({ review_id: reviewId, text: text })
                });
                const data = await res.json();
                if (res.ok && data.status === 'ok') {
                    const list = document.getElementById(`comments-${reviewId}`);
                    if (list) {
                        const el = document.createElement('div');
                        el.className = 'd-flex gap-2 mb-2 small';
                        el.innerHTML = `<strong>${data.user}:</strong> <span class="text-muted">${data.text}</span>`;
                        list.appendChild(el);
                        input.value = '';
                    }
                }
            } catch(err) { console.error('Comment error:', err); }
            finally {
                btn.disabled = false; btn.innerHTML = oldText;
            }
        }
    });

    // ==========================================
    // 5. ПАГИНАЦИЯ ОТЗЫВОВ
    // ==========================================
    window.loadMoreReviews = function() {
        const container = document.getElementById('reviews-container');
        const hiddenContainer = document.getElementById('hidden-reviews');
        const loadMoreBtn = document.getElementById('load-more-reviews');

        if (!hiddenContainer) return;

        const hiddenReviews = Array.from(hiddenContainer.querySelectorAll('.review-item'));
        const toShow = hiddenReviews.slice(0, 3);

        toShow.forEach(review => {
            container.appendChild(review); // Переносим элемент (делегирование событий сохранится)
        });

        const remaining = hiddenContainer.querySelectorAll('.review-item').length;
        if (remaining > 0) {
            loadMoreBtn.textContent = `Показать ещё отзывы (${remaining})`;
        } else {
            loadMoreBtn.remove();
        }
    };

    // ==========================================
    // 6. ФИЛЬТРЫ И СОРТИРОВКА ОТЗЫВОВ (ИСПРАВЛЕНО)
    // ==========================================
    document.addEventListener('click', function(e) {
        // Ищем кнопку, даже если клик был по иконке <i> внутри неё
        const filterBtn = e.target.closest('.filter-btn, .filter-rating-btn');
        if (!filterBtn) return;

        e.preventDefault();

        const url = new URL(window.location.href);

        if (filterBtn.classList.contains('filter-btn')) {
            const filter = filterBtn.dataset.filter;
            const isActive = filterBtn.dataset.state === 'true';

            if (filter === 'all') {
                url.searchParams.delete('filter_photos');
                url.searchParams.delete('filter_videos');
                url.searchParams.delete('filter_rating');
            } else if (filter === 'photos') {
                isActive ? url.searchParams.delete('filter_photos') : url.searchParams.set('filter_photos', 'on');
            } else if (filter === 'videos') {
                isActive ? url.searchParams.delete('filter_videos') : url.searchParams.set('filter_videos', 'on');
            }
        }
        else if (filterBtn.classList.contains('filter-rating-btn')) {
            const rating = filterBtn.dataset.rating;
            const isActive = filterBtn.dataset.active === 'true';
            const currentRatings = url.searchParams.getAll('filter_rating');

            if (isActive) {
                // Удаляем этот рейтинг и перезаписываем остальные
                const newRatings = currentRatings.filter(r => r !== rating);
                url.searchParams.delete('filter_rating');
                newRatings.forEach(r => url.searchParams.append('filter_rating', r));
            } else {
                // Добавляем новый рейтинг
                url.searchParams.append('filter_rating', rating);
            }
        }

        // Сбрасываем пагинацию при изменении фильтров
        url.searchParams.delete('page');

        // Перенаправляем (используем toString() для максимальной совместимости)
        window.location.href = url.toString();
    });

    document.getElementById('review-sort-select')?.addEventListener('change', function() {
        const url = new URL(window.location.href);
        url.searchParams.set('sort', this.value);
        url.searchParams.delete('page');
        window.location.href = url.toString();
    });
});