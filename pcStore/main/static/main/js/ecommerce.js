// main/static/main/js/ecommerce.js
document.addEventListener('DOMContentLoaded', () => {
    function getCSRFToken() {
        const name = 'csrftoken';
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) return decodeURIComponent(cookie.substring(name.length + 1));
        }
        return null;
    }
    const csrfToken = getCSRFToken();
    const isFavoritesPage = window.location.pathname.includes('/cart/favorites/');

    function updateBadge(selector, value) {
        const el = document.querySelector(selector);
        if (el) el.textContent = value;
    }

    function syncButtons(slug, type, isAdded, total = null) {
        const selector = `[data-slug="${slug}"]${type === 'cart' ? '.btn-add-cart' : '.btn-toggle-fav'}`;
        const buttons = document.querySelectorAll(selector);

        console.log(`🔄 syncButtons: ${type} | найдено: ${buttons.length} | isAdded: ${isAdded}`);

        buttons.forEach(btn => {
            // 🔑 1. Удаляем спиннер
            const spinner = btn.querySelector('.spinner-border');
            if (spinner) spinner.remove();

            // 🔑 2. Сбрасываем inline-стили
            btn.style.backgroundColor = '';
            btn.style.color = '';
            btn.style.borderColor = '';

            if (type === 'cart') {
                if (isAdded) {
                    btn.classList.remove('btn-dark');
                    btn.classList.add('btn-success');
                    btn.style.backgroundColor = '#198754';
                    btn.style.color = '#fff';
                    btn.style.borderColor = '#198754';
                    // 🔑 Полностью заменяем HTML
                    btn.innerHTML = '<i class="bi bi-check-lg me-1"></i> В корзине';
                    if (total !== null) updateBadge('.cart-count-badge', total);
                }
            } else {
                // 🔑 ИЗБРАННОЕ — полностью перерисовываем кнопку
                const iconHTML = isAdded
                    ? '<i class="bi bi-heart-fill"></i>'
                    : '<i class="bi bi-heart"></i>';

                if (isAdded) {
                    btn.classList.add('active');
                    btn.style.backgroundColor = '#dc3545';
                    btn.style.color = '#fff';
                    btn.style.borderColor = '#dc3545';
                } else {
                    btn.classList.remove('active');
                    // Возвращаем стандартные стили Bootstrap
                    btn.style.backgroundColor = '';
                    btn.style.color = '';
                    btn.style.borderColor = '';
                }

                // 🔑 Полностью заменяем HTML (важно!)
                btn.innerHTML = iconHTML;

                if (total !== null) updateBadge('.fav-count-badge', total);
            }

            // 🔑 3. Снимаем блокировку
            btn.disabled = false;
            btn.removeAttribute('data-processing');
            console.log(`   ✅ Кнопка обновлена, HTML: "${btn.innerHTML}"`);
        });
    }

    function handleAction(e, type) {
        e.preventDefault();
        const btn = e.target.closest('.btn-add-cart, .btn-toggle-fav');
        if (!btn || btn.getAttribute('data-processing') === 'true') return;

        const slug = btn.dataset.slug;
        if (!slug) return;

        console.log(`🎯 Клик: ${type} | ${slug}`);

        if (type === 'cart' && (btn.classList.contains('btn-success') || btn.innerHTML.includes('В корзине'))) {
            window.location.href = '/cart/';
            return;
        }

        btn.setAttribute('data-processing', 'true');
        btn.disabled = true;
        btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>...';

        const url = type === 'cart' ? `/cart/add/${slug}/` : `/cart/favorites/toggle/${slug}/`;

        fetch(url, {
            method: 'POST',
            headers: { 'X-CSRFToken': csrfToken, 'X-Requested-With': 'XMLHttpRequest' }
        })
        .then(res => {
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return res.json();
        })
        .then(data => {
            console.log(`📦 Ответ:`, data);
            if (data.status === 'ok') {
                if (type === 'cart') {
                    syncButtons(slug, 'cart', true, data.total);
                } else {
                    const favBadge = document.querySelector('.fav-count-badge');
                    let current = parseInt(favBadge?.textContent) || 0;
                    syncButtons(slug, 'fav', data.is_favorited, data.is_favorited ? current + 1 : Math.max(0, current - 1));

                    if (!data.is_favorited && isFavoritesPage) {
                        const col = btn.closest('[class*="col-"]');
                        if (col) {
                            col.style.transition = 'opacity 0.3s ease';
                            col.style.opacity = '0';
                            setTimeout(() => col.remove(), 300);
                        }
                    }
                }
            }
        })
        .catch(err => {
            console.error(`❌ Ошибка:`, err);
            btn.disabled = false;
            btn.removeAttribute('data-processing');
            // Откат к исходному состоянию
            if (type === 'cart') {
                btn.innerHTML = '<i class="bi bi-cart-plus me-1"></i> Купить';
            } else {
                btn.innerHTML = '<i class="bi bi-heart"></i>';
            }
        });
    }

    document.addEventListener('click', (e) => {
        if (e.target.closest('.btn-add-cart')) handleAction(e, 'cart');
        if (e.target.closest('.btn-toggle-fav')) handleAction(e, 'fav');
    });
});