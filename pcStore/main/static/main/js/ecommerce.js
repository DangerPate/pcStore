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

    // 🔑 Обновляет состояние кнопок, сохраняя их оригинальные классы (btn-lg, btn-sm и т.д.)
    function syncButtons(slug, type, isAdded, total = null) {
        const selector = `[data-slug="${slug}"]${type === 'cart' ? '.btn-add-cart' : '.btn-toggle-fav'}`;

        document.querySelectorAll(selector).forEach(btn => {
            if (type === 'cart') {
                if (isAdded) {
                    // 🔑 Меняем только цвет и текст, сохраняя btn-lg/px-4 и другие классы
                    btn.classList.remove('btn-dark');
                    btn.classList.add('btn-success');
                    btn.innerHTML = '<i class="bi bi-check-lg me-1"></i> В корзине';
                    if (total !== null) updateBadge('.cart-count-badge', total);
                }
            } else {
                const icon = btn.querySelector('i');
                if (isAdded) {
                    btn.classList.add('active');
                    if (icon) icon.classList.replace('bi-heart', 'bi-heart-fill');
                } else {
                    btn.classList.remove('active');
                    if (icon) icon.classList.replace('bi-heart-fill', 'bi-heart');
                }
                if (total !== null) updateBadge('.fav-count-badge', total);
            }
            // 🔑 Снимаем блокировку и спиннер
            btn.disabled = false;
            btn.dataset.processing = 'false';
        });
    }

    function handleAction(e, type) {
        e.preventDefault();
        const btn = e.target.closest('.btn-add-cart, .btn-toggle-fav');
        if (!btn) return;

        // Если уже обрабатывается — игнорируем повторный клик
        if (btn.dataset.processing === 'true') return;

        const slug = btn.dataset.slug;
        if (!slug) return;

        // Для корзины: если уже добавлено → редирект
        if (type === 'cart' && (btn.classList.contains('btn-success') || btn.innerHTML.includes('В корзине'))) {
            window.location.href = '/cart/';
            return;
        }

        // 🔑 Блокируем кнопку и показываем спиннер
        btn.dataset.processing = 'true';
        btn.disabled = true;
        const originalHTML = btn.innerHTML;
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
            if (data.status === 'ok') {
                if (type === 'cart') {
                    syncButtons(slug, 'cart', true, data.total);
                } else {
                    const favBadge = document.querySelector('.fav-count-badge');
                    let current = parseInt(favBadge?.textContent) || 0;
                    syncButtons(slug, 'fav', data.is_favorited, data.is_favorited ? current + 1 : Math.max(0, current - 1));

                    // Удаляем карточку только на странице избранного
                    if (!data.is_favorited && isFavoritesPage) {
                        const col = btn.closest('[class*="col-"]');
                        if (col) {
                            col.style.transition = 'opacity 0.3s ease';
                            col.style.opacity = '0';
                            setTimeout(() => col.remove(), 300);
                        }
                    }
                }
            } else {
                // Если сервер вернул ошибку — откатываем состояние
                btn.innerHTML = originalHTML;
                btn.disabled = false;
                btn.dataset.processing = 'false';
            }
        })
        .catch(err => {
            console.error(`${type} error:`, err);
            // 🔑 При ошибке сети — откатываем кнопку
            btn.innerHTML = originalHTML;
            btn.disabled = false;
            btn.dataset.processing = 'false';
        });
        // ❌ Убираем .finally(), чтобы не дублировать разблокировку
    }

    // Делегирование событий
    document.addEventListener('click', (e) => {
        if (e.target.closest('.btn-add-cart')) handleAction(e, 'cart');
        if (e.target.closest('.btn-toggle-fav')) handleAction(e, 'fav');
    });
});