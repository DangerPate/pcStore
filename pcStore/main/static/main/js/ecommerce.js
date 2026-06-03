if (window.ecommerceInitialized) {
    console.log('⚠️ ecommerce.js уже инициализирован, пропускаем');
} else {
    window.ecommerceInitialized = true;

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

        function updateAllBadges(selector, value) {
            const elements = document.querySelectorAll(selector);
            elements.forEach(el => {
                el.textContent = value;
                el.style.display = value > 0 ? '' : 'none';
            });
        }

        function syncButtons(slug, type, isAdded, total = null) {
            const selector = `[data-slug="${slug}"]${type === 'cart' ? '.btn-add-cart' : '.btn-toggle-fav'}`;
            const buttons = document.querySelectorAll(selector);

            // Сначала обновляем бейджи (ОДИН РАЗ, вне цикла)
            if (type === 'cart') {
                if (total !== null && total !== undefined) {
                    updateAllBadges('.cart-count-badge', total);
                }
            } else {
                if (total !== null && total !== undefined) {
                    updateAllBadges('.fav-count-badge', total);
                } else {
                    const favBadge = document.querySelector('.fav-count-badge');
                    let current = parseInt(favBadge?.textContent) || 0;
                    const newTotal = isAdded ? current + 1 : Math.max(0, current - 1);
                    updateAllBadges('.fav-count-badge', newTotal);
                }
            }

            // Теперь обновляем кнопки
            buttons.forEach(btn => {
                const spinner = btn.querySelector('.spinner-border');
                if (spinner) spinner.remove();

                if (type === 'cart') {
                    // Сбрасываем inline стили
                    btn.style.backgroundColor = '';
                    btn.style.color = '';
                    btn.style.borderColor = '';

                    if (isAdded) {
                        btn.classList.remove('btn-dark', 'btn-primary');
                        btn.classList.add('btn-success');
                        btn.style.backgroundColor = '#198754';
                        btn.style.color = '#fff';
                        btn.style.borderColor = '#198754';
                        btn.innerHTML = '<i class="bi bi-check-lg me-1"></i> В корзине';
                    } else {
                        btn.classList.remove('btn-success');
                        btn.classList.add('btn-primary');
                        btn.innerHTML = '<i class="bi bi-cart-plus me-1"></i> В корзину';
                    }
                } else {
                    // 🔥 ИСПРАВЛЕНИЕ: Явно устанавливаем стили для избранного
                    const iconHTML = isAdded
                        ? '<i class="bi bi-heart-fill"></i>'
                        : '<i class="bi bi-heart"></i>';

                    // Гарантируем видимость кнопки

                    btn.style.display = 'flex';
                    btn.style.visibility = 'visible';
                    btn.style.opacity = '1';
                    btn.style.alignItems = 'center';
                    btn.style.justifyContent = 'center';

                    if (isAdded) {
                        btn.classList.add('active');
                        btn.style.backgroundColor = 'rgb(255, 71, 87)';
                        btn.style.color = '#ffffff';
                        btn.style.borderColor = 'rgb(255, 71, 87)';
                    } else {
                        btn.classList.remove('active');
                        // 🔥 Явно задаём стили для неактивного состояния
                        btn.style.backgroundColor = 'transparent';
                        btn.style.color = 'rgb(255, 71, 87)';
                        btn.style.borderColor = 'rgb(255, 71, 87)';
                    }
                    btn.innerHTML = iconHTML;
                }

                btn.disabled = false;
                btn.removeAttribute('data-processing');
            });
        }

        function handleAction(e, type) {
            e.preventDefault();
            e.stopPropagation();

            const btn = e.target.closest('.btn-add-cart, .btn-toggle-fav');
            if (!btn || btn.getAttribute('data-processing') === 'true') return;

            const slug = btn.dataset.slug;
            if (!slug) return;

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
                        if (!data.is_favorited && isFavoritesPage) {
                            window.location.reload();
                            return;
                        }
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
                    // 🔥 Восстанавливаем стили при ошибке
                    btn.style.display = 'flex';
                    btn.style.visibility = 'visible';
                    btn.style.opacity = '1';
                    btn.style.backgroundColor = 'transparent';
                    btn.style.color = '#ff4757';
                    btn.style.borderColor = '#ff4757';
                    btn.innerHTML = '<i class="bi bi-heart"></i>';
                }
            });
        }

        document.addEventListener('click', (e) => {
            const cartBtn = e.target.closest('.btn-add-cart');
            const favBtn = e.target.closest('.btn-toggle-fav');

            if (cartBtn || favBtn) {
                if (window.IS_AUTHENTICATED !== true) {
                    e.preventDefault();
                    e.stopPropagation();
                    const loginUrl = window.LOGIN_URL || '/auth/login/';
                    window.location.href = loginUrl;
                    return;
                }

                if (cartBtn) handleAction(e, 'cart');
                if (favBtn) handleAction(e, 'fav');
            }
        });
    });
}