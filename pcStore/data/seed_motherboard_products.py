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

mb_cat, _ = Category.objects.get_or_create(title='Материнские платы', slug='motherboard')

REALISTIC_MOTHERBOARDS = [
    # === INTEL Z890 (LGA1851) — НОВЕЙШИЕ ===
    {
        "title": "ASUS ROG MAXIMUS Z890 HERO",
        "price": 64990, "brand": "ASUS",
        "info": "Флагманская плата для процессоров Intel Core Ultra 200S с расширенными возможностями разгона.",
        "specs": {
            "socket": "LGA1851", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "Intel Z890", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "Intel", "m2_slots": "5", "wifi_std": "Wi-Fi 7 (802.11be)"
        }
    },
    {
        "title": "MSI MEG Z890 ACE",
        "price": 72990, "brand": "MSI",
        "info": "Премиальная плата для экстремального разгона с усиленной системой питания.",
        "specs": {
            "socket": "LGA1851", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "Intel Z890", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "Intel", "m2_slots": "5", "wifi_std": "Wi-Fi 7 (802.11be)"
        }
    },
    {
        "title": "Gigabyte Z890 AORUS MASTER",
        "price": 59990, "brand": "Gigabyte",
        "info": "Топовая плата AORUS с массивным радиатором VRM и поддержкой DDR5-8000+.",
        "specs": {
            "socket": "LGA1851", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "Intel Z890", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "Intel", "m2_slots": "4", "wifi_std": "Wi-Fi 7 (802.11be)"
        }
    },
    {
        "title": "ASUS ROG STRIX Z890-E GAMING WIFI",
        "price": 49990, "brand": "ASUS",
        "info": "Оптимальный баланс для игровых систем на базе Intel Core Ultra 200S.",
        "specs": {
            "socket": "LGA1851", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "Intel Z890", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "Intel", "m2_slots": "4", "wifi_std": "Wi-Fi 7 (802.11be)"
        }
    },

    # === INTEL Z790/B760 (LGA1700) ===
    {
        "title": "ASUS ROG MAXIMUS Z790 HERO",
        "price": 54990, "brand": "ASUS",
        "info": "Легендарная плата для процессоров Intel 13-14 поколений с расширенным охлаждением VRM.",
        "specs": {
            "socket": "LGA1700", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "Intel Z790", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "Intel", "m2_slots": "5", "wifi_std": "Wi-Fi 6E"
        }
    },
    {
        "title": "MSI MPG Z790 CARBON WIFI",
        "price": 42990, "brand": "MSI",
        "info": "Игровая плата Carbon с отличной системой питания и RGB подсветкой.",
        "specs": {
            "socket": "LGA1700", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "Intel Z790", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "Intel", "m2_slots": "4", "wifi_std": "Wi-Fi 6E"
        }
    },
    {
        "title": "Gigabyte Z790 AORUS ELITE AX",
        "price": 29990, "brand": "Gigabyte",
        "info": "Популярный выбор для игровых ПК среднего уровня на платформе LGA1700.",
        "specs": {
            "socket": "LGA1700", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "Intel Z790", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "Intel", "m2_slots": "4", "wifi_std": "Wi-Fi 6 (802.11ax)"
        }
    },
    {
        "title": "MSI MAG B760 TOMAHAWK WIFI",
        "price": 24990, "brand": "MSI",
        "info": "Надежная плата среднего сегмента для сборки игрового ПК.",
        "specs": {
            "socket": "LGA1700", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "Intel B760", "pcie_version": "PCIe 4.0", "ram_slots": "4",
            "cpu_support": "Intel", "m2_slots": "3", "wifi_std": "Wi-Fi 6E"
        }
    },
    {
        "title": "ASUS ROG STRIX B760-G GAMING WIFI",
        "price": 22990, "brand": "ASUS",
        "info": "Компактная плата формата mATX для компактных игровых сборок.",
        "specs": {
            "socket": "LGA1700", "memory_type": "DDR5", "form_factor": "Micro-ATX (mATX)",
            "chipset": "Intel B760", "pcie_version": "PCIe 4.0", "ram_slots": "4",
            "cpu_support": "Intel", "m2_slots": "2", "wifi_std": "Wi-Fi 6E"
        }
    },

    # === INTEL B860 (LGA1851) — СРЕДНИЙ СЕГМЕНТ ===
    {
        "title": "MSI MAG B860 TOMAHAWK MAX WIFI",
        "price": 27990, "brand": "MSI",
        "info": "Плата среднего сегмента для платформы LGA1851 с поддержкой Wi-Fi 7.",
        "specs": {
            "socket": "LGA1851", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "Intel B860", "pcie_version": "PCIe 4.0", "ram_slots": "4",
            "cpu_support": "Intel", "m2_slots": "3", "wifi_std": "Wi-Fi 7 (802.11be)"
        }
    },

    # === INTEL WORKSTATION W790 (LGA4677) ===
    {
        "title": "ASUS Pro WS W790-ACE",
        "price": 89990, "brand": "ASUS",
        "info": "Профессиональная плата для рабочих станций Intel Xeon W-2400/3400.",
        "specs": {
            "socket": "LGA4677", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "Intel W790", "pcie_version": "PCIe 5.0", "ram_slots": "8",
            "cpu_support": "Intel", "m2_slots": "4", "wifi_std": "Нет Wi-Fi"
        }
    },

    # === AMD X870E/AM5 — НОВЕЙШИЕ ===
    {
        "title": "ASUS ROG CROSSHAIR X870E HERO",
        "price": 69990, "brand": "ASUS",
        "info": "Флагманская плата для процессоров AMD Ryzen 9000 с максимальной производительностью.",
        "specs": {
            "socket": "AM5", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "AMD X870E", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "AMD", "m2_slots": "5", "wifi_std": "Wi-Fi 7 (802.11be)"
        }
    },
    {
        "title": "MSI MEG X870E GODLIKE",
        "price": 94990, "brand": "MSI",
        "info": "Ультра-премиальная плата с встроенным дисплеем и системой охлаждения.",
        "specs": {
            "socket": "AM5", "memory_type": "DDR5", "form_factor": "E-ATX",
            "chipset": "AMD X870E", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "AMD", "m2_slots": "5", "wifi_std": "Wi-Fi 7 (802.11be)"
        }
    },
    {
        "title": "Gigabyte X870E AORUS MASTER",
        "price": 54990, "brand": "Gigabyte",
        "info": "Топовая плата AORUS для энтузиастов платформы AM5.",
        "specs": {
            "socket": "AM5", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "AMD X870E", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "AMD", "m2_slots": "4", "wifi_std": "Wi-Fi 7 (802.11be)"
        }
    },
    {
        "title": "ASUS ROG STRIX B650E-F GAMING WIFI",
        "price": 29990, "brand": "ASUS",
        "info": "Оптимальная плата для игровых систем на базе Ryzen 7000/9000.",
        "specs": {
            "socket": "AM5", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "AMD B650E", "pcie_version": "PCIe 5.0", "ram_slots": "4",
            "cpu_support": "AMD", "m2_slots": "3", "wifi_std": "Wi-Fi 6E"
        }
    },
    {
        "title": "MSI MAG B650 TOMAHAWK WIFI",
        "price": 24990, "brand": "MSI",
        "info": "Народный выбор для игровых сборок на платформе AM5.",
        "specs": {
            "socket": "AM5", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "AMD B650", "pcie_version": "PCIe 4.0", "ram_slots": "4",
            "cpu_support": "AMD", "m2_slots": "3", "wifi_std": "Wi-Fi 6E"
        }
    },
    {
        "title": "Gigabyte B650 AORUS ELITE AX V2",
        "price": 19990, "brand": "Gigabyte",
        "info": "Доступная плата с хорошей системой питания для Ryzen 7000.",
        "specs": {
            "socket": "AM5", "memory_type": "DDR5", "form_factor": "ATX",
            "chipset": "AMD B650", "pcie_version": "PCIe 4.0", "ram_slots": "4",
            "cpu_support": "AMD", "m2_slots": "2", "wifi_std": "Wi-Fi 6 (802.11ax)"
        }
    },
    {
        "title": "ASUS ROG STRIX B650E-I GAMING WIFI",
        "price": 32990, "brand": "ASUS",
        "info": "Компактная плата Mini-ITX с поддержкой PCIe 5.0 для AM5.",
        "specs": {
            "socket": "AM5", "memory_type": "DDR5", "form_factor": "Mini-ITX",
            "chipset": "AMD B650E", "pcie_version": "PCIe 5.0", "ram_slots": "2",
            "cpu_support": "AMD", "m2_slots": "2", "wifi_std": "Wi-Fi 6E"
        }
    },

    # === AMD X570/B550 (AM4) ===
    {
        "title": "ASUS ROG CROSSHAIR VIII HERO (WI-FI)",
        "price": 34990, "brand": "ASUS",
        "info": "Легендарная плата для энтузиастов AM4 с поддержкой PCIe 4.0.",
        "specs": {
            "socket": "AM4", "memory_type": "DDR4", "form_factor": "ATX",
            "chipset": "AMD X570", "pcie_version": "PCIe 4.0", "ram_slots": "4",
            "cpu_support": "AMD", "m2_slots": "3", "wifi_std": "Wi-Fi 5 (802.11ac)"
        }
    },
    {
        "title": "MSI MPG B550 GAMING EDGE WIFI",
        "price": 18990, "brand": "MSI",
        "info": "Популярная плата для Ryzen 5000 с отличным балансом цены и возможностей.",
        "specs": {
            "socket": "AM4", "memory_type": "DDR4", "form_factor": "ATX",
            "chipset": "AMD B550", "pcie_version": "PCIe 4.0", "ram_slots": "4",
            "cpu_support": "AMD", "m2_slots": "2", "wifi_std": "Wi-Fi 6 (802.11ax)"
        }
    },
    {
        "title": "ASUS TUF GAMING B550-PLUS",
        "price": 16990, "brand": "ASUS",
        "info": "Надежная плата TUF Gaming для ежедневного использования с Ryzen 5000.",
        "specs": {
            "socket": "AM4", "memory_type": "DDR4", "form_factor": "ATX",
            "chipset": "AMD B550", "pcie_version": "PCIe 4.0", "ram_slots": "4",
            "cpu_support": "AMD", "m2_slots": "2", "wifi_std": "Нет Wi-Fi"
        }
    },
    {
        "title": "Gigabyte B550 AORUS PRO AC",
        "price": 17990, "brand": "Gigabyte",
        "info": "Плата с качественной системой питания и встроенным Wi-Fi/Bluetooth.",
        "specs": {
            "socket": "AM4", "memory_type": "DDR4", "form_factor": "ATX",
            "chipset": "AMD B550", "pcie_version": "PCIe 4.0", "ram_slots": "4",
            "cpu_support": "AMD", "m2_slots": "2", "wifi_std": "Wi-Fi 5 (802.11ac)"
        }
    },

    # === AMD THREADRIPPER (sTR5) ===
    {
        "title": "ASUS Pro WS TRX50E-SAGE SE",
        "price": 119990, "brand": "ASUS",
        "info": "Профессиональная плата для AMD Ryzen Threadripper 7000 серии.",
        "specs": {
            "socket": "TR5 (sTR5)", "memory_type": "DDR5", "form_factor": "E-ATX",
            "chipset": "AMD TRX50", "pcie_version": "PCIe 5.0", "ram_slots": "8",
            "cpu_support": "AMD", "m2_slots": "5", "wifi_std": "Wi-Fi 6E"
        }
    },

    # === AMD EPYC (SP5) ===
    {
        "title": "ASUS Pro WS WRX80E-SAGE SE WIFI",
        "price": 99990, "brand": "ASUS",
        "info": "Серверная плата для AMD EPYC 9004 с максимальной расширяемостью.",
        "specs": {
            "socket": "SP5", "memory_type": "DDR5", "form_factor": "E-ATX",
            "chipset": "AMD WRX80", "pcie_version": "PCIe 5.0", "ram_slots": "8",
            "cpu_support": "AMD", "m2_slots": "3", "wifi_std": "Wi-Fi 6E"
        }
    },

    # === MINI-ITX КОМПАКТНЫЕ ===
    {
        "title": "ASUS ROG STRIX B760-I GAMING WIFI",
        "price": 26990, "brand": "ASUS",
        "info": "Мощная плата Mini-ITX для компактных игровых ПК на LGA1700.",
        "specs": {
            "socket": "LGA1700", "memory_type": "DDR5", "form_factor": "Mini-ITX",
            "chipset": "Intel B760", "pcie_version": "PCIe 4.0", "ram_slots": "2",
            "cpu_support": "Intel", "m2_slots": "2", "wifi_std": "Wi-Fi 6E"
        }
    },
    {
        "title": "MSI MPG B650I EDGE WIFI",
        "price": 27990, "brand": "MSI",
        "info": "Компактная плата Mini-ITX для платформы AM5 с поддержкой DDR5.",
        "specs": {
            "socket": "AM5", "memory_type": "DDR5", "form_factor": "Mini-ITX",
            "chipset": "AMD B650", "pcie_version": "PCIe 4.0", "ram_slots": "2",
            "cpu_support": "AMD", "m2_slots": "2", "wifi_std": "Wi-Fi 6E"
        }
    },
]

def seed_motherboards():
    print("🚀 Начинаю создание реалистичных материнских плат...")
    created_count = 0

    for item in REALISTIC_MOTHERBOARDS:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"️  Пропуск: {item['title']} уже существует")
            continue

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(3, 30),
            warranty="36 месяцев"
        )
        p.categories.add(mb_cat)
        created_count += 1
        print(f"✅ Создано: {p.title} | Цена: {p.price} ₽ | Сокет: {item['specs']['socket']}")

    print(f"\n🎉 Готово! Добавлено {created_count} новых материнских плат.")

if __name__ == '__main__':
    seed_motherboards()