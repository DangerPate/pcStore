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
ssd_cat, _ = Category.objects.get_or_create(title='SSD накопители', slug='ssd')
ssd_25_cat, _ = Category.objects.get_or_create(title='SSD 2.5"', slug='ssd-25', parent=ssd_cat)
ssd_m2_cat, _ = Category.objects.get_or_create(title='SSD M.2', slug='ssd-m2', parent=ssd_cat)

# ==========================================
# SSD 2.5" (10 товаров)
# ==========================================
REALISTIC_SSD_25 = [
    # === БЮДЖЕТНЫЕ SATA ===
    {
        "title": "Kingston A400 240GB (SA400S37/240G)",
        "price": 2490, "brand": "Kingston",
        "info": "Бюджетный SSD для апгрейда старых ноутбуков и ПК. Надежный выбор для базовых задач.",
        "specs": {
            "capacity": 240,
            "interface": "SATA III (6 Гбит/с)",
            "tbw": 80,
            "dram_cache": "Нет (DRAM-less)",
            "read_speed": 500,
            "nand_type": "TLC (3 бита)",
            "write_speed": 350,
            "nand_structure": "3D NAND (96–128 слоев)",
            "dwpd": "Не указано (Потребительский)",
            "controller": "Silicon Motion SM2258 / SM2259"
        }
    },
    {
        "title": "Crucial BX500 480GB (CT480BX500SSD1)",
        "price": 3490, "brand": "Crucial",
        "info": "Популярный бюджетный SSD от Micron с хорошей надежностью и скоростью.",
        "specs": {
            "capacity": 480,
            "interface": "SATA III (6 Гбит/с)",
            "tbw": 120,
            "dram_cache": "Нет (DRAM-less)",
            "read_speed": 540,
            "nand_type": "TLC (3 бита)",
            "write_speed": 500,
            "nand_structure": "3D NAND (96–128 слоев)",
            "dwpd": "Не указано (Потребительский)",
            "controller": "Silicon Motion SM2258 / SM2259"
        }
    },
    {
        "title": "Western Digital WD Green 1TB (WDS100T3G0A)",
        "price": 5990, "brand": "Western Digital",
        "info": "Энергоэффективный SSD для повседневных задач с низким тепловыделением.",
        "specs": {
            "capacity": 1000,
            "interface": "SATA III (6 Гбит/с)",
            "tbw": 200,
            "dram_cache": "Нет (DRAM-less)",
            "read_speed": 545,
            "nand_type": "TLC (3 бита)",
            "write_speed": 465,
            "nand_structure": "3D NAND (96–128 слоев)",
            "dwpd": "Не указано (Потребительский)",
            "controller": "WD / SanDisk (собственный)"
        }
    },

    # === СРЕДНИЙ СЕГМЕНТ ===
    {
        "title": "Samsung 870 EVO 500GB (MZ-77E500B)",
        "price": 5490, "brand": "Samsung",
        "info": "Один из лучших SATA SSD с DRAM-буфером и высокой надежностью.",
        "specs": {
            "capacity": 500,
            "interface": "SATA III (6 Гбит/с)",
            "tbw": 300,
            "dram_cache": "Есть",
            "read_speed": 560,
            "nand_type": "TLC (3 бита)",
            "write_speed": 530,
            "nand_structure": "Samsung V-NAND (6-7 поколение)",
            "dwpd": "Не указано (Потребительский)",
            "controller": "Samsung MJX / MKX / MEX"
        }
    },
    {
        "title": "Crucial MX500 1TB (CT1000MX500SSD1)",
        "price": 7990, "brand": "Crucial",
        "info": "Топовый SATA SSD с DRAM-кэшем и отличной производительностью для игр и работы.",
        "specs": {
            "capacity": 1000,
            "interface": "SATA III (6 Гбит/с)",
            "tbw": 360,
            "dram_cache": "Есть",
            "read_speed": 560,
            "nand_type": "TLC (3 бита)",
            "write_speed": 510,
            "nand_structure": "Micron 3D NAND (Gen3/Gen4)",
            "dwpd": "Не указано (Потребительский)",
            "controller": "Silicon Motion SM2262 / SM2263"
        }
    },
    {
        "title": "Samsung 870 EVO 2TB (MZ-77E2T0B)",
        "price": 14990, "brand": "Samsung",
        "info": "Максимальная емкость для SATA интерфейса с отличной надежностью.",
        "specs": {
            "capacity": 2000,
            "interface": "SATA III (6 Гбит/с)",
            "tbw": 1200,
            "dram_cache": "Есть",
            "read_speed": 560,
            "nand_type": "TLC (3 бита)",
            "write_speed": 530,
            "nand_structure": "Samsung V-NAND (6-7 поколение)",
            "dwpd": "Не указано (Потребительский)",
            "controller": "Samsung MJX / MKX / MEX"
        }
    },

    # === ENTERPRISE / СЕРВЕРНЫЕ ===
    {
        "title": "Samsung PM893 960GB (MZ-7L39600)",
        "price": 18990, "brand": "Samsung",
        "info": "Серверный SSD с высоким ресурсом записи для дата-центров и NAS.",
        "specs": {
            "capacity": 960,
            "interface": "SATA III (6 Гбит/с)",
            "tbw": 1752,
            "dram_cache": "Есть",
            "read_speed": 550,
            "nand_type": "TLC (3 бита)",
            "write_speed": 520,
            "nand_structure": "Samsung V-NAND (6-7 поколение)",
            "dwpd": "1 (Mixed Use)",
            "controller": "Samsung MJX / MKX / MEX"
        }
    },
    {
        "title": "Intel DC S4510 1.92TB (SSDSCKKB1T92T1)",
        "price": 34990, "brand": "Intel",
        "info": "Корпоративный SSD для серверов с максимальным ресурсом записи и MTBF.",
        "specs": {
            "capacity": 1920,
            "interface": "SATA III (6 Гбит/с)",
            "tbw": 6984,
            "dram_cache": "Есть",
            "read_speed": 560,
            "nand_type": "TLC (3 бита)",
            "write_speed": 510,
            "nand_structure": "3D NAND (96–128 слоев)",
            "dwpd": "3 (Write Intensive)",
            "controller": "Marvell 88SS1074"
        }
    },

    # === МАКСИМАЛЬНАЯ ЕМКОСТЬ ===
    {
        "title": "Seagate IronWolf 125 4TB (ZA4000NM10011)",
        "price": 44990, "brand": "Seagate",
        "info": "Специализированный SSD для NAS с высокой емкостью и надежностью.",
        "specs": {
            "capacity": 4000,
            "interface": "SATA III (6 Гбит/с)",
            "tbw": 7300,
            "dram_cache": "Есть",
            "read_speed": 560,
            "nand_type": "TLC (3 бита)",
            "write_speed": 530,
            "nand_structure": "3D NAND (144–176 слоев)",
            "dwpd": "1 (Mixed Use)",
            "controller": "Phison E12 / E12S"
        }
    },
    {
        "title": "Western Digital WD Gold 8TB (WDS800T3X0E)",
        "price": 89990, "brand": "Western Digital",
        "info": "Флагманский серверный SSD с максимальным ресурсом для дата-центров.",
        "specs": {
            "capacity": 8000,
            "interface": "SATA III (6 Гбит/с)",
            "tbw": 14400,
            "dram_cache": "Есть",
            "read_speed": 560,
            "nand_type": "TLC (3 бита)",
            "write_speed": 530,
            "nand_structure": "3D NAND (232+ слоя)",
            "dwpd": "10 (Endurance)",
            "controller": "WD / SanDisk (собственный)"
        }
    },
]

