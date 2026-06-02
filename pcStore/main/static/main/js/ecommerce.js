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

    // 🔑 Обновляет ВСЕ кнопки с этим slug на всей странице
    function syncButtons(slug, type, isAdded, total = null) {
        const selector = `[data-slug="${slug}"]${type === 'cart' ? '.btn-add-cart' : '.btn-toggle-fav'}`;
        const buttons = document.querySelectorAll(selector);

        buttons.forEach(btn => {
            const spinner = btn.querySelector('.spinner-border');
            if (spinner) spinner.remove();

            // Сброс стилей
            btn.style.backgroundColor = '';
            btn.style.color = '';
            btn.style.borderColor = '';

            if (type === 'cart') {
                if (isAdded) {
                    btn.classList.remove('btn-dark', 'btn-primary');
                    btn.classList.add('btn-success');
                    btn.style.backgroundColor = '#198754';
                    btn.style.color = '#fff';
                    btn.style.borderColor = '#198754';
                    btn.innerHTML = '<i class="bi bi-check-lg me-1"></i> В корзине';
                    if (total !== null) updateBadge('.cart-count-badge', total);
                } else {
                    btn.classList.remove('btn-success');
                    btn.classList.add('btn-primary'); // Или btn-dark, в зависимости от твоего дизайна
                    btn.innerHTML = '<i class="bi bi-cart-plus me-1"></i> В корзину';
                }
            } else {
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
                    // Стили сбрасываются выше
                }
                btn.innerHTML = iconHTML;

                if (total !== null) {
                    updateBadge('.fav-count-badge', total);
                } else {
                    // Если total не передан, пробуем вычислить локально
                    const favBadge = document.querySelector('.fav-count-badge');
                    let current = parseInt(favBadge?.textContent) || 0;
                    updateBadge('.fav-count-badge', isAdded ? current + 1 : Math.max(0, current - 1));
                }
            }

            btn.disabled = false;
            btn.removeAttribute('data-processing');
        });
    }

    function handleAction(e, type) {
        e.preventDefault();
        const btn = e.target.closest('.btn-add-cart, .btn-toggle-fav');
        if (!btn || btn.getAttribute('data-processing') === 'true') return;

        const slug = btn.dataset.slug;
        if (!slug) return;

        // 🔑 Для корзины: если уже добавлено → редирект
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
            headers: {
                'X-CSRFToken': csrfToken,
                'X-Requested-With': 'XMLHttpRequest'
            }
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
                    // 🔑 Если удаляем из избранного НА СТРАНИЦЕ ИЗБРАННОГО → перезагружаем
                    if (!data.is_favorited && isFavoritesPage) {
                        window.location.reload();
                        return;
                    }
                    // Для всех остальных случаев
                    syncButtons(slug, 'fav', data.is_favorited, data.total);
                }
            }
        })
        .catch(err => {
            console.error(`❌ Ошибка:`, err);
            btn.disabled = false;
            btn.removeAttribute('data-processing');
            if (type === 'cart') {
                btn.classList.remove('btn-success');
                btn.classList.add('btn-primary');
                btn.innerHTML = '<i class="bi bi-cart-plus me-1"></i> В корзину';
            } else {
                btn.classList.remove('active');
                btn.innerHTML = '<i class="bi bi-heart"></i>';
            }
        });
    }

    // 🔥 ГЛАВНЫЙ ОБРАБОТЧИК КЛИКОВ С ПРОВЕРКОЙ АВТОРИЗАЦИИ
    document.addEventListener('click', (e) => {
        const cartBtn = e.target.closest('.btn-add-cart');
        const favBtn = e.target.closest('.btn-toggle-fav');

        if (cartBtn || favBtn) {
            // Проверяем статус авторизации. Если false или undefined - блокируем всё.
            if (window.IS_AUTHENTICATED !== true) {
                e.preventDefault();      // Отменяем стандартное действие
                e.stopPropagation();     // Останавливаем всплытие события

                const loginUrl = window.LOGIN_URL || '/auth/login/';

                // Перенаправляем на страницу входа
                window.location.href = loginUrl;
                return; // ВАЖНО: выходим из функции, fetch НИКОГДА не запустится
            }

            // Если код дошел сюда, значит пользователь ТОЧНО авторизован
            if (cartBtn) handleAction(e, 'cart');
            if (favBtn) handleAction(e, 'fav');
        }
    });
});