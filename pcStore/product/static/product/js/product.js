

document.addEventListener('DOMContentLoaded', () => {

    const productDataScript = document.getElementById('product-data');
    const productData = productDataScript ? JSON.parse(productDataScript.textContent) : { images: [], title: 'Товар' };
    const images = productData.images || [];
    const productTitle = productData.title || 'Товар';




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




    const stars = document.querySelectorAll('.rating-star');
    const ratingInput = document.getElementById('ratingInput');
    const ratingError = document.getElementById('rating-error');

    stars.forEach(star => {
        star.addEventListener('click', function() {
            const val = parseInt(this.dataset.value);
            ratingInput.value = val;
            stars.forEach(s => {
                const sVal = parseInt(s.dataset.value);
                s.className = `bi bi-star${sVal <= val ? '-fill' : ''} rating-star`;
                s.style.color = sVal <= val ? '#ffc107' : '#e0e0e0';
            });
            if (ratingError) {
                ratingError.style.display = 'none';
            }
            ratingInput.removeAttribute('required');
        });
    });

    const reviewForm = document.getElementById('reviewForm');
    if (reviewForm) {
        reviewForm.addEventListener('submit', function(e) {
            const rating = ratingInput.value;
            const comment = document.querySelector('textarea[name="comment"]')?.value.trim();
            let error = false;

            if (!rating) {
                if (ratingError) {
                    ratingError.style.display = 'block';
                    ratingInput.setCustomValidity('Пожалуйста, поставьте оценку');
                    ratingInput.reportValidity();
                }
                error = true;
            } else {
                ratingInput.setCustomValidity('');
            }

            const commentError = document.getElementById('comment-error');
            if (!comment) {
                if (commentError) {
                    commentError.style.display = 'block';
                }
                error = true;
            } else if (commentError) {
                commentError.style.display = 'none';
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




    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('attachmentInput');
    const fileList = document.getElementById('fileList');
    let uploadedFiles = [];

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

    if (fileInput) {
        fileInput.addEventListener('change', function() {
            handleFiles(this.files);
        });
    }

    function handleFiles(files) {
        if (!fileList) return;

        const dt = new DataTransfer();
        const allowedTypes = ['image/jpeg', 'image/png', 'video/mp4'];
        const maxSize = 50 * 1024 * 1024;

        Array.from(files).forEach(f => {
            if (!allowedTypes.includes(f.type)) {
                alert(`Файл ${f.name} имеет неподдерживаемый формат. Разрешены: JPG, PNG, MP4`);
                return;
            }
            if (f.size > maxSize) {
                alert(`Файл ${f.name} слишком большой. Максимум 50MB`);
                return;
            }
            if (uploadedFiles.length >= 5) {
                alert('Можно загрузить максимум 5 файлов');
                return;
            }

            uploadedFiles.push(f);
            dt.items.add(f);
        });

        if (fileInput) fileInput.files = dt.files;
        renderFilePreviews();
    }

    function renderFilePreviews() {
        if (!fileList) return;
        fileList.innerHTML = '';

        uploadedFiles.forEach((file, index) => {
            const wrapper = document.createElement('div');
            wrapper.className = 'position-relative d-inline-block';

            const preview = document.createElement('div');
            preview.className = 'file-preview';

            if (file.type.startsWith('image/')) {
                const img = document.createElement('img');
                img.src = URL.createObjectURL(file);
                img.className = 'rounded-2';
                img.style.cssText = 'width: 80px; height: 80px; object-fit: cover; cursor: pointer;';
                img.onclick = () => openModal(file, index);
                preview.appendChild(img);
            } else if (file.type.startsWith('video/')) {
                const video = document.createElement('video');
                video.src = URL.createObjectURL(file);
                video.className = 'rounded-2';
                video.style.cssText = 'width: 120px; height: 80px; object-fit: cover; cursor: pointer;';
                video.onclick = () => openModal(file, index);
                preview.appendChild(video);
            }

            const removeBtn = document.createElement('button');
            removeBtn.type = 'button';
            removeBtn.className = 'btn btn-danger btn-sm position-absolute top-0 start-100 translate-middle rounded-circle';
            removeBtn.style.cssText = 'width: 24px; height: 24px; padding: 0; display: flex; align-items: center; justify-content: center;';
            removeBtn.innerHTML = '<i class="bi bi-x-lg" style="font-size: 12px;"></i>';
            removeBtn.onclick = () => removeFile(index);

            wrapper.appendChild(preview);
            wrapper.appendChild(removeBtn);
            fileList.appendChild(wrapper);
        });
    }

    function removeFile(index) {
        uploadedFiles.splice(index, 1);
        const dt = new DataTransfer();
        uploadedFiles.forEach(f => dt.items.add(f));
        if (fileInput) fileInput.files = dt.files;
        renderFilePreviews();
    }




    document.addEventListener('click', async function(e) {
        const voteBtn = e.target.closest('.vote-btn');
        if (!voteBtn) return;

        e.preventDefault();
        const id = voteBtn.dataset.id;
        const vote = parseInt(voteBtn.dataset.vote);
        const csrf = document.querySelector('[name=csrfmiddlewaretoken]')?.value;

        const likeBtn = document.querySelector(`.vote-btn[data-id="${id}"][data-vote="1"]`);
        const dislikeBtn = document.querySelector(`.vote-btn[data-id="${id}"][data-vote="-1"]`);

        if (likeBtn) likeBtn.disabled = true;
        if (dislikeBtn) dislikeBtn.disabled = true;

        try {
            const res = await fetch('/catalog/review/vote/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrf,
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: `review_id=${id}&vote=${vote}`
            });
            const data = await res.json();

            if (res.ok) {
                const likesEl = document.querySelector(`.vote-likes-${id}`);
                const dislikesEl = document.querySelector(`.vote-dislikes-${id}`);
                if (likesEl) likesEl.textContent = data.likes;
                if (dislikesEl) dislikesEl.textContent = data.dislikes;

                const userVote = data.user_vote || 0;

                if (userVote === 1) {
                    likeBtn?.classList.remove('btn-outline-success');
                    likeBtn?.classList.add('active', 'btn-success');
                    dislikeBtn?.classList.remove('active', 'btn-danger');
                    dislikeBtn?.classList.add('btn-outline-danger');
                } else if (userVote === -1) {
                    dislikeBtn?.classList.remove('btn-outline-danger');
                    dislikeBtn?.classList.add('active', 'btn-danger');
                    likeBtn?.classList.remove('active', 'btn-success');
                    likeBtn?.classList.add('btn-outline-success');
                } else {
                    likeBtn?.classList.remove('active', 'btn-success');
                    likeBtn?.classList.add('btn-outline-success');
                    dislikeBtn?.classList.remove('active', 'btn-danger');
                    dislikeBtn?.classList.add('btn-outline-danger');
                }
            }
        } catch(err) {
            console.error('Vote error:', err);
        } finally {
            if (likeBtn) likeBtn.disabled = false;
            if (dislikeBtn) dislikeBtn.disabled = false;
        }
    });




    document.addEventListener('submit', async function(e) {
        const commentForm = e.target.closest('.comment-form');
        if (!commentForm) return;

        e.preventDefault();
        const input = commentForm.querySelector('input[type="text"]');
        if (!input) return;

        const text = input.value.trim();
        if (text.length < 2) {
            input.focus();
            return;
        }

        const reviewId = commentForm.dataset.review;
        const csrf = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
        const btn = commentForm.querySelector('button');
        const oldText = btn.innerHTML;
        btn.disabled = true;
        btn.innerHTML = '<i class="bi bi-hourglass-split"></i>';

        try {
            const res = await fetch('/catalog/review/comment/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrf,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ review_id: reviewId, text: text })
            });
            const data = await res.json();

            if (res.ok && data.status === 'ok') {
                const list = document.getElementById(`comments-${reviewId}`);
                if (list) {
                    const el = document.createElement('div');
                    el.className = 'd-flex gap-2 mb-2 small';
                    el.innerHTML = `<strong>${data.user}:</strong> <span class="">${data.text}</span>`;
                    list.appendChild(el);
                    input.value = '';

                    const counter = commentForm.closest('.border-top')?.querySelector('h6');
                    if (counter) {
                        const match = counter.textContent.match(/\d+/);
                        const currentCount = match ? parseInt(match[0]) + 1 : 1;
                        counter.textContent = counter.textContent.replace(/\d+/, currentCount);
                    }

                    const collapseEl = document.getElementById(`comments-${reviewId}`);
                    if (collapseEl && !collapseEl.classList.contains('show')) {
                        const bsCollapse = new bootstrap.Collapse(collapseEl, { show: true });
                    }
                }
            } else {
                alert(data.error || 'Ошибка при отправке комментария');
            }
        } catch(err) {
            console.error('Comment error:', err);
            alert('Произошла ошибка при отправке комментария');
        } finally {
            btn.disabled = false;
            btn.innerHTML = oldText;
        }
    });




    window.loadMoreReviews = function() {
        const container = document.getElementById('reviews-container');
        const hiddenContainer = document.getElementById('hidden-reviews');
        const loadMoreBtn = document.getElementById('load-more-reviews');

        if (!hiddenContainer) return;

        const hiddenReviews = Array.from(hiddenContainer.querySelectorAll('.review-item'));
        const toShow = hiddenReviews.slice(0, 3);

        toShow.forEach(review => {
            container.appendChild(review);
        });

        const remaining = hiddenContainer.querySelectorAll('.review-item').length;
        if (remaining > 0) {
            loadMoreBtn.textContent = `Показать ещё отзывы (${remaining})`;
        } else {
            loadMoreBtn.remove();
        }
    };




    const filterForm = document.getElementById('review-filter-form');
    if (filterForm) {
        filterForm.addEventListener('submit', function() {
            const url = new URL(window.location.href);
            url.searchParams.delete('page');
            this.action = url.toString();
        });
    }




    let modalInstance = null;

    window.openModal = function(file, index) {
        let modal = document.getElementById('filePreviewModal');
        if (!modal) {
            modal = document.createElement('div');
            modal.className = 'modal fade';
            modal.id = 'filePreviewModal';
            modal.tabIndex = '-1';
            modal.innerHTML = `
                <div class="modal-dialog modal-dialog-centered modal-lg">
                    <div class="modal-content bg-dark border-0">
                        <div class="modal-header border-0">
                            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body p-0 d-flex align-items-center justify-content-center" style="min-height: 400px;">
                            <div id="modalContent"></div>
                        </div>
                    </div>
                </div>
            `;
            document.body.appendChild(modal);
        }

        const modalContent = modal.querySelector('#modalContent');

        if (file.type.startsWith('image/')) {
            modalContent.innerHTML = `<img src="${URL.createObjectURL(file)}" class="img-fluid" style="max-height: 80vh;">`;
        } else if (file.type.startsWith('video/')) {
            modalContent.innerHTML = `<video controls class="w-100" style="max-height: 80vh;"><source src="${URL.createObjectURL(file)}"></video>`;
        }

        if (!modalInstance) {
            modalInstance = new bootstrap.Modal(modal);
        }
        modalInstance.show();
    };

    window.openExistingMedia = function(url, type) {
        let modal = document.getElementById('existingMediaModal');
        if (!modal) {
            modal = document.createElement('div');
            modal.className = 'modal fade';
            modal.id = 'existingMediaModal';
            modal.tabIndex = '-1';
            modal.innerHTML = `
                <div class="modal-dialog modal-dialog-centered modal-lg">
                    <div class="modal-content bg-dark border-0">
                        <div class="modal-header border-0">
                            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body p-0 d-flex align-items-center justify-content-center" style="min-height: 400px;">
                            <div id="existingModalContent"></div>
                        </div>
                    </div>
                </div>
            `;
            document.body.appendChild(modal);
        }

        const modalContent = modal.querySelector('#existingModalContent');

        if (type === 'image') {
            modalContent.innerHTML = `<img src="${url}" class="img-fluid" style="max-height: 80vh;">`;
        } else {
            modalContent.innerHTML = `<video controls class="w-100" style="max-height: 80vh;"><source src="${url}"></video>`;
        }

        const instance = new bootstrap.Modal(modal);
        instance.show();
    };




    window.openProductImageModal = function(index) {

        const images = window.PRODUCT_IMAGES || [];
        const productTitle = window.PRODUCT_TITLE || 'Товар';

        if (!images || images.length === 0) return;

        let modal = document.getElementById('productImageModal');
        if (!modal) {
            modal = document.createElement('div');
            modal.className = 'modal fade';
            modal.id = 'productImageModal';
            modal.tabIndex = '-1';
            modal.innerHTML = `
                <div class="modal-dialog modal-dialog-centered modal-xl">
                    <div class="modal-content bg-dark border-0">
                        <div class="modal-header border-0">
                            <h5 class="modal-title text-white">${productTitle}</h5>
                            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body p-0 d-flex align-items-center justify-content-center" style="min-height: 600px;">
                            <img id="modalProductImage" src="" class="img-fluid" style="max-height: 85vh;">
                        </div>
                        <div class="modal-footer border-0 bg-dark">
                            <button type="button" class="btn btn-outline-light btn-sm" id="prevImageBtn">
                                <i class="bi bi-chevron-left"></i> Назад
                            </button>
                            <span class="text-white" id="imageCounter">1 / ${images.length}</span>
                            <button type="button" class="btn btn-outline-light btn-sm" id="nextImageBtn">
                                Вперёд <i class="bi bi-chevron-right"></i>
                            </button>
                        </div>
                    </div>
                </div>
            `;
            document.body.appendChild(modal);

            let currentIndex = 0;

            document.getElementById('prevImageBtn').addEventListener('click', function() {
                currentIndex = (currentIndex - 1 + images.length) % images.length;
                updateModalImage();
            });

            document.getElementById('nextImageBtn').addEventListener('click', function() {
                currentIndex = (currentIndex + 1) % images.length;
                updateModalImage();
            });

            function updateModalImage() {
                document.getElementById('modalProductImage').src = images[currentIndex];
                document.getElementById('imageCounter').textContent = `${currentIndex + 1} / ${images.length}`;
            }

            window.productImageModalInstance = new bootstrap.Modal(modal);
        }

        const modalImg = modal.querySelector('#modalProductImage');
        if (modalImg) {
            modalImg.src = images[index];
            modal.querySelector('#imageCounter').textContent = `${index + 1} / ${images.length}`;
        }

        modal.currentIndex = index;

        if (!window.productImageModalInstance) {
            window.productImageModalInstance = new bootstrap.Modal(modal);
        }
        window.productImageModalInstance.show();
    };
});