import os
import django
import random

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcStore.settings')
django.setup()

from catalog.models import Category, Product

print(" Запуск генерации тестовых данных (HDD, Охлаждение, БП, Корпуса)...")

# 1. Категории
categories_data = [
    {'title': 'HDD Накопители', 'slug': 'hdd', 'icon': 'bi-hdd'},
    {'title': 'Охлаждение', 'slug': 'pc-cooling', 'icon': 'bi-fan'},
    {'title': 'Блоки питания', 'slug': 'psu', 'icon': 'bi-plug'},
    {'title': 'Корпуса', 'slug': 'pc-case', 'icon': 'bi-box'},
]

# 2. Товары: (название, slug_категории, цена, бренд, краткие характеристики)
products_data = [
    # HDD (10 шт)
    ('Seagate Barracuda 1TB', 'hdd', 4200, 'Seagate', '3.5", 7200 об/мин, 256 МБ кэш'),
    ('WD Blue 2TB', 'hdd', 5600, 'WD', '3.5", 5400 об/мин, 256 МБ кэш'),
    ('Seagate IronWolf 4TB', 'hdd', 9800, 'Seagate', 'NAS, 5900 об/мин, CMR технология'),
    ('WD Red Plus 6TB', 'hdd', 13500, 'WD', 'NAS, 5400 об/мин, оптимизация под RAID'),
    ('Seagate Exos X18 16TB', 'hdd', 24900, 'Seagate', 'Серверный, 7200 об/мин, 256 МБ кэш'),
    ('WD Purple 4TB', 'hdd', 8900, 'WD', 'Видеонаблюдение, AllFrame технология'),
    ('Toshiba P300 1TB', 'hdd', 3800, 'Toshiba', 'Бюджетный десктопный, 7200 об/мин'),
    ('Seagate Barracuda 4TB', 'hdd', 8200, 'Seagate', 'Архивный, 5400 об/мин, тихий'),
    ('WD Gold 10TB', 'hdd', 28900, 'WD', 'ЦОД, 7200 об/мин, 2.5 млн часов MTBF'),
    ('Seagate SkyHawk AI 8TB', 'hdd', 18500, 'Seagate', 'AI-видеоаналитика, 24/7 нагрузка'),

    # Охлаждение (10 шт)
    ('DeepCool AK400', 'pc-cooling', 2400, 'DeepCool', 'Башенный, 4 теплотрубки, 220 Вт TDP'),
    ('ID-COOLING SE-214-XT', 'pc-cooling', 1500, 'ID-COOLING', 'Бюджетный башенный, 180 Вт TDP'),
    ('Arctic Freezer 34 eSports DUO', 'pc-cooling', 3200, 'Arctic', 'Два вентилятора P12, 250 Вт TDP'),
    ('be quiet! Dark Rock 4', 'pc-cooling', 6500, 'be quiet!', 'Премиум тишина, 200 Вт TDP'),
    ('Noctua NH-U12S redux', 'pc-cooling', 5400, 'Noctua', 'Надежность, 6 лет гарантии'),
    ('DeepCool LS720 SE', 'pc-cooling', 8900, 'DeepCool', 'СЖО 360мм, ARGB подсветка'),
    ('NZXT Kraken X63', 'pc-cooling', 11500, 'NZXT', 'СЖО 280мм, LCD экран помпы'),
    ('Corsair iCUE H150i Elite', 'pc-cooling', 13900, 'Corsair', 'СЖО 360мм, RGB вентиляторы'),
    ('Arctic Liquid Freezer II 280', 'pc-cooling', 9200, 'Arctic', 'СЖО с VRM вентилятором'),
    ('Thermalright Peerless Assassin 120', 'pc-cooling', 2900, 'Thermalright', 'Двухбашенный, топ за свои деньги'),

    # Блоки питания (10 шт)
    ('DeepCool PF500', 'psu', 2800, 'DeepCool', '500 Вт, 80+ White, не модульный'),
    ('Corsair CV550', 'psu', 4200, 'Corsair', '550 Вт, 80+ Bronze, тихий вентилятор'),
    ('be quiet! System Power 10 650W', 'psu', 5800, 'be quiet!', '650 Вт, 80+ Bronze, DC-DC'),
    ('Corsair RM750e', 'psu', 9500, 'Corsair', '750 Вт, 80+ Gold, полностью модульный'),
    ('be quiet! Straight Power 12 850W', 'psu', 14500, 'be quiet!', '850 Вт, 80+ Platinum, ATX 3.0'),
    ('Seasonic Focus GX-750', 'psu', 10200, 'Seasonic', '750 Вт, 80+ Gold, гибридный режим'),
    ('DeepCool PQ750M', 'psu', 6900, 'DeepCool', '750 Вт, 80+ Gold, модульный'),
    ('NZXT C850', 'psu', 11900, 'NZXT', '850 Вт, 80+ Gold, плоские кабели'),
    ('Thermaltake Toughpower GF1 750W', 'psu', 8700, 'Thermaltake', '750 Вт, 80+ Gold, нулевые обороты'),
    ('FSP Hydro G Pro 850W', 'psu', 10800, 'FSP', '850 Вт, 80+ Gold, японские конденсаторы'),

    # Корпуса (10 шт)
    ('DeepCool MATREXX 30', 'pc-case', 3200, 'DeepCool', 'mATX, сетка спереди, 1 вентилятор'),
    ('Cougar MX330-G Air', 'pc-case', 4100, 'Cougar', 'ATX, стекло, 3x 120мм RGB'),
    ('NZXT H5 Flow', 'pc-case', 8500, 'NZXT', 'ATX, отличный продув, современный дизайн'),
    ('Fractal Design Pop Air', 'pc-case', 7800, 'Fractal', 'ATX, 3x 120мм, шумоизоляция'),
    ('Lian Li Lancool 216', 'pc-case', 9200, 'Lian Li', 'ATX, 2x 160мм спереди, GPU 400мм'),
    ('Corsair 4000D Airflow', 'pc-case', 7400, 'Corsair', 'ATX, сетка, кабель-менеджмент'),
    ('be quiet! Pure Base 500DX', 'pc-case', 8900, 'be quiet!', 'ATX, 3x 140мм, ARGB'),
    ('Phanteks Eclipse G360A', 'pc-case', 6500, 'Phanteks', 'ATX, воздушный поток, D-RGB'),
    ('DeepCool CH560 Digital', 'pc-case', 10500, 'DeepCool', 'ATX, LCD экран, 4x 120мм'),
    ('Montech Air 100 ARGB', 'pc-case', 4800, 'Montech', 'mATX, 4x 120мм, стеклянная дверь'),
]

