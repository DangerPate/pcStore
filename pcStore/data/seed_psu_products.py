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

psu_cat, _ = Category.objects.get_or_create(title='Блоки питания', slug='psu')

REALISTIC_PSUS = [
    # === БЮДЖЕТНЫЕ (до 5000 ₽) ===
    {
        "title": "Chieftec Smart GPS-500 500W",
        "price": 3490, "brand": "Chieftec",
        "info": "Бюджетный блок питания для офисных ПК без высоких требований к энергопотреблению.",
        "specs": {
            "wattage": 500,
            "certification": "80 Plus Standard",
            "modularity": "Немодульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.31",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "4+4 pin",
            "cable_sleeving": "Без оплетки"
        }
    },
    {
        "title": "Aerocool VX PLUS 600W",
        "price": 3990, "brand": "Aerocool",
        "info": "Компактный блок питания для базовых игровых сборок среднего уровня.",
        "specs": {
            "wattage": 600,
            "certification": "80 Plus Standard",
            "modularity": "Немодульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.31",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "8-pin (4+4)",
            "cable_sleeving": "Без оплетки"
        }
    },
    {
        "title": "DeepCool PF550 550W",
        "price": 3790, "brand": "DeepCool",
        "info": "Надёжный бюджетный блок с чёрными плоскими кабелями и активным PFC.",
        "specs": {
            "wattage": 550,
            "certification": "80 Plus",
            "modularity": "Немодульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.31",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "4+4 pin",
            "cable_sleeving": "Плоские кабели"
        }
    },
    {
        "title": "1stPlayer FSP350-60SG 350W",
        "price": 2490, "brand": "1stPlayer",
        "info": "Ультрабюджетный блок для нетребовательных офисных конфигураций.",
        "specs": {
            "wattage": 350,
            "certification": "Нет сертификата",
            "modularity": "Немодульный",
            "form_factor": "ATX",
            "pci_e_connectors": "6-pin",
            "atx_standard": "ATX 12V 2.03",
            "pfc": "Пассивный (Passive PFC)",
            "cpu_connectors": "4-pin",
            "cable_sleeving": "Без оплетки"
        }
    },

    # === СРЕДНИЙ СЕГМЕНТ (5000–10000 ₽) ===
    {
        "title": "be quiet! System Power 10 550W",
        "price": 5990, "brand": "be quiet!",
        "info": "Немецкий блок питания с отличным соотношением цена/качество и тихим вентилятором.",
        "specs": {
            "wattage": 550,
            "certification": "80 Plus Bronze",
            "modularity": "Немодульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.52",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "8-pin (4+4)",
            "cable_sleeving": "Без оплетки"
        }
    },
    {
        "title": "DeepCool PK650D 650W 80 Plus Bronze",
        "price": 5490, "brand": "DeepCool",
        "info": "Сертифицированный Bronze блок с плоскими кабелями и 5-летней гарантией.",
        "specs": {
            "wattage": 650,
            "certification": "80 Plus Bronze",
            "modularity": "Немодульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.52",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "4+4 pin",
            "cable_sleeving": "Плоские кабели"
        }
    },
    {
        "title": "Corsair CX550 550W 80 Plus Bronze",
        "price": 5990, "brand": "Corsair",
        "info": "Классический блок от Corsair для игровых сборок начального уровня.",
        "specs": {
            "wattage": 550,
            "certification": "80 Plus Bronze",
            "modularity": "Немодульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 6-pin",
            "atx_standard": "ATX 12V 2.31",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "8-pin (4+4)",
            "cable_sleeving": "Без оплетки"
        }
    },
    {
        "title": "Aerocool KCAS Plus 750W 80 Plus Bronze",
        "price": 6290, "brand": "Aerocool",
        "info": "Мощный блок для сборок с одной видеокартой уровня RTX 4070.",
        "specs": {
            "wattage": 750,
            "certification": "80 Plus Bronze",
            "modularity": "Полумодульный",
            "form_factor": "ATX",
            "pci_e_connectors": "3x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.31",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "8+4 pin",
            "cable_sleeving": "В оплетке"
        }
    },
    {
        "title": "be quiet! Pure Power 12 M 650W",
        "price": 8990, "brand": "be quiet!",
        "info": "Полностью модульный блок с тихим 120-мм вентилятором и сертификатом Gold.",
        "specs": {
            "wattage": 650,
            "certification": "80 Plus Gold",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.52",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "8+8 pin",
            "cable_sleeving": "В оплетке"
        }
    },

    # === HIGH-END (10000–20000 ₽) ===
    {
        "title": "Corsair RM850e (2023) 850W 80 Plus Gold",
        "price": 11990, "brand": "Corsair",
        "info": "Полностью модульный блок питания для игровых систем с одной мощной видеокартой.",
        "specs": {
            "wattage": 850,
            "certification": "80 Plus Gold",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.52",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "8+8 pin",
            "cable_sleeving": "В оплетке"
        }
    },
    {
        "title": "Seasonic Focus GX-850 850W 80 Plus Gold",
        "price": 12490, "brand": "Seasonic",
        "info": "Легендарный блок питания Seasonic с 10-летней гарантией и топ-качеством сборки.",
        "specs": {
            "wattage": 850,
            "certification": "80 Plus Gold",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.52",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "8+8 pin",
            "cable_sleeving": "В оплетке"
        }
    },
    {
        "title": "be quiet! Straight Power 12 1000W 80 Plus Platinum",
        "price": 17990, "brand": "be quiet!",
        "info": "Топовый блок питания с платиновым сертификатом и вентилятором Silent Wings 4.",
        "specs": {
            "wattage": 1000,
            "certification": "80 Plus Platinum",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "4x 8-pin (6+2)",
            "atx_standard": "ATX 3.0",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "2x 8-pin (4+4)",
            "cable_sleeving": "В оплетке"
        }
    },
    {
        "title": "Corsair HX1000i 1000W 80 Plus Platinum",
        "price": 19990, "brand": "Corsair",
        "info": "Профессиональный блок с мониторингом через Corsair iCUE и платиновой эффективностью.",
        "specs": {
            "wattage": 1000,
            "certification": "80 Plus Platinum",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "4x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.4",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "2x 8-pin (4+4)",
            "cable_sleeving": "В оплетке"
        }
    },
    {
        "title": "DeepCool PX1000G 1000W 80 Plus Gold",
        "price": 14990, "brand": "DeepCool",
        "info": "Блок стандарта ATX 3.0 с кабелем 12VHPWR для карт NVIDIA RTX 40-серии.",
        "specs": {
            "wattage": 1000,
            "certification": "80 Plus Gold",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "1x 16-pin (12V-2x6)",
            "atx_standard": "ATX 3.0",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "2x 8-pin (4+4)",
            "cable_sleeving": "В оплетке"
        }
    },
    {
        "title": "MSI MPG A850G PCIE5 850W 80 Plus Gold",
        "price": 11990, "brand": "MSI",
        "info": "Блок питания с нативным кабелем 12V-2x6 для видеокарт нового поколения.",
        "specs": {
            "wattage": 850,
            "certification": "80 Plus Gold",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "1x 16-pin (12V-2x6)",
            "atx_standard": "ATX 3.1",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "2x 8-pin (4+4)",
            "cable_sleeving": "В оплетке"
        }
    },

    # === ЭНТУЗИАСТСКИЕ (20000+ ₽) ===
    {
        "title": "Seasonic PRIME TX-1000 1000W 80 Plus Titanium",
        "price": 24990, "brand": "Seasonic",
        "info": "Флагман Seasonic с титановым сертификатом эффективности и 12-летней гарантией.",
        "specs": {
            "wattage": 1000,
            "certification": "80 Plus Titanium",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "4x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.52",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "2x 8-pin (4+4)",
            "cable_sleeving": "Silicone Cables"
        }
    },
    {
        "title": "Corsair AX1600i 1600W 80 Plus Titanium",
        "price": 39990, "brand": "Corsair",
        "info": "Абсолютный топ для экстремальных сборок с несколькими RTX 4090. Цифровое управление.",
        "specs": {
            "wattage": 1600,
            "certification": "80 Plus Titanium",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "4x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.52",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "2x 8-pin (4+4)",
            "cable_sleeving": "Silicone Cables"
        }
    },
    {
        "title": "be quiet! Dark Power Pro 13 1300W 80 Plus Titanium",
        "price": 42990, "brand": "be quiet!",
        "info": "Премиальный блок для workstation-систем с двумя GPU и разгоном процессора.",
        "specs": {
            "wattage": 1300,
            "certification": "80 Plus Titanium",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "4x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.52",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "2x 8-pin (4+4)",
            "cable_sleeving": "Silicone Cables"
        }
    },
    {
        "title": "ASUS ROG Thor 1200P2 1200W 80 Plus Platinum",
        "price": 34990, "brand": "ASUS",
        "info": "Блок питания с OLED-дисплеем, показывающим потребление в реальном времени.",
        "specs": {
            "wattage": 1200,
            "certification": "80 Plus Platinum",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 16-pin (12V-2x6)",
            "atx_standard": "ATX 3.0",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "2x 8-pin (4+4)",
            "cable_sleeving": "Silicone Cables"
        }
    },

    # === SFX / SFF (Компактные) ===
    {
        "title": "Corsair SF750 750W 80 Plus Platinum SFX",
        "price": 17990, "brand": "Corsair",
        "info": "Компактный блок формата SFX для мощных мини-сборок. Полностью модульный.",
        "specs": {
            "wattage": 750,
            "certification": "80 Plus Platinum",
            "modularity": "Полностью модульный",
            "form_factor": "SFX",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.31",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "8+4 pin",
            "cable_sleeving": "Silicone Cables"
        }
    },
    {
        "title": "be quiet! SFX L Power 600W 80 Plus Gold",
        "price": 9990, "brand": "be quiet!",
        "info": "Удлинённый формат SFX-L для корпусов Mini-ITX с увеличенной мощностью.",
        "specs": {
            "wattage": 600,
            "certification": "80 Plus Gold",
            "modularity": "Полностью модульный",
            "form_factor": "SFX-L",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.31",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "4+4 pin",
            "cable_sleeving": "В оплетке"
        }
    },
    {
        "title": "Corsair SF850L 850W 80 Plus Platinum SFX-L",
        "price": 19990, "brand": "Corsair",
        "info": "Топовый SFX-L блок с поддержкой ATX 3.0 и кабелем 12VHPWR для RTX 40-серии.",
        "specs": {
            "wattage": 850,
            "certification": "80 Plus Platinum",
            "modularity": "Полностью модульный",
            "form_factor": "SFX-L",
            "pci_e_connectors": "1x 16-pin (12V-2x6)",
            "atx_standard": "ATX 3.0",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "8+8 pin",
            "cable_sleeving": "Silicone Cables"
        }
    },

    # === СЕРВЕРНЫЕ ===
    {
        "title": "Seasonic Prime Fanless TX-700 700W 80 Plus Titanium",
        "price": 27990, "brand": "Seasonic",
        "info": "Пассивный блок без вентилятора для бесшумных workstation-систем.",
        "specs": {
            "wattage": 700,
            "certification": "80 Plus Titanium",
            "modularity": "Полностью модульный",
            "form_factor": "ATX",
            "pci_e_connectors": "2x 8-pin (6+2)",
            "atx_standard": "ATX 12V 2.52",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "8+8 pin",
            "cable_sleeving": "Silicone Cables"
        }
    },
    {
        "title": "Supermicro PWS-1K26P-1R 1200W Platinum Server",
        "price": 34990, "brand": "Supermicro",
        "info": "Серверный блок питания с резервированием (1+1) для стоек 1U.",
        "specs": {
            "wattage": 1200,
            "certification": "80 Plus Platinum",
            "modularity": "Полностью модульный",
            "form_factor": "EPS 12V (Server)",
            "pci_e_connectors": "4x 8-pin (6+2)",
            "atx_standard": "EPS 12V",
            "pfc": "Активный (Active PFC)",
            "cpu_connectors": "2x 8-pin (4+4)",
            "cable_sleeving": "Без оплетки"
        }
    },
]

