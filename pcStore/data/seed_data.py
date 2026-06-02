
import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcStore.settings')
django.setup()

from catalog.models import Product, Category

BRANDS = ["NVIDIA", "AMD", "Intel", "Samsung", "Kingston", "Corsair", "Seagate", "MSI", "ASUS", "Gigabyte"]
MODELS = ["RTX 4060", "RTX 4070", "Ryzen 5 5600", "Ryzen 7 5800X", "Core i5-12400", "Core i7-13700K",
          "Fury Beast 32GB", "Aorus Elite", "P44 Pro", "IronWolf 4TB", "Barracuda 2TB", "Vengeance DDR5"]
CATEGORIES_MAP = {
    "Процессоры": ["Ryzen", "Core"],
    "Видеокарты": ["RTX", "RX"],
    "Оперативная память": ["Fury", "Vengeance", "DDR5"],
    "SSD": ["Pro", "P44", "IronWolf"],
    "Материнские платы": ["Aorus", "MSI", "Gigabyte"]
}

def seed():
    print("🌱 Начинаю наполнение базы данных...")

    categories = {}
    for cat_name in CATEGORIES_MAP.keys():
        cat, created = Category.objects.get_or_create(title=cat_name)
        categories[cat_name] = cat
        if created:
            print(f"   + Создана категория: {cat_name}")

    for i in range(50):

        cat_name = random.choice(list(categories.keys()))
        category = categories[cat_name]

        valid_brands = ["Intel", "AMD"] if cat_name == "Процессоры" else BRANDS
        brand = random.choice(valid_brands)
        model = random.choice(MODELS)

        title = f"{brand} {model} - Версия {random.randint(10, 99)}"
        price = random.randint(4000, 85000)

        product = Product.objects.create(
            title=title,
            brand=brand,
            price=price,
            info=f"Характеристики: {model}, Бренд: {brand}, Скорость: {random.randint(3000, 6000)} MHz",
            in_stock=random.randint(1, 50),
            warranty="12 месяцев",

        )

        product.categories.add(category)

    print("✅ Готово! Создано 50 товаров.")
    print("💡 Теперь заходи в админку или на страницу товара, чтобы тестировать карусели.")

if __name__ == '__main__':
    seed()