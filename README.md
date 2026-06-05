<div align="center">

# 🖥️ pcStore

### Интернет-магазин компьютерных комплектующих

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0.5-green?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18.3-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Полнофункциональный веб-магазин на Django с модульной архитектурой, корзиной, избранным и оптимизированной работой с БД**

[Особенности](#-особенности) • [Технологии](#-технологический-стек) • [Установка](#-установка) • [Запуск](#-запуск-проекта) • [Структура](#-структура-проекта)

</div>

---

## 📖 О проекте

**pcStore** — это веб-приложение для розничной продажи компьютерных комплектующих, разработанное на базе фреймворка **Django**. Проект реализует полный цикл взаимодействия покупателя с каталогом: от поиска и фильтрации товаров до управления персональными списками (корзина, избранное).

Ключевой архитектурной особенностью является **модульная структура** Django-приложений, где каждый компонент (каталог, карточка товара, корзина, пользователи) представляет собой изолированный модуль со своей областью ответственности.

> 🎓 Проект разработан в рамках выпускной квалификационной работы по специальности *09.02.07 «Информационные системы и программирование»*.

---

## ✨ Особенности

### 🛒 Функциональность для покупателя
- 📂 **Каталог из 9 категорий** комплектующих: видеокарты, процессоры, материнские платы, ОЗУ, SSD, HDD, блоки питания, системы охлаждения, корпуса
- 🔍 **Полнотекстовый поиск** по названию, описанию, бренду и категориям
- 🏷️ **Фильтрация** по цене, бренду, наличию на складе
- 🛍️ **Корзина** с сохранением состояния между сессиями
- ❤️ **Избранное** для отложенных покупок
- 👤 **Кастомная авторизация** по email (вместо стандартного username)

### ⚙️ Технические особенности
- 🚀 **Оптимизация ORM**: `select_related`, `prefetch_related`, `Exists`, `OuterRef` — защита от N+1 запросов
- 🔒 **Безопасность**: защита от CSRF, XSS, SQL-инъекций, хеширование паролей (PBKDF2-SHA256)
- 🌐 **Читаемые URL** на основе `slug` для товаров и категорий
- 🔗 **ManyToMany** связь между товарами и категориями
- 📱 **Адаптивная вёрстка** на Bootstrap 5 (от 320px до 1920px)
- ⚡ **Асинхронные AJAX-запросы** для добавления в корзину без перезагрузки страницы
- 🎨 **Компонентный подход**: переиспользуемый `mini_product_card.html`

### 🛠️ Для администратора
- Административная панель Django Admin с кастомизированными фильтрами и поиском
- Управление публикацией товаров, остатками на складе, маркетинговыми флагами
- Разграничение прав доступа (гость / пользователь / staff / суперпользователь)

---

## 🛠 Технологический стек

| Категория | Технология | Версия |
|:---|:---|:-------|
| **Backend** | Python | 3.14+  |
| **Framework** | Django | 6.0.5  |
| **База данных** | PostgreSQL | 18.3   |
| **ORM-драйвер** | psycopg2-binary | 2.9+   |
| **Изображения** | Pillow | 10.0+  |
| **Frontend** | HTML5 / CSS3 / JavaScript (ES6+) | —      |
| **CSS-фреймворк** | Bootstrap | 5.3    |
| **Иконки** | Bootstrap Icons | 1.11   |
| **Контроль версий** | Git + GitHub | —      |

---

## 📁 Структура проекта
```
pcStore/
├── manage.py                    # Точка входа Django
├── requirements.txt             # Зависимости проекта
├── README.md                    # Этот файл
├── .env.example                 # Шаблон переменных окружения
│
├── pcStore/                     # Главный проект
│   ├── settings.py              # Конфигурация Django
│   ├── urls.py                  # Главная маршрутизация
│   ├── asgi.py / wsgi.py        # Точки входа для серверов
│
├── main/                        # 🏠 Главная страница, layout.html
│   ├── views.py
│   ├── urls.py
│   └── templates/main/
│
├── catalog/                     # 📂 Категории, списки, поиск
│   ├── models.py                # Product, Category
│   ├── views.py                 # category_view, search_view
│   ├── urls.py
│   └── templates/catalog/
│
├── product/                     # 🏷️ Шаблоны детальной карточки
│   └── templates/product/
│       ├── product_card.html
│       └── mini_product_card.html
│
├── cart/                        # 🛒 Корзина и избранное
│   ├── models.py                # Cart, CartItem, Favorite
│   ├── views.py                 # add_to_cart, favorites_view
│   └── urls.py
│
├── users/                       # 👤 Регистрация и авторизация
│   ├── models.py                # CustomUser (email-based)
│   ├── forms.py
│   ├── views.py
│   └── urls.py
│
├── static/                      # 🎨 CSS, JS, изображения
└── media/                       # 📸 Загружаемые файлы товаров

```
---

## 🚀 Установка

### Предварительные требования
- Python 3.14+
- PostgreSQL 18.3+
- Git

### Шаг 1. Клонирование репозитория

```bash
git clone https://github.com/DangerPate/pcStore.git
cd pcStore
```
### Шаг 2. Создание виртуального окружения
#### Windows
```commandline
python -m venv .venv
.venv\Scripts\activate
```
#### Linux / macOS
```commandline
python3 -m venv .venv
source .venv/bin/activate
```
### Шаг 3. Установка зависимостей
```commandline
pip install --upgrade pip
pip install -r requirements.txt
```
### Шаг 4. Создание базы данных PostgreSQL
```
-- 1. Создание БД и пользователя
CREATE DATABASE pcstore_db;
CREATE USER pcstore_user WITH PASSWORD 'your_password';
ALTER ROLE pcstore_user SET client_encoding TO 'utf8';
ALTER ROLE pcstore_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE pcstore_user SET timezone TO 'Europe/Moscow';
GRANT ALL PRIVILEGES ON DATABASE pcstore_db TO pcstore_user;

-- 2. Подключаемся к БД и раздаём права на схему/объекты
\c pcstore_db
GRANT ALL ON SCHEMA public TO pcstore_user;
GRANT ALL ON ALL TABLES IN SCHEMA public TO pcstore_user;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO pcstore_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO pcstore_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO pcstore_user;
```
### Шаг 5. Настройка переменных окружения
Создайте файл .env в корне проекта на основе .env.example:
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DB_NAME=pcstore_db
DB_USER=pcstore_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
ALLOWED_HOSTS=localhost,127.0.0.1
```
### Шаг 6. Применение миграций
```commandline
python manage.py makemigrations
python manage.py migrate
```
### Шаг 7. Создание суперпользователя
```commandline
python manage.py createsuperuser
```
### Шаг 8. Сборка статических файлов
```commandline
python manage.py collectstatic --noinput
```
### Запуск проекта
```commandline
python manage.py runserver
```