def seed_psus():
    print(" Начинаю создание реалистичных блоков питания...")
    created_count = 0

    for item in REALISTIC_PSUS:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"⏭️  Пропуск: {item['title']} уже существует")
            continue

        warranty_map = {
            "1stPlayer": "24 месяца",
            "Chieftec": "36 месяцев",
            "Aerocool": "36 месяцев",
            "DeepCool": "60 месяцев",
            "Corsair": "84 месяца" if "Titanium" in item['specs']['certification'] else "60 месяцев",
            "be quiet!": "60 месяцев" if "Titanium" in item['specs']['certification'] else "60 месяцев",
            "Seasonic": "120 месяцев" if "Titanium" in item['specs']['certification'] else "120 месяцев",
            "MSI": "120 месяцев",
            "ASUS": "120 месяцев",
            "Supermicro": "60 месяцев",
        }

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(3, 25),
            warranty=warranty_map.get(item["brand"], "36 месяцев")
        )
        p.categories.add(psu_cat)
        created_count += 1
        print(f"✅ Создано: {p.title} | {item['specs']['wattage']}W | {item['specs']['certification']} | {item['price']} ₽")

    print(f"\n🎉 Готово! Добавлено {created_count} новых блоков питания.")

if __name__ == '__main__':
    seed_psus()