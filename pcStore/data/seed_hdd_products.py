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

# Получаем или создаем категории
hdd_cat, _ = Category.objects.get_or_create(title='Жесткие диски (HDD)', slug='hdd')
hdd_35_cat, _ = Category.objects.get_or_create(title='HDD 3.5"', slug='hdd-35', parent=hdd_cat)
hdd_25_cat, _ = Category.objects.get_or_create(title='HDD 2.5"', slug='hdd-25', parent=hdd_cat)

# ==========================================
# HDD 3.5" (10 товаров)
# ==========================================
REALISTIC_HDD_35 = [
    # === DESKTOP (Настольные ПК) ===
    {
        "title": "Western Digital WD Blue 1TB (WD10EZEX)",
        "price": 4990, "brand": "Western Digital",
        "info": "Классический настольный жесткий диск для повседневных задач и хранения данных.",
        "specs": {
            "capacity": 1.0,
            "purpose": "Для настольных ПК (Desktop)",
            "rpm": "5400 RPM",
            "recording_technology": "CMR (Conventional Magnetic Recording)",
            "cache_size": "64 МБ",
            "raid_optimized": "Нет (стандартный режим)",
            "helium_filled": "Нет (воздушный корпус)",
            "load_unload_cycles": 600000,
            "noise_level": 25,
            "thickness": 26
        }
    },
    {
        "title": "Seagate Barracuda 2TB (ST2000DM008)",
        "price": 6490, "brand": "Seagate",
        "info": "Популярный накопитель для домашних ПК с высокой емкостью и низкой ценой за гигабайт.",
        "specs": {
            "capacity": 2.0,
            "purpose": "Для настольных ПК (Desktop)",
            "rpm": "5400 RPM",
            "recording_technology": "SMR (Shingled Magnetic Recording)",
            "cache_size": "256 МБ",
            "raid_optimized": "Нет (стандартный режим)",
            "helium_filled": "Нет (воздушный корпус)",
            "load_unload_cycles": 300000,
            "noise_level": 26,
            "thickness": 26
        }
    },
    {
        "title": "Seagate Barracuda Compute 4TB (ST4000DM004)",
        "price": 8990, "brand": "Seagate",
        "info": "4-терабайтный накопитель для хранения медиафайлов и архивов.",
        "specs": {
            "capacity": 4.0,
            "purpose": "Для настольных ПК (Desktop)",
            "rpm": "5400 RPM",
            "recording_technology": "SMR (Shingled Magnetic Recording)",
            "cache_size": "256 МБ",
            "raid_optimized": "Нет (стандартный режим)",
            "helium_filled": "Нет (воздушный корпус)",
            "load_unload_cycles": 300000,
            "noise_level": 28,
            "thickness": 26
        }
    },

    # === NAS (Сетевые хранилища) ===
    {
        "title": "Western Digital WD Red Plus 4TB (WD40EFRX)",
        "price": 12990, "brand": "Western Digital",
        "info": "Специализированный диск для NAS с технологией CMR и поддержкой RAID.",
        "specs": {
            "capacity": 4.0,
            "purpose": "Для NAS (сетевых хранилищ)",
            "rpm": "5400 RPM",
            "recording_technology": "CMR (Conventional Magnetic Recording)",
            "cache_size": "256 МБ",
            "raid_optimized": "Есть (поддержка TLER / ERC / CCTL)",
            "helium_filled": "Нет (воздушный корпус)",
            "load_unload_cycles": 600000,
            "noise_level": 27,
            "thickness": 26
        }
    },
    {
        "title": "Seagate IronWolf 8TB (ST8000VN004)",
        "price": 21990, "brand": "Seagate",
        "info": "Надежный диск для домашних и офисных NAS с технологией AgileArray.",
        "specs": {
            "capacity": 8.0,
            "purpose": "Для NAS (сетевых хранилищ)",
            "rpm": "7200 RPM",
            "recording_technology": "CMR (Conventional Magnetic Recording)",
            "cache_size": "256 МБ",
            "raid_optimized": "Есть (поддержка TLER / ERC / CCTL)",
            "helium_filled": "Да (гелиевый корпус)",
            "load_unload_cycles": 600000,
            "noise_level": 28,
            "thickness": 26
        }
    },

    # === ENTERPRISE (Серверы) ===
    {
        "title": "Western Digital WD Gold 14TB (WD141KRYZ)",
        "price": 39990, "brand": "Western Digital",
        "info": "Серверный накопитель с максимальной надежностью и нагрузкой до 550 ТБ/год.",
        "specs": {
            "capacity": 14.0,
            "purpose": "Для серверов (Enterprise / Data Center)",
            "rpm": "7200 RPM",
            "recording_technology": "CMR (Conventional Magnetic Recording)",
            "cache_size": "512 МБ",
            "raid_optimized": "Есть (поддержка TLER / ERC / CCTL)",
            "helium_filled": "Да (гелиевый корпус)",
            "load_unload_cycles": 600000,
            "noise_level": 36,
            "thickness": 26
        }
    },
    {
        "title": "Seagate Exos X18 16TB (ST16000NM000J)",
        "price": 44990, "brand": "Seagate",
        "info": "Флагманский серверный диск с нагрузкой до 550 ТБ/год и MTBF 2.5 млн часов.",
        "specs": {
            "capacity": 16.0,
            "purpose": "Для серверов (Enterprise / Data Center)",
            "rpm": "7200 RPM",
            "recording_technology": "CMR (Conventional Magnetic Recording)",
            "cache_size": "256 МБ",
            "raid_optimized": "Есть (поддержка TLER / ERC / CCTL)",
            "helium_filled": "Да (гелиевый корпус)",
            "load_unload_cycles": 600000,
            "noise_level": 38,
            "thickness": 26
        }
    },

    # === SURVEILLANCE (Видеонаблюдение) ===
    {
        "title": "Western Digital WD Purple 4TB (WD42PURZ)",
        "price": 11990, "brand": "Western Digital",
        "info": "Диск для систем видеонаблюдения с поддержкой до 64 камер и технологией AllFrame.",
        "specs": {
            "capacity": 4.0,
            "purpose": "Для видеонаблюдения (Surveillance)",
            "rpm": "5400 RPM",
            "recording_technology": "CMR (Conventional Magnetic Recording)",
            "cache_size": "64 МБ",
            "raid_optimized": "Нет (стандартный режим)",
            "helium_filled": "Нет (воздушный корпус)",
            "load_unload_cycles": 300000,
            "noise_level": 25,
            "thickness": 26
        }
    },
    {
        "title": "Seagate SkyHawk 6TB (ST6000VX001)",
        "price": 16990, "brand": "Seagate",
        "info": "Накопитель для NVR с оптимизацией под запись видео 24/7.",
        "specs": {
            "capacity": 6.0,
            "purpose": "Для видеонаблюдения (Surveillance)",
            "rpm": "5900 RPM",
            "recording_technology": "CMR (Conventional Magnetic Recording)",
            "cache_size": "256 МБ",
            "raid_optimized": "Нет (стандартный режим)",
            "helium_filled": "Нет (воздушный корпус)",
            "load_unload_cycles": 300000,
            "noise_level": 28,
            "thickness": 26
        }
    },

    # === MAXIMUM CAPACITY (HAMR) ===
    {
        "title": "Seagate IronWolf Pro 24TB (ST24000NE001)",
        "price": 64990, "brand": "Seagate",
        "info": "Новейший диск для NAS с технологией HAMR и рекордной емкостью.",
        "specs": {
            "capacity": 24.0,
            "purpose": "Для NAS (сетевых хранилищ)",
            "rpm": "7200 RPM",
            "recording_technology": "HAMR (Heat-Assisted Magnetic Recording)",
            "cache_size": "512 МБ",
            "raid_optimized": "Есть (поддержка TLER / ERC / CCTL)",
            "helium_filled": "Да (гелиевый корпус)",
            "load_unload_cycles": 600000,
            "noise_level": 32,
            "thickness": 26
        }
    }
]