created_cats = 0
created_prods = 0

try:
    # 1. Создаём категории
    for cat_info in categories_data:
        _, created = Category.objects.get_or_create(slug=cat_info['slug'], defaults=cat_info)
        if created:
            created_cats += 1

    # 2. Создаём товары
    for title, cat_slug, price, brand, info in products_data:
        cat = Category.objects.get(slug=cat_slug)

        # Формируем дефолтные значения
        defaults = {
            'price': price,
            'brand': brand,
            'info': info,
            'description': f"{title} — отличное решение для вашей сборки. {info}. Официальная гарантия производителя.",
            'in_stock': random.randint(5, 120),
            'warranty': '24 месяца',
            'is_active': True,
            'is_new': random.choice([True, False, False]),  # ~30% новинок
            'is_hit': random.choice([True, False, False]),  # ~30% хитов
            'old_price': price + random.randint(500, 3000) if random.random() > 0.7 else None
        }

        prod, created = Product.objects.get_or_create(title=title, defaults=defaults)
        if created:
            prod.categories.add(cat)
            created_prods += 1
        elif cat not in prod.categories.all():
            prod.categories.add(cat)  # Привязываем, если товар уже был в БД

    print(f"\n✅ Готово! Добавлено категорий: {created_cats}, товаров: {created_prods}")

except Exception as e:
    print(f"\n❌ Ошибка при заполнении: {e}")