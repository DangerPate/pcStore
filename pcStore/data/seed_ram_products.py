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

ram_cat, _ = Category.objects.get_or_create(title='Оперативная память', slug='ram')

REALISTIC_RAM = [
    # === DDR5 HIGH-END ===
    {
        "title": "Kingston FURY Renegade 32GB (2x16GB) DDR5 7200MHz CL36",
        "price": 18990, "brand": "Kingston",
        "info": "Топовый комплект DDR5 для экстремального гейминга и разгона.",
        "specs": {
            "memory_type": "DDR5",
            "total_capacity": "32 ГБ",
            "module_capacity": "16 ГБ",
            "frequency": "7200",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 36,
            "heatsink": "Есть"
        }
    },
    {
        "title": "Corsair Dominator Platinum RGB 32GB (2x16GB) DDR5 6400MHz CL32",
        "price": 21990, "brand": "Corsair",
        "info": "Премиальный комплект с RGB подсветкой и запатентованной технологией рассеивания тепла.",
        "specs": {
            "memory_type": "DDR5",
            "total_capacity": "32 ГБ",
            "module_capacity": "16 ГБ",
            "frequency": "6400",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 32,
            "heatsink": "Есть"
        }
    },
    {
        "title": "G.Skill Trident Z5 RGB 64GB (2x32GB) DDR5 6000MHz CL30",
        "price": 26990, "brand": "G.Skill",
        "info": "Флагманский комплект для рабочих станций и энтузиастов.",
        "specs": {
            "memory_type": "DDR5",
            "total_capacity": "64 ГБ",
            "module_capacity": "32 ГБ",
            "frequency": "6000",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 30,
            "heatsink": "Есть"
        }
    },
    {
        "title": "TeamGroup T-Force Delta RGB 32GB (2x16GB) DDR5 6000MHz CL30",
        "price": 14990, "brand": "TeamGroup",
        "info": "Оптимальный баланс цены и производительности для игровых систем.",
        "specs": {
            "memory_type": "DDR5",
            "total_capacity": "32 ГБ",
            "module_capacity": "16 ГБ",
            "frequency": "6000",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 30,
            "heatsink": "Есть"
        }
    },
    {
        "title": "Crucial Pro 32GB (2x16GB) DDR5 5600MHz CL36",
        "price": 11990, "brand": "Crucial",
        "info": "Надежная память от производителя Micron для стабильной работы.",
        "specs": {
            "memory_type": "DDR5",
            "total_capacity": "32 ГБ",
            "module_capacity": "16 ГБ",
            "frequency": "5600",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 36,
            "heatsink": "Есть"
        }
    },

    # === DDR4 HIGH-END ===
    {
        "title": "G.Skill Trident Z RGB 32GB (2x16GB) DDR4 3600MHz CL16",
        "price": 12990, "brand": "G.Skill",
        "info": "Легендарный комплект с RGB подсветкой для AM4 и LGA1200.",
        "specs": {
            "memory_type": "DDR4",
            "total_capacity": "32 ГБ",
            "module_capacity": "16 ГБ",
            "frequency": "3600",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 16,
            "heatsink": "Есть"
        }
    },
    {
        "title": "Corsair Vengeance LPX 32GB (2x16GB) DDR4 3600MHz CL18",
        "price": 10990, "brand": "Corsair",
        "info": "Компактный низкопрофильный комплект для совместимости с кулерами.",
        "specs": {
            "memory_type": "DDR4",
            "total_capacity": "32 ГБ",
            "module_capacity": "16 ГБ",
            "frequency": "3600",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 18,
            "heatsink": "Есть"
        }
    },
    {
        "title": "Kingston FURY Beast 16GB (2x8GB) DDR4 3200MHz CL16",
        "price": 5490, "brand": "Kingston",
        "info": "Народный выбор для игровых ПК на платформах DDR4.",
        "specs": {
            "memory_type": "DDR4",
            "total_capacity": "16 ГБ",
            "module_capacity": "8 ГБ",
            "frequency": "3200",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 16,
            "heatsink": "Есть"
        }
    },
    {
        "title": "Crucial Ballistix 32GB (2x16GB) DDR4 3600MHz CL16",
        "price": 11490, "brand": "Crucial",
        "info": "Игровая память с алюминиевым радиатором и отличным разгонным потенциалом.",
        "specs": {
            "memory_type": "DDR4",
            "total_capacity": "32 ГБ",
            "module_capacity": "16 ГБ",
            "frequency": "3600",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 16,
            "heatsink": "Есть"
        }
    },
    {
        "title": "ADATA XPG Spectrix D41 16GB (2x8GB) DDR4 3200MHz CL16",
        "price": 6490, "brand": "ADATA",
        "info": "Память с RGB подсветкой по доступной цене.",
        "specs": {
            "memory_type": "DDR4",
            "total_capacity": "16 ГБ",
            "module_capacity": "8 ГБ",
            "frequency": "3200",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 16,
            "heatsink": "Есть"
        }
    },

    # === DDR4 BUDGET ===
    {
        "title": "Kingston FURY Beast 16GB (2x8GB) DDR4 2666MHz CL16",
        "price": 4490, "brand": "Kingston",
        "info": "Базовый комплект для офисных и домашних ПК.",
        "specs": {
            "memory_type": "DDR4",
            "total_capacity": "16 ГБ",
            "module_capacity": "8 ГБ",
            "frequency": "2666",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 16,
            "heatsink": "Нет"
        }
    },
    {
        "title": "Samsung DDR4 16GB (2x8GB) 3200MHz CL22",
        "price": 4990, "brand": "Samsung",
        "info": "Оригинальная память Samsung без радиатора для стабильной работы.",
        "specs": {
            "memory_type": "DDR4",
            "total_capacity": "16 ГБ",
            "module_capacity": "8 ГБ",
            "frequency": "3200",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 22,
            "heatsink": "Нет"
        }
    },
    {
        "title": "Crucial DDR4 8GB 2666MHz CL19",
        "price": 1990, "brand": "Crucial",
        "info": "Одиночный модуль для апгрейда офисных ПК.",
        "specs": {
            "memory_type": "DDR4",
            "total_capacity": "8 ГБ",
            "module_capacity": "8 ГБ",
            "frequency": "2666",
            "kit_size": "1",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 19,
            "heatsink": "Нет"
        }
    },

    # === DDR3 LEGACY ===
    {
        "title": "Kingston HyperX Fury 8GB (2x4GB) DDR3 1600MHz CL10",
        "price": 2990, "brand": "Kingston",
        "info": "Классический комплект для старых платформ LGA1155 и AM3+.",
        "specs": {
            "memory_type": "DDR3",
            "total_capacity": "8 ГБ",
            "module_capacity": "4 ГБ",
            "frequency": "1600",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 10,
            "heatsink": "Есть"
        }
    },
    {
        "title": "Corsair Vengeance 16GB (2x8GB) DDR3 1866MHz CL9",
        "price": 4490, "brand": "Corsair",
        "info": "Топовый комплект DDR3 для энтузиастов старых платформ.",
        "specs": {
            "memory_type": "DDR3",
            "total_capacity": "16 ГБ",
            "module_capacity": "8 ГБ",
            "frequency": "1866",
            "kit_size": "2",
            "ram_purpose": "Desktop (UDIMM)",
            "cas_latency": 9,
            "heatsink": "Есть"
        }
    },

    # === SODIMM LAPTOP ===
    {
        "title": "Kingston FURY Impact 32GB (2x16GB) DDR5 5600MHz SODIMM CL36",
        "price": 14990, "brand": "Kingston",
        "info": "Игровая память для ноутбуков и мини-ПК нового поколения.",
        "specs": {
            "memory_type": "SODIMM DDR5",
            "total_capacity": "32 ГБ",
            "module_capacity": "16 ГБ",
            "frequency": "5600",
            "kit_size": "2",
            "ram_purpose": "Laptop (SODIMM)",
            "cas_latency": 36,
            "heatsink": "Нет"
        }
    },
    {
        "title": "Crucial 16GB (2x8GB) DDR4 3200MHz SODIMM CL22",
        "price": 4990, "brand": "Crucial",
        "info": "Надежная память для апгрейда ноутбуков и неттопов.",
        "specs": {
            "memory_type": "SODIMM DDR4",
            "total_capacity": "16 ГБ",
            "module_capacity": "8 ГБ",
            "frequency": "3200",
            "kit_size": "2",
            "ram_purpose": "Laptop (SODIMM)",
            "cas_latency": 22,
            "heatsink": "Нет"
        }
    },
    {
        "title": "Samsung 16GB DDR4 3200MHz SODIMM",
        "price": 3490, "brand": "Samsung",
        "info": "Оригинальная память Samsung для ноутбуков.",
        "specs": {
            "memory_type": "SODIMM DDR4",
            "total_capacity": "16 ГБ",
            "module_capacity": "16 ГБ",
            "frequency": "3200",
            "kit_size": "1",
            "ram_purpose": "Laptop (SODIMM)",
            "cas_latency": 22,
            "heatsink": "Нет"
        }
    },
    {
        "title": "Kingston 8GB DDR3L 1600MHz SODIMM",
        "price": 1990, "brand": "Kingston",
        "info": "Модуль для старых ноутбуков с низким энергопотреблением.",
        "specs": {
            "memory_type": "SODIMM DDR3",
            "total_capacity": "8 ГБ",
            "module_capacity": "8 ГБ",
            "frequency": "1600",
            "kit_size": "1",
            "ram_purpose": "Laptop (SODIMM)",
            "cas_latency": 11,
            "heatsink": "Нет"
        }
    },

    # === SERVER ECC ===
    {
        "title": "Kingston Server Premier 64GB (2x32GB) DDR4 3200MHz ECC RDIMM",
        "price": 34990, "brand": "Kingston",
        "info": "Серверная память с коррекцией ошибок для рабочих станций.",
        "specs": {
            "memory_type": "DDR4 ECC",
            "total_capacity": "64 ГБ",
            "module_capacity": "32 ГБ",
            "frequency": "3200",
            "kit_size": "2",
            "ram_purpose": "Server (RDIMM/LRDIMM)",
            "cas_latency": 22,
            "heatsink": "Нет"
        }
    },
    {
        "title": "Samsung 32GB DDR5 4800MHz ECC RDIMM",
        "price": 24990, "brand": "Samsung",
        "info": "Оригинальная серверная память DDR5 для платформ EPYC и Xeon.",
        "specs": {
            "memory_type": "DDR5 ECC",
            "total_capacity": "32 ГБ",
            "module_capacity": "32 ГБ",
            "frequency": "4800",
            "kit_size": "1",
            "ram_purpose": "Server (RDIMM/LRDIMM)",
            "cas_latency": 40,
            "heatsink": "Нет"
        }
    },
    {
        "title": "Kingston 128GB (4x32GB) DDR4 2933MHz ECC RDIMM",
        "price": 89990, "brand": "Kingston",
        "info": "Максимальный объем для профессиональных серверов и виртуализации.",
        "specs": {
            "memory_type": "DDR4 ECC",
            "total_capacity": "128 ГБ",
            "module_capacity": "32 ГБ",
            "frequency": "2933",
            "kit_size": "4",
            "ram_purpose": "Server (RDIMM/LRDIMM)",
            "cas_latency": 21,
            "heatsink": "Нет"
        }
    },
]

def seed_ram():
    print("🚀 Начинаю создание комплектов оперативной памяти...")
    created_count = 0

    for item in REALISTIC_RAM:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"⏭️  Пропуск: {item['title']} уже существует")
            continue

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(5, 80),
            warranty="Пожизненная гарантия" if item["brand"] in ["Kingston", "Crucial", "Corsair", "G.Skill"] else "24 месяца"
        )
        p.categories.add(ram_cat)
        created_count += 1
        print(f"✅ Создано: {p.title} | Цена: {p.price} ₽ | {item['specs']['total_capacity']} @ {item['specs']['frequency']}МГц")

    print(f"\n🎉 Готово! Добавлено {created_count} новых комплектов RAM.")

if __name__ == '__main__':
    seed_ram()