# ==========================================
# HDD 2.5" (8 товаров)
# ==========================================
REALISTIC_HDD_25 = [
    # === LAPTOP (Ноутбуки) ===
    {
        "title": "Western Digital WD Blue 1TB (WD10SPZX)",
        "price": 5490, "brand": "Western Digital",
        "info": "Стандартный ноутбучный жесткий диск толщиной 7 мм для ультрабуков и ноутбуков.",
        "specs": {
            "capacity": 1.0,
            "interface": "SATA III (6 Гбит/с)",
            "rpm": "5400 RPM",
            "recording_technology": "SMR (Shingled Magnetic Recording)",
            "cache_size": "128 МБ",
            "thickness": "7 мм (стандартный для ноутбуков)",
            "noise_level_active": 24,
            "data_transfer_rate": 120,
            "noise_level_idle": 21,
            "load_unload_cycles": 600000
        }
    },
    {
        "title": "Seagate BarraCuda 2TB (ST2000LM015)",
        "price": 6990, "brand": "Seagate",
        "info": "Тонкий накопитель для ноутбуков с высокой емкостью и низким энергопотреблением.",
        "specs": {
            "capacity": 2.0,
            "interface": "SATA III (6 Гбит/с)",
            "rpm": "5400 RPM",
            "recording_technology": "SMR (Shingled Magnetic Recording)",
            "cache_size": "128 МБ",
            "thickness": "15 мм (серверный/enterprise)",  # На самом деле это thin, но по конфигу 15мм макс
            "noise_level_active": 25,
            "data_transfer_rate": 140,
            "noise_level_idle": 22,
            "load_unload_cycles": 300000
        }
    },
    {
        "title": "Toshiba MQ04ABF100 1TB",
        "price": 4990, "brand": "Toshiba",
        "info": "Компактный и надежный диск для ноутбуков с улучшенной защитой от ударов.",
        "specs": {
            "capacity": 1.0,
            "interface": "SATA III (6 Гбит/с)",
            "rpm": "5400 RPM",
            "recording_technology": "SMR (Shingled Magnetic Recording)",
            "cache_size": "128 МБ",
            "thickness": "7 мм (стандартный для ноутбуков)",
            "noise_level_active": 23,
            "data_transfer_rate": 115,
            "noise_level_idle": 20,
            "load_unload_cycles": 300000
        }
    },

    # === HIGH PERFORMANCE 2.5" ===
    {
        "title": "Western Digital WD Black 1TB (WD10JPLX)",
        "price": 8990, "brand": "Western Digital",
        "info": "Производительный 2.5\" диск с 7200 об/мин для игровых ноутбуков и портативных рабочих станций.",
        "specs": {
            "capacity": 1.0,
            "interface": "SATA III (6 Гбит/с)",
            "rpm": "7200 RPM",
            "recording_technology": "PMR (Perpendicular Magnetic Recording)",
            "cache_size": "32 МБ",
            "thickness": "9.5 мм (стандартный)",
            "noise_level_active": 28,
            "data_transfer_rate": 160,
            "noise_level_idle": 24,
            "load_unload_cycles": 300000
        }
    },

    # === PORTABLE / EXTERNAL ===
    {
        "title": "Seagate Backup Plus Slim 2TB (Portable)",
        "price": 7490, "brand": "Seagate",
        "info": "Внешний портативный накопитель с USB 3.0 для резервного копирования.",
        "specs": {
            "capacity": 2.0,
            "interface": "USB 3.0 (внешний)",
            "rpm": "5400 RPM",
            "recording_technology": "SMR (Shingled Magnetic Recording)",
            "cache_size": "128 МБ",
            "thickness": "9.5 мм (стандартный)",
            "noise_level_active": 24,
            "data_transfer_rate": 120,
            "noise_level_idle": 21,
            "load_unload_cycles": 300000
        }
    },
    {
        "title": "Western Digital My Passport 4TB",
        "price": 10990, "brand": "Western Digital",
        "info": "Компактный внешний накопитель с аппаратным шифрованием AES-256.",
        "specs": {
            "capacity": 4.0,
            "interface": "USB 3.1 (внешний)",
            "rpm": "5400 RPM",
            "recording_technology": "SMR (Shingled Magnetic Recording)",
            "cache_size": "128 МБ",
            "thickness": "12.5 мм (увеличенный)",
            "noise_level_active": 25,
            "data_transfer_rate": 140,
            "noise_level_idle": 22,
            "load_unload_cycles": 300000
        }
    },

    # === ENTERPRISE / SERVER 2.5" ===
    {
        "title": "Seagate Exos 7E2000 2TB (ST2000NX0253)",
        "price": 18990, "brand": "Seagate",
        "info": "Серверный 2.5\" накопитель с SAS интерфейсом для стоек 2U и blade-систем.",
        "specs": {
            "capacity": 2.0,
            "interface": "SAS 12 Гбит/с",
            "rpm": "7200 RPM",
            "recording_technology": "CMR (Conventional Magnetic Recording)",
            "cache_size": "128 МБ",
            "thickness": "15 мм (серверный/enterprise)",
            "noise_level_active": 28,
            "data_transfer_rate": 250,
            "noise_level_idle": 24,
            "load_unload_cycles": 600000
        }
    },
    {
        "title": "Western Digital Ultrastar DC HC560 2.5\" 2TB",
        "price": 22990, "brand": "Western Digital",
        "info": "Корпоративный накопитель для дата-центров с MTBF 2.5 млн часов.",
        "specs": {
            "capacity": 2.0,
            "interface": "SAS 12 Гбит/с",
            "rpm": "10000 RPM",
            "recording_technology": "CMR (Conventional Magnetic Recording)",
            "cache_size": "256 МБ",
            "thickness": "15 мм (серверный/enterprise)",
            "noise_level_active": 32,
            "data_transfer_rate": 280,
            "noise_level_idle": 26,
            "load_unload_cycles": 600000
        }
    }
]


def seed_hdds():
    print(" Начинаю создание реалистичных жестких дисков (HDD)...")

    # === HDD 3.5" ===
    print("\n=== HDD 3.5\" ===")
    created_35 = 0
    for item in REALISTIC_HDD_35:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"⏭️  Пропуск: {item['title']} уже существует")
            continue

        warranty_map = {
            "Western Digital": "24 месяца" if "Blue" in item["title"] else "60 месяцев",
            "Seagate": "24 месяца" if "Barracuda" in item["title"] else "60 месяцев",
            "Toshiba": "24 месяца",
        }

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(5, 50),
            warranty=warranty_map.get(item["brand"], "24 месяца")
        )
        p.categories.add(hdd_35_cat)
        created_35 += 1
        print(f"✅ {p.title} | {item['specs']['capacity']}TB | {item['specs']['rpm']} | {item['price']} ₽")

    print(f"\n HDD 3.5\": добавлено {created_35}")

    # === HDD 2.5" ===
    print("\n=== HDD 2.5\" ===")
    created_25 = 0
    for item in REALISTIC_HDD_25:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"⏭️  Пропуск: {item['title']} уже существует")
            continue

        warranty_map = {
            "Western Digital": "24 месяца" if "Blue" in item["title"] else "60 месяцев",
            "Seagate": "24 месяца" if "BarraCuda" in item["title"] or "Backup" in item["title"] else "60 месяцев",
            "Toshiba": "24 месяца",
        }

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(5, 60),
            warranty=warranty_map.get(item["brand"], "24 месяца")
        )
        p.categories.add(hdd_25_cat)
        created_25 += 1
        print(f"✅ {p.title} | {item['specs']['capacity']}TB | {item['specs']['interface']} | {item['price']} ₽")

    print(f"\n🎉 HDD 2.5\": добавлено {created_25}")
    print(f"\n{'=' * 50}")
    print(f"🏆 ИТОГО: HDD 3.5\"={created_35}, HDD 2.5\"={created_25}")
    print(f"🏆 ВСЕГО: {created_35 + created_25} жестких дисков")


if __name__ == '__main__':
    seed_hdds()