# ==========================================
# SSD M.2 (12 товаров)
# ==========================================
REALISTIC_SSD_M2 = [
    # === БЮДЖЕТНЫЕ NVMe ===
    {
        "title": "Kingston NV2 500GB (SNV2S/500G)",
        "price": 3990, "brand": "Kingston",
        "info": "Бюджетный NVMe SSD для апгрейда ноутбуков и ПК с PCIe 4.0.",
        "specs": {
            "capacity": 500,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 4.0 x4",
            "form_factor": "2280",
            "has_dram": "Нет (DRAM-less)",
            "read_speed": 3500,
            "tbw": 200,
            "write_speed": 2100,
            "has_heatsink": "Нет",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "Phison E21T"
        }
    },
    {
        "title": "Crucial P3 1TB (CT1000P3SSD8)",
        "price": 6490, "brand": "Crucial",
        "info": "Доступный NVMe SSD с хорошей производительностью для игр и работы.",
        "specs": {
            "capacity": 1000,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 4.0 x4",
            "form_factor": "2280",
            "has_dram": "Нет (DRAM-less)",
            "read_speed": 5000,
            "tbw": 400,
            "write_speed": 3600,
            "has_heatsink": "Нет",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "Micron (собственный)"
        }
    },

    # === СРЕДНИЙ СЕГМЕНТ ===
    {
        "title": "Samsung 980 1TB (MZ-V8V1T0BW)",
        "price": 8990, "brand": "Samsung",
        "info": "Популярный NVMe SSD без DRAM, но с высокой производительностью.",
        "specs": {
            "capacity": 1000,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 3.0 x4",
            "form_factor": "2280",
            "has_dram": "Нет (DRAM-less)",
            "read_speed": 3500,
            "tbw": 600,
            "write_speed": 3000,
            "has_heatsink": "Нет",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "Samsung (собственный)"
        }
    },
    {
        "title": "WD Blue SN580 1TB (WDS100T3B0E)",
        "price": 7490, "brand": "Western Digital",
        "info": "Надежный NVMe SSD для повседневных задач с PCIe 4.0.",
        "specs": {
            "capacity": 1000,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 4.0 x4",
            "form_factor": "2280",
            "has_dram": "Нет (DRAM-less)",
            "read_speed": 4150,
            "tbw": 500,
            "write_speed": 4150,
            "has_heatsink": "Нет",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "WD / SanDisk (собственный)"
        }
    },
    {
        "title": "SK Hynix Gold P31 1TB (HFS001TEJ9X101N)",
        "price": 9990, "brand": "SK Hynix",
        "info": "Энергоэффективный NVMe SSD с высокой производительностью и низким нагревом.",
        "specs": {
            "capacity": 1000,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 3.0 x4",
            "form_factor": "2280",
            "has_dram": "Есть",
            "read_speed": 3500,
            "tbw": 750,
            "write_speed": 3200,
            "has_heatsink": "Нет",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "SK Hynix (собственный)"
        }
    },

    # === HIGH-END NVMe ===
    {
        "title": "Samsung 990 PRO 2TB (MZ-V9P2T0BW)",
        "price": 19990, "brand": "Samsung",
        "info": "Флагманский NVMe SSD с PCIe 4.0 для энтузиастов и профессионалов.",
        "specs": {
            "capacity": 2000,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 4.0 x4",
            "form_factor": "2280",
            "has_dram": "Есть",
            "read_speed": 7450,
            "tbw": 1200,
            "write_speed": 6900,
            "has_heatsink": "Опционально / Съемный",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "Samsung (собственный)"
        }
    },
    {
        "title": "WD Black SN850X 2TB (WDS200T2X0E)",
        "price": 18990, "brand": "Western Digital",
        "info": "Топовый игровой SSD с PCIe 4.0 и отличной производительностью.",
        "specs": {
            "capacity": 2000,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 4.0 x4",
            "form_factor": "2280",
            "has_dram": "Есть",
            "read_speed": 7300,
            "tbw": 1200,
            "write_speed": 6600,
            "has_heatsink": "Опционально / Съемный",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "WD / SanDisk (собственный)"
        }
    },
    {
        "title": "Seagate FireCuda 530 2TB (ZP2000GM3A013)",
        "price": 21990, "brand": "Seagate",
        "info": "Максимальная производительность PCIe 4.0 с ресурсом записи 2550 ТБ.",
        "specs": {
            "capacity": 2000,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 4.0 x4",
            "form_factor": "2280",
            "has_dram": "Есть",
            "read_speed": 7300,
            "tbw": 2550,
            "write_speed": 6900,
            "has_heatsink": "Опционально / Съемный",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "Phison E18"
        }
    },

    # === PCIe 5.0 (НОВЕЙШИЕ) ===
    {
        "title": "Crucial T700 2TB (CT2000T700SSD3)",
        "price": 29990, "brand": "Crucial",
        "info": "Один из первых потребительских SSD с PCIe 5.0 и рекордной скоростью.",
        "specs": {
            "capacity": 2000,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 5.0 x4",
            "form_factor": "2280",
            "has_dram": "Есть",
            "read_speed": 12400,
            "tbw": 1200,
            "write_speed": 11800,
            "has_heatsink": "Есть (в комплекте)",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "Phison E25 / E25T"
        }
    },
    {
        "title": "Corsair MP700 PRO 2TB (CSSD-F2000GBMP700)",
        "price": 32990, "brand": "Corsair",
        "info": "Флагманский PCIe 5.0 SSD с радиатором и максимальной производительностью.",
        "specs": {
            "capacity": 2000,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 5.0 x4",
            "form_factor": "2280",
            "has_dram": "Есть",
            "read_speed": 14000,
            "tbw": 1400,
            "write_speed": 12000,
            "has_heatsink": "Есть (в комплекте)",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "Phison E31T"
        }
    },

    # === КОМПАКТНЫЕ (2230/2242) ===
    {
        "title": "Samsung 990 EVO 1TB (MZ-V9E1T0BW)",
        "price": 11990, "brand": "Samsung",
        "info": "Компактный NVMe SSD для ноутбуков и устройств с ограниченным пространством.",
        "specs": {
            "capacity": 1000,
            "has_nvme": "Да (NVMe)",
            "interface": "PCIe 4.0 x4",
            "form_factor": "2230",
            "has_dram": "Нет (DRAM-less)",
            "read_speed": 5000,
            "tbw": 600,
            "write_speed": 4200,
            "has_heatsink": "Нет",
            "nand_type": "TLC (3 бита)",
            "m_key": "M-Key (PCIe NVMe / SATA)",
            "pcie_lanes": "x4",
            "controller": "Samsung (собственный)"
        }
    },

    # === SATA M.2 (БЕЗ NVMe) ===
    {
        "title": "Samsung 870 EVO M.2 1TB (MZ-77E1T0B)",
        "price": 8990, "brand": "Samsung",
        "info": "SATA M.2 SSD для старых материнских плат без поддержки NVMe.",
        "specs": {
            "capacity": 1000,
            "has_nvme": "Нет (SATA M.2)",
            "interface": "SATA III (6 Гбит/с)",
            "form_factor": "2280",
            "has_dram": "Есть",
            "read_speed": 560,
            "tbw": 600,
            "write_speed": 530,
            "has_heatsink": "Нет",
            "nand_type": "TLC (3 бита)",
            "m_key": "B+M Key (SATA)",
            "pcie_lanes": "x2",
            "controller": "Samsung MJX / MKX / MEX"
        }
    },
]


def seed_ssds():
    print("🚀 Начинаю создание реалистичных SSD накопителей...")

    # === SSD 2.5" ===
    print("\n=== SSD 2.5\" ===")
    created_25 = 0
    for item in REALISTIC_SSD_25:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"⏭️  Пропуск: {item['title']} уже существует")
            continue

        warranty_map = {
            "Kingston": "60 месяцев",
            "Crucial": "60 месяцев",
            "Western Digital": "60 месяцев",
            "Samsung": "60 месяцев",
            "Intel": "60 месяцев",
            "Seagate": "60 месяцев",
        }

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(5, 50),
            warranty=warranty_map.get(item["brand"], "36 месяцев")
        )
        p.categories.add(ssd_25_cat)
        created_25 += 1
        print(f"✅ {p.title} | {item['specs']['capacity']}GB | {item['specs']['interface']} | {item['price']} ₽")

    print(f"\n SSD 2.5\": добавлено {created_25}")

    # === SSD M.2 ===
    print("\n=== SSD M.2 ===")
    created_m2 = 0
    for item in REALISTIC_SSD_M2:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"⏭️  Пропуск: {item['title']} уже существует")
            continue

        warranty_map = {
            "Kingston": "60 месяцев",
            "Crucial": "60 месяцев",
            "Western Digital": "60 месяцев",
            "Samsung": "60 месяцев",
            "SK Hynix": "60 месяцев",
            "Seagate": "60 месяцев",
            "Corsair": "60 месяцев",
        }

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(3, 40),
            warranty=warranty_map.get(item["brand"], "36 месяцев")
        )
        p.categories.add(ssd_m2_cat)
        created_m2 += 1
        print(f"✅ {p.title} | {item['specs']['capacity']}GB | {item['specs']['interface']} | {item['price']} ₽")

    print(f"\n🎉 SSD M.2: добавлено {created_m2}")
    print(f"\n{'=' * 50}")
    print(f"🏆 ИТОГО: SSD 2.5\"={created_25}, SSD M.2={created_m2}")
    print(f"🏆 ВСЕГО: {created_25 + created_m2} SSD накопителей")


if __name__ == '__main__':
    seed_ssds()