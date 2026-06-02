import sys
import os
import django

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pcStore.settings')
django.setup()

import random
from catalog.models import Product, Category

gpu_cat, _ = Category.objects.get_or_create(title='Видеокарты', slug='gpu')

REALISTIC_GPUS = [
    {
        "title": "NVIDIA GeForce RTX 4090 Founders Edition",
        "price": 189990, "brand": "NVIDIA",
        "info": "Флагманская видеокарта для 4K гейминга и профессионального рендеринга.",
        "specs": {
            "gpu_model": "GeForce RTX 4090", "vram": "24 ГБ", "gpu_vendor": "NVIDIA",
            "purpose": "Игровая", "memory_bus": "384 бит", "interface": "PCIe 4.0 x16",
            "cooling": "3 осевых", "memory_type": "GDDR6X", "gpu_series": "NVIDIA GeForce RTX 40",
            "color": "Черный", "length": "300–349 мм"
        }
    },
    {
        "title": "AMD Radeon RX 7900 XTX Reference",
        "price": 114990, "brand": "AMD",
        "info": "Топовая архитектура RDNA 3 для ультра-настроек в 4K.",
        "specs": {
            "gpu_model": "Radeon RX 7900 XTX", "vram": "24 ГБ", "gpu_vendor": "AMD",
            "purpose": "Игровая", "memory_bus": "384 бит", "interface": "PCIe 4.0 x16",
            "cooling": "3 осевых", "memory_type": "GDDR6", "gpu_series": "AMD Radeon RX 7000",
            "color": "Черный", "length": "300–349 мм"
        }
    },
    {
        "title": "NVIDIA GeForce RTX 4080 SUPER",
        "price": 109990, "brand": "NVIDIA",
        "info": "Оптимальный баланс производительности и цены для high-end систем.",
        "specs": {
            "gpu_model": "GeForce RTX 4080 SUPER", "vram": "16 ГБ", "gpu_vendor": "NVIDIA",
            "purpose": "Игровая", "memory_bus": "256 бит", "interface": "PCIe 4.0 x16",
            "cooling": "3 осевых", "memory_type": "GDDR6X", "gpu_series": "NVIDIA GeForce RTX 40",
            "color": "Черный", "length": "300–349 мм"
        }
    },
    {
        "title": "NVIDIA GeForce RTX 4070 Ti SUPER",
        "price": 84990, "brand": "NVIDIA",
        "info": "Улучшенная версия с 16 ГБ памяти для стабильных 1440p.",
        "specs": {
            "gpu_model": "GeForce RTX 4070 Ti SUPER", "vram": "16 ГБ", "gpu_vendor": "NVIDIA",
            "purpose": "Игровая", "memory_bus": "256 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6X", "gpu_series": "NVIDIA GeForce RTX 40",
            "color": "Белый", "length": "250–299 мм"
        }
    },
    {
        "title": "AMD Radeon RX 7800 XT",
        "price": 54990, "brand": "AMD",
        "info": "Народный выбор для 1440p гейминга с большим запасом памяти.",
        "specs": {
            "gpu_model": "Radeon RX 7800 XT", "vram": "16 ГБ", "gpu_vendor": "AMD",
            "purpose": "Игровая", "memory_bus": "256 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "AMD Radeon RX 7000",
            "color": "Черный", "length": "250–299 мм"
        }
    },
    {
        "title": "NVIDIA GeForce RTX 4070 SUPER",
        "price": 64990, "brand": "NVIDIA",
        "info": "Эффективная карта для 2K гейминга с поддержкой DLSS 3.",
        "specs": {
            "gpu_model": "GeForce RTX 4070 SUPER", "vram": "12 ГБ", "gpu_vendor": "NVIDIA",
            "purpose": "Игровая", "memory_bus": "192 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6X", "gpu_series": "NVIDIA GeForce RTX 40",
            "color": "Черный", "length": "250–299 мм"
        }
    },
    {
        "title": "AMD Radeon RX 7700 XT",
        "price": 44990, "brand": "AMD",
        "info": "Средний сегмент RDNA 3 для комфортного 1080p/1440p.",
        "specs": {
            "gpu_model": "Radeon RX 7700 XT", "vram": "12 ГБ", "gpu_vendor": "AMD",
            "purpose": "Игровая", "memory_bus": "192 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "AMD Radeon RX 7000",
            "color": "Черный", "length": "250–299 мм"
        }
    },
    {
        "title": "Intel Arc A770 16GB",
        "price": 32990, "brand": "Intel",
        "info": "Первый флагман Intel с поддержкой AV1 и XeSS.",
        "specs": {
            "gpu_model": "Intel Arc A770", "vram": "16 ГБ", "gpu_vendor": "Intel",
            "purpose": "Игровая", "memory_bus": "256 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "Intel Arc A700",
            "color": "Синий", "length": "250–299 мм"
        }
    },
    {
        "title": "NVIDIA GeForce RTX 4060 Ti 8GB",
        "price": 39990, "brand": "NVIDIA",
        "info": "Энергоэффективная карта для 1080p Ultra.",
        "specs": {
            "gpu_model": "GeForce RTX 4060 Ti", "vram": "8 ГБ", "gpu_vendor": "NVIDIA",
            "purpose": "Игровая", "memory_bus": "128 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "NVIDIA GeForce RTX 40",
            "color": "Белый", "length": "200–249 мм"
        }
    },
    {
        "title": "AMD Radeon RX 7600",
        "price": 28990, "brand": "AMD",
        "info": "Базовая карта поколения RDNA 3 для бюджетных сборок.",
        "specs": {
            "gpu_model": "Radeon RX 7600", "vram": "8 ГБ", "gpu_vendor": "AMD",
            "purpose": "Игровая", "memory_bus": "128 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "AMD Radeon RX 7000",
            "color": "Черный", "length": "200–249 мм"
        }
    },
    {
        "title": "NVIDIA GeForce RTX 4060",
        "price": 31990, "brand": "NVIDIA",
        "info": "Самая популярная карта для entry-level 1080p гейминга.",
        "specs": {
            "gpu_model": "GeForce RTX 4060", "vram": "8 ГБ", "gpu_vendor": "NVIDIA",
            "purpose": "Игровая", "memory_bus": "128 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "NVIDIA GeForce RTX 40",
            "color": "Черный", "length": "200–249 мм"
        }
    },
    {
        "title": "AMD Radeon RX 6700 XT",
        "price": 34990, "brand": "AMD",
        "info": "Проверенная временем карта с 12 ГБ памяти.",
        "specs": {
            "gpu_model": "Radeon RX 6700 XT", "vram": "12 ГБ", "gpu_vendor": "AMD",
            "purpose": "Игровая", "memory_bus": "192 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "AMD Radeon RX 6000",
            "color": "Черный", "length": "250–299 мм"
        }
    },
    {
        "title": "NVIDIA GeForce RTX 3060 12GB",
        "price": 26990, "brand": "NVIDIA",
        "info": "Универсальная карта для игр и начального монтажа видео.",
        "specs": {
            "gpu_model": "GeForce RTX 3060", "vram": "12 ГБ", "gpu_vendor": "NVIDIA",
            "purpose": "Универсальная", "memory_bus": "192 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "NVIDIA GeForce RTX 30",
            "color": "Черный", "length": "200–249 мм"
        }
    },
    {
        "title": "AMD Radeon RX 6600",
        "price": 19990, "brand": "AMD",
        "info": "Отличный выбор для 1080p с низким энергопотреблением.",
        "specs": {
            "gpu_model": "Radeon RX 6600", "vram": "8 ГБ", "gpu_vendor": "AMD",
            "purpose": "Игровая", "memory_bus": "128 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "AMD Radeon RX 6000",
            "color": "Черный", "length": "200–249 мм"
        }
    },
    {
        "title": "Intel Arc A750 8GB",
        "price": 24990, "brand": "Intel",
        "info": "Средний сегмент Intel с отличной производительностью в DX12.",
        "specs": {
            "gpu_model": "Intel Arc A750", "vram": "8 ГБ", "gpu_vendor": "Intel",
            "purpose": "Игровая", "memory_bus": "256 бит", "interface": "PCIe 4.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "Intel Arc A700",
            "color": "Черный", "length": "250–299 мм"
        }
    },
    {
        "title": "NVIDIA GeForce GTX 1660 SUPER",
        "price": 18990, "brand": "NVIDIA",
        "info": "Легендарная бюджетная карта для 1080p.",
        "specs": {
            "gpu_model": "GeForce GTX 1660 SUPER", "vram": "6 ГБ", "gpu_vendor": "NVIDIA",
            "purpose": "Для офиса и дома", "memory_bus": "192 бит", "interface": "PCIe 3.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR6", "gpu_series": "NVIDIA GeForce GTX 16",
            "color": "Черный", "length": "200–249 мм"
        }
    },
    {
        "title": "AMD Radeon RX 580 8GB",
        "price": 8990, "brand": "AMD",
        "info": "Бюджетная классика для нетребовательных игр.",
        "specs": {
            "gpu_model": "Radeon RX 580", "vram": "8 ГБ", "gpu_vendor": "AMD",
            "purpose": "Для офиса и дома", "memory_bus": "256 бит", "interface": "PCIe 3.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR5", "gpu_series": "AMD Radeon RX 500/400",
            "color": "Красный", "length": "250–299 мм"
        }
    },
    {
        "title": "NVIDIA GeForce RTX 3050 6GB",
        "price": 16990, "brand": "NVIDIA",
        "info": "Entry-level карта с поддержкой DLSS.",
        "specs": {
            "gpu_model": "GeForce RTX 3050", "vram": "6 ГБ", "gpu_vendor": "NVIDIA",
            "purpose": "Для офиса и дома", "memory_bus": "96 бит", "interface": "PCIe 3.0 x16",
            "cooling": "1 осевой", "memory_type": "GDDR6", "gpu_series": "NVIDIA GeForce RTX 30",
            "color": "Черный", "length": "150–199 мм"
        }
    },
    {
        "title": "Intel Arc A310 4GB",
        "price": 9990, "brand": "Intel",
        "info": "Компактная карта для офисных ПК и мультимедиа.",
        "specs": {
            "gpu_model": "Intel Arc A310", "vram": "4 ГБ", "gpu_vendor": "Intel",
            "purpose": "Для офиса и дома", "memory_bus": "64 бит", "interface": "PCIe 4.0 x16",
            "cooling": "1 осевой", "memory_type": "GDDR6", "gpu_series": "Intel Arc A500/A300",
            "color": "Зелёный", "length": "150–199 мм"
        }
    },
    {
        "title": "NVIDIA GeForce GTX 1050 Ti",
        "price": 11990, "brand": "NVIDIA",
        "info": "Надежная карта для старых игр и работы без доп. питания.",
        "specs": {
            "gpu_model": "GeForce GTX 1050 Ti", "vram": "4 ГБ", "gpu_vendor": "NVIDIA",
            "purpose": "Для офиса и дома", "memory_bus": "128 бит", "interface": "PCIe 3.0 x16",
            "cooling": "2 осевых", "memory_type": "GDDR5", "gpu_series": "NVIDIA GeForce GTX 10",
            "color": "Черный", "length": "150–199 мм"
        }
    },
]

def seed_gpus():
    print("🚀 Начинаю создание 20 реалистичных видеокарт...")
    created_count = 0

    for item in REALISTIC_GPUS:
        if Product.objects.filter(title=item["title"]).exists():
            print(f" Пропуск: {item['title']} уже существует")
            continue

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(3, 45),
            warranty="24 месяца"
        )
        p.categories.add(gpu_cat)
        created_count += 1
        print(f"✅ Создано: {p.title} | Цена: {p.price} ₽")

    print(f"\n🎉 Готово! Добавлено {created_count} новых видеокарт.")

if __name__ == '__main__':
    seed_gpus()