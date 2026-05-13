import os
import django
import random

# Настройка окружения Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcStore.settings')
django.setup()

from catalog.models import Category, Product

print("🚀 Запуск генерации тестовых данных...")

# 1. Категории
categories_data = [
    {'title': 'Процессоры', 'slug': 'cpu', 'icon': 'bi-cpu'},
    {'title': 'Видеокарты', 'slug': 'gpu', 'icon': 'bi-display'},
    {'title': 'Оперативная память', 'slug': 'ram', 'icon': 'bi-memory'},
    {'title': 'Материнские платы', 'slug': 'motherboard', 'icon': 'bi-hdd-rack'},
    {'title': 'SSD Накопители', 'slug': 'ssd', 'icon': 'bi-sd-card'},
]

# 2. Товары: (название, slug_категории, цена, бренд, краткие характеристики)
products_data = [
    # CPU (18 шт)
    ('Intel Core i3-13100F', 'cpu', 9990, 'Intel', '4 ядра, 4.5 ГГц, LGA1700'),
    ('Intel Core i5-12400F', 'cpu', 12990, 'Intel', '6 ядер, 4.4 ГГц, LGA1700'),
    ('Intel Core i5-13500', 'cpu', 21990, 'Intel', '14 ядер, 4.8 ГГц, LGA1700'),
    ('Intel Core i7-13700K', 'cpu', 34990, 'Intel', '16 ядер, 5.4 ГГц, LGA1700'),
    ('Intel Core i7-14700K', 'cpu', 38990, 'Intel', '20 ядер, 5.6 ГГц, LGA1851'),
    ('Intel Core i9-13900KS', 'cpu', 64990, 'Intel', '24 ядра, 6.0 ГГц, LGA1700'),
    ('Intel Core i9-14900K', 'cpu', 59990, 'Intel', '24 ядра, 6.0 ГГц, LGA1851'),
    ('AMD Ryzen 5 5600', 'cpu', 10990, 'AMD', '6 ядер, 4.4 ГГц, AM4'),
    ('AMD Ryzen 5 7600X', 'cpu', 19990, 'AMD', '6 ядер, 5.3 ГГц, AM5'),
    ('AMD Ryzen 7 5700X', 'cpu', 16990, 'AMD', '8 ядер, 4.6 ГГц, AM4'),
    ('AMD Ryzen 7 7700X', 'cpu', 29990, 'AMD', '8 ядер, 5.4 ГГц, AM5'),
    ('AMD Ryzen 7 7800X3D', 'cpu', 39990, 'AMD', '8 ядер, 5.0 ГГц, 3D V-Cache, AM5'),
    ('AMD Ryzen 9 5900X', 'cpu', 28990, 'AMD', '12 ядер, 4.8 ГГц, AM4'),
    ('AMD Ryzen 9 7900', 'cpu', 37990, 'AMD', '12 ядер, 5.4 ГГц, AM5'),
    ('AMD Ryzen 9 7950X3D', 'cpu', 54990, 'AMD', '16 ядер, 5.7 ГГц, 3D V-Cache, AM5'),
    ('AMD Ryzen 9 9950X', 'cpu', 59990, 'AMD', '16 ядер, 5.7 ГГц, Zen 5, AM5'),
    ('Intel Core Ultra 7 265K', 'cpu', 39990, 'Intel', '20 ядер, 5.5 ГГц, LGA1851'),
    ('AMD Ryzen 5 8600G', 'cpu', 18990, 'AMD', '6 ядер, 5.0 ГГц, Radeon 760M, AM5'),

    # GPU (18 шт)
    ('NVIDIA RTX 3060 12GB', 'gpu', 26990, 'NVIDIA', '192-бит, GDDR6, DLSS 2'),
    ('NVIDIA RTX 3070 Ti 8GB', 'gpu', 34990, 'NVIDIA', '256-бит, GDDR6X'),
    ('NVIDIA RTX 4060 8GB', 'gpu', 32990, 'NVIDIA', '128-бит, GDDR6, DLSS 3'),
    ('NVIDIA RTX 4060 Ti 8GB', 'gpu', 42990, 'NVIDIA', '128-бит, GDDR6'),
    ('NVIDIA RTX 4070 Super 12GB', 'gpu', 64990, 'NVIDIA', '192-бит, GDDR6X'),
    ('NVIDIA RTX 4070 Ti Super 16GB', 'gpu', 79990, 'NVIDIA', '256-бит, GDDR6X'),
    ('NVIDIA RTX 4080 Super 16GB', 'gpu', 99990, 'NVIDIA', '256-бит, GDDR6X'),
    ('NVIDIA RTX 4090 24GB', 'gpu', 189990, 'NVIDIA', '384-бит, GDDR6X'),
    ('AMD RX 6600 8GB', 'gpu', 19990, 'AMD', '128-бит, GDDR6, FSR 3'),
    ('AMD RX 6700 XT 12GB', 'gpu', 28990, 'AMD', '192-бит, GDDR6'),
    ('AMD RX 7600 8GB', 'gpu', 27990, 'AMD', '128-бит, GDDR6, RDNA 3'),
    ('AMD RX 7700 XT 12GB', 'gpu', 44990, 'AMD', '192-бит, GDDR6'),
    ('AMD RX 7800 XT 16GB', 'gpu', 54990, 'AMD', '256-бит, GDDR6'),
    ('AMD RX 7900 GRE 16GB', 'gpu', 59990, 'AMD', '256-бит, GDDR6'),
    ('AMD RX 7900 XTX 24GB', 'gpu', 99990, 'AMD', '384-бит, GDDR6'),
    ('Intel Arc A750 8GB', 'gpu', 22990, 'Intel', '256-бит, GDDR6, XeSS'),
    ('Intel Arc A770 16GB', 'gpu', 28990, 'Intel', '256-бит, GDDR6'),
    ('NVIDIA RTX 4090D 24GB', 'gpu', 159990, 'NVIDIA', '384-бит, Китайская версия'),

    # RAM (16 шт)
    ('Kingston Fury Beast 16GB DDR4 3200MHz', 'ram', 3990, 'Kingston', 'CL16, 1.35V'),
    ('Kingston Fury Beast 32GB DDR4 3600MHz', 'ram', 7990, 'Kingston', 'CL18, 1.35V'),
    ('Kingston Fury Beast 32GB DDR5 5600MHz', 'ram', 11990, 'Kingston', 'CL40, 1.1V'),
    ('G.Skill Trident Z5 RGB 32GB DDR5 6000MHz', 'ram', 14990, 'G.Skill', 'CL36, RGB'),
    ('G.Skill Trident Z5 Neo 32GB DDR5 6400MHz', 'ram', 16990, 'G.Skill', 'CL32, AMD EXPO'),
    ('Corsair Vengeance 32GB DDR5 5200MHz', 'ram', 10990, 'Corsair', 'CL40, черный'),
    ('Corsair Dominator Platinum 32GB DDR5 6200MHz', 'ram', 21990, 'Corsair', 'CL30, RGB'),
    ('ADATA XPG Lancer 32GB DDR5 6000MHz', 'ram', 12990, 'ADATA', 'CL38, Intel/AMD'),
    ('TeamGroup T-Force Delta 32GB DDR5 6400MHz', 'ram', 13990, 'TeamGroup', 'CL36, RGB'),
    ('Crucial Pro 32GB DDR5 5600MHz', 'ram', 9990, 'Crucial', 'CL46, низкопрофильный'),
    ('Samsung 32GB DDR5 4800MHz', 'ram', 8990, 'Samsung', 'CL40, OEM'),
    ('Kingston Fury Renegade 32GB DDR5 7200MHz', 'ram', 24990, 'Kingston', 'CL34, разгонный'),
    ('G.Skill Ripjaws S5 16GB DDR5 5200MHz', 'ram', 5990, 'G.Skill', 'CL36, бюджетный'),
    ('Corsair Vengeance LPX 32GB DDR4 3200MHz', 'ram', 6990, 'Corsair', 'CL16, низкопрофильный'),
    ('ADATA XPG Lancer Blade 32GB DDR5 6000MHz', 'ram', 11990, 'ADATA', 'CL30, AMD EXPO'),
    ('Kingston Fury Beast 64GB DDR5 5200MHz', 'ram', 19990, 'Kingston', 'CL42, 2x32GB'),

    # Motherboard (18 шт)
    ('ASUS Prime B660M-A', 'motherboard', 10990, 'ASUS', 'B660, DDR4, mATX, LGA1700'),
    ('MSI PRO B760M-A WiFi', 'motherboard', 13990, 'MSI', 'B760, DDR5, mATX, LGA1700'),
    ('Gigabyte B760M AORUS ELITE AX', 'motherboard', 15990, 'Gigabyte', 'B660, DDR5, mATX, WiFi 6E'),
    ('ASUS ROG Strix Z790-A Gaming WiFi', 'motherboard', 29990, 'ASUS', 'Z790, DDR5, ATX, WiFi 6E'),
    ('MSI MAG Z790 TOMAHAWK WiFi', 'motherboard', 27990, 'MSI', 'Z790, DDR5, ATX, 2.5G LAN'),
    ('ASRock B650M-HDV/M.2', 'motherboard', 9990, 'ASRock', 'B650, DDR5, mATX, AM5'),
    ('ASUS TUF Gaming B650-PLUS WiFi', 'motherboard', 19990, 'ASUS', 'B650, DDR5, ATX, AM5'),
    ('Gigabyte B650 AORUS ELITE AX', 'motherboard', 18990, 'Gigabyte', 'B650, DDR5, ATX, AM5'),
    ('MSI MAG X670E TOMAHAWK WiFi', 'motherboard', 26990, 'MSI', 'X670E, DDR5, ATX, PCIe 5.0'),
    ('ASUS ROG Crosshair X670E HERO', 'motherboard', 44990, 'ASUS', 'X670E, DDR5, ATX, 10Gb LAN'),
    ('Gigabyte Z790 AORUS PRO X', 'motherboard', 28990, 'Gigabyte', 'Z790, DDR5, ATX, WiFi 7'),
    ('MSI MPG Z790 EDGE WiFi', 'motherboard', 31990, 'MSI', 'Z790, DDR5, ATX, 2.5G LAN'),
    ('ASRock B760M Pro RS/D4', 'motherboard', 8990, 'ASRock', 'B760, DDR4, mATX, LGA1700'),
    ('ASUS Prime B760-PLUS D4', 'motherboard', 11990, 'ASUS', 'B760, DDR4, ATX, LGA1700'),
    ('Gigabyte B650M AORUS ELITE AX ICE', 'motherboard', 20990, 'Gigabyte', 'B650, DDR5, mATX, Белая'),
    ('MSI PRO B650-P WiFi', 'motherboard', 14990, 'MSI', 'B650, DDR5, ATX, AM5'),
    ('ASUS ROG Strix B650E-F Gaming WiFi', 'motherboard', 24990, 'ASUS', 'B650E, DDR5, ATX, PCIe 5.0'),
    ('ASRock X670E Taichi', 'motherboard', 39990, 'ASRock', 'X670E, DDR5, ATX, Thunderbolt 4'),

    # SSD (18 шт)
    ('Kingston A400 480GB SATA', 'ssd', 2990, 'Kingston', '500/450 МБ/с, 2.5"'),
    ('Samsung 870 EVO 1TB SATA', 'ssd', 7990, 'Samsung', '560/530 МБ/с, 2.5"'),
    ('Crucial MX500 1TB SATA', 'ssd', 6990, 'Crucial', '560/510 МБ/с, 2.5"'),
    ('Kingston NV2 500GB NVMe', 'ssd', 3490, 'Kingston', 'Gen4, 3500/2100 МБ/с'),
    ('Kingston NV2 1TB NVMe', 'ssd', 5490, 'Kingston', 'Gen4, 3500/2800 МБ/с'),
    ('Kingston NV2 2TB NVMe', 'ssd', 9990, 'Kingston', 'Gen4, 3500/2800 МБ/с'),
    ('Samsung 980 1TB NVMe', 'ssd', 7490, 'Samsung', 'Gen3, 3500/3000 МБ/с'),
    ('Samsung 980 PRO 1TB NVMe', 'ssd', 9990, 'Samsung', 'Gen4, 7000/5000 МБ/с'),
    ('Samsung 980 PRO 2TB NVMe', 'ssd', 16990, 'Samsung', 'Gen4, 7000/5100 МБ/с'),
    ('Samsung 990 PRO 1TB NVMe', 'ssd', 11990, 'Samsung', 'Gen4, 7450/6900 МБ/с'),
    ('Samsung 990 PRO 2TB NVMe', 'ssd', 18990, 'Samsung', 'Gen4, 7450/6900 МБ/с'),
    ('Samsung 990 PRO 4TB NVMe', 'ssd', 34990, 'Samsung', 'Gen4, 7450/6900 МБ/с'),
    ('WD Black SN770 1TB NVMe', 'ssd', 8490, 'WD', 'Gen4, 5150/4900 МБ/с'),
    ('WD Black SN770 2TB NVMe', 'ssd', 13990, 'WD', 'Gen4, 5150/4850 МБ/с'),
    ('Crucial P3 Plus 1TB NVMe', 'ssd', 6490, 'Crucial', 'Gen4, 5000/3600 МБ/с'),
    ('Crucial P3 Plus 2TB NVMe', 'ssd', 10990, 'Crucial', 'Gen4, 5000/4200 МБ/с'),
    ('ADATA Legend 960 1TB NVMe', 'ssd', 7990, 'ADATA', 'Gen4, 7400/6800 МБ/с'),
    ('ADATA Legend 960 2TB NVMe', 'ssd', 13990, 'ADATA', 'Gen4, 7400/6800 МБ/с'),
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
            'description': f"{title} — отличный выбор для сборки ПК. {info}. Официальная гарантия производителя.",
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