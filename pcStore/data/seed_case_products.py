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

case_cat, _ = Category.objects.get_or_create(title='Корпуса', slug='pc-case')

REALISTIC_CASES = [
    # === ПОПУЛЯРНЫЕ MID TOWER (6000-12000 ₽) ===
    {
        "title": "NZXT H5 Flow (2023) Black",
        "price": 7990, "brand": "NZXT",
        "info": "Классический Mid Tower с отличной циркуляцией воздуха и минималистичным дизайном.",
        "specs": {
            "mb_support": "ATX", "case_type": "Mid Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "2 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 165,
            "max_gpu_length": 360, "has_side_window": "Есть"
        }
    },
    {
        "title": "Corsair 4000D Airflow White",
        "price": 8490, "brand": "Corsair",
        "info": "Один из самых популярных корпусов для игровых сборок с сетчатой передней панелью.",
        "specs": {
            "mb_support": "ATX", "case_type": "Mid Tower", "color": "Белый",
            "aquarium_style": "Нет", "included_fans": "2 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 170,
            "max_gpu_length": 360, "has_side_window": "Есть"
        }
    },
    {
        "title": "be quiet! Pure Base 500DX Black",
        "price": 9990, "brand": "be quiet!",
        "info": "Корпус с тихими вентиляторами Pure Wings 2 и ARGB подсветкой.",
        "specs": {
            "mb_support": "ATX", "case_type": "Mid Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "3 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 190,
            "max_gpu_length": 369, "has_side_window": "Есть"
        }
    },
    {
        "title": "Fractal Design Meshify 2 Compact",
        "price": 11990, "brand": "Fractal Design",
        "info": "Компактный Mid Tower с уникальной сетчатой передней панелью и премиальным качеством.",
        "specs": {
            "mb_support": "ATX", "case_type": "Mid Tower", "color": "Серый",
            "aquarium_style": "Нет", "included_fans": "3 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 172,
            "max_gpu_length": 341, "has_side_window": "Есть"
        }
    },
    {
        "title": "DeepCool CH560 Digital Black",
        "price": 6990, "brand": "DeepCool",
        "info": "Современный корпус с цифровым дисплеем температуры и хорошей продуваемостью.",
        "specs": {
            "mb_support": "ATX", "case_type": "Mid Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "4 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 160,
            "max_gpu_length": 380, "has_side_window": "Есть"
        }
    },

    # === АКВАРИУМЫ (популярные в 2024) ===
    {
        "title": "Lian Li O11 Dynamic EVO White",
        "price": 14990, "brand": "Lian Li",
        "info": "Легендарный корпус-аквариум с двумя камерами и максимальной кастомизацией.",
        "specs": {
            "mb_support": "E-ATX", "case_type": "Mid Tower", "color": "Белый",
            "aquarium_style": "Да", "included_fans": "Без вентиляторов", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 167,
            "max_gpu_length": 457, "has_side_window": "Есть"
        }
    },
    {
        "title": "NZXT H9 Flow Black/White",
        "price": 15990, "brand": "NZXT",
        "info": "Двухкамерный корпус-аквариум с панорамным видом на компоненты.",
        "specs": {
            "mb_support": "ATX", "case_type": "Mid Tower", "color": "Белый",
            "aquarium_style": "Да", "included_fans": "Без вентиляторов", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 165,
            "max_gpu_length": 400, "has_side_window": "Есть"
        }
    },
    {
        "title": "Lian Li Lancool III Mesh ARGB Black",
        "price": 12990, "brand": "Lian Li",
        "info": "Мощный корпус с сетчатой передней панелью и отличной поддержкой СЖО.",
        "specs": {
            "mb_support": "E-ATX", "case_type": "Mid Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "4 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 167,
            "max_gpu_length": 423, "has_side_window": "Есть"
        }
    },
    {
        "title": "Phanteks G500A Black",
        "price": 10990, "brand": "Phanteks",
        "info": "Корпус-аквариум с четырьмя D-RGB вентиляторами в комплекте.",
        "specs": {
            "mb_support": "ATX", "case_type": "Mid Tower", "color": "Черный",
            "aquarium_style": "Да", "included_fans": "4 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 162,
            "max_gpu_length": 415, "has_side_window": "Есть"
        }
    },

    # === FULL TOWER ДЛЯ ЭНТУЗИАСТОВ ===
    {
        "title": "be quiet! Dark Base Pro 901 Black",
        "price": 24990, "brand": "be quiet!",
        "info": "Флагманский Full Tower с модульной конструкцией и шумоизоляцией.",
        "specs": {
            "mb_support": "E-ATX", "case_type": "Full Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "2 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 194,
            "max_gpu_length": 490, "has_side_window": "Есть"
        }
    },
    {
        "title": "Fractal Design Torrent Black TG",
        "price": 18990, "brand": "Fractal Design",
        "info": "Культовый корпус для кастомных СЖО с уникальной сетчатой передней панелью.",
        "specs": {
            "mb_support": "E-ATX", "case_type": "Full Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "5 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 185,
            "max_gpu_length": 461, "has_side_window": "Есть"
        }
    },
    {
        "title": "Corsair 7000D Airflow Black",
        "price": 22990, "brand": "Corsair",
        "info": "Огромный Full Tower для топовых сборок с тремя видеокартами.",
        "specs": {
            "mb_support": "E-ATX", "case_type": "Full Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "2 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 190,
            "max_gpu_length": 420, "has_side_window": "Есть"
        }
    },

    # === MINI-ITX / SFF КОМПАКТНЫЕ ===
    {
        "title": "NZXT H1 V2 Black",
        "price": 29990, "brand": "NZXT",
        "info": "Компактный вертикальный корпус для Mini-ITX с встроенным БП и СЖО.",
        "specs": {
            "mb_support": "Mini-ITX", "case_type": "Small Form Factor (SFF)", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "2 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 148,
            "max_gpu_length": 324, "has_side_window": "Есть"
        }
    },
    {
        "title": "Fractal Design Terra Black",
        "price": 13990, "brand": "Fractal Design",
        "info": "Минималистичный SFF-корпус с отделкой из орехового дерева.",
        "specs": {
            "mb_support": "Mini-ITX", "case_type": "Small Form Factor (SFF)", "color": "Дерево / Финиш под дерево",
            "aquarium_style": "Нет", "included_fans": "Без вентиляторов", "psu_location": "Снизу",
            "window_material": "Перфорация (Mesh)", "max_cooler_height": 80,
            "max_gpu_length": 322, "has_side_window": "Нет"
        }
    },
    {
        "title": "Cooler Master NR200P V2 White",
        "price": 8990, "brand": "Cooler Master",
        "info": "Популярный компактный корпус для Mini-ITX с хорошим охлаждением.",
        "specs": {
            "mb_support": "Mini-ITX", "case_type": "Mini Tower", "color": "Белый",
            "aquarium_style": "Нет", "included_fans": "2 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 155,
            "max_gpu_length": 330, "has_side_window": "Есть"
        }
    },
    {
        "title": "Lian Li A4-H2O Black",
        "price": 19990, "brand": "Lian Li",
        "info": "Премиальный SFF-корпус с предустановленной СЖО для видеокарты.",
        "specs": {
            "mb_support": "Mini-ITX", "case_type": "Small Form Factor (SFF)", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "2 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 90,
            "max_gpu_length": 320, "has_side_window": "Есть"
        }
    },

    # === БЮДЖЕТНЫЕ (до 6000 ₽) ===
    {
        "title": "DeepCool MACUBE 110 Black",
        "price": 4490, "brand": "DeepCool",
        "info": "Тихий бюджетный корпус с хорошей сборкой и шумоизоляцией.",
        "specs": {
            "mb_support": "Micro-ATX (mATX)", "case_type": "Mid Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "1 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 160,
            "max_gpu_length": 320, "has_side_window": "Есть"
        }
    },
    {
        "title": "Zalman i3 Neo Black",
        "price": 3990, "brand": "Zalman",
        "info": "Доступный корпус с RGB вентиляторами и закаленным стеклом.",
        "specs": {
            "mb_support": "Micro-ATX (mATX)", "case_type": "Mid Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "3 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 155,
            "max_gpu_length": 320, "has_side_window": "Есть"
        }
    },
    {
        "title": "Thermaltake Versa H18 Tempered Glass",
        "price": 3490, "brand": "Thermaltake",
        "info": "Ультрабюджетный корпус с боковым стеклом для базовых сборок.",
        "specs": {
            "mb_support": "Micro-ATX (mATX)", "case_type": "Mid Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "1 шт", "psu_location": "Снизу",
            "window_material": "Закаленное стекло", "max_cooler_height": 155,
            "max_gpu_length": 300, "has_side_window": "Есть"
        }
    },

    # === БЕЗ ОКНА (MESH / СТРОГИЙ ДИЗАЙН) ===
    {
        "title": "Fractal Design Define 7 Compact",
        "price": 10990, "brand": "Fractal Design",
        "info": "Строгий корпус без стекла с отличной шумоизоляцией.",
        "specs": {
            "mb_support": "ATX", "case_type": "Mid Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "3 шт", "psu_location": "Снизу",
            "window_material": "Перфорация (Mesh)", "max_cooler_height": 169,
            "max_gpu_length": 315, "has_side_window": "Нет"
        }
    },
    {
        "title": "be quiet! Silent Base 802 Black",
        "price": 13990, "brand": "be quiet!",
        "info": "Тихий корпус с шумоизоляционными панелями и без стекла.",
        "specs": {
            "mb_support": "ATX", "case_type": "Mid Tower", "color": "Черный",
            "aquarium_style": "Нет", "included_fans": "3 шт", "psu_location": "Снизу",
            "window_material": "Перфорация (Mesh)", "max_cooler_height": 190,
            "max_gpu_length": 434, "has_side_window": "Нет"
        }
    },

    # === СЕРВЕРНЫЕ / РАКМОНТ ===
    {
        "title": "Cooler Master Storm Trooper",
        "price": 16990, "brand": "Cooler Master",
        "info": "Полноразмерный корпус с поддержкой серверного оборудования.",
        "specs": {
            "mb_support": "E-ATX", "case_type": "Full Tower", "color": "Серебристый",
            "aquarium_style": "Нет", "included_fans": "2 шт", "psu_location": "Снизу",
            "window_material": "Перфорация (Mesh)", "max_cooler_height": 185,
            "max_gpu_length": 450, "has_side_window": "Нет"
        }
    },
]

def seed_cases():
    print("🚀 Начинаю создание реалистичных корпусов...")
    created_count = 0

    for item in REALISTIC_CASES:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"⏭️  Пропуск: {item['title']} уже существует")
            continue

        warranty_map = {
            "NZXT": "24 месяца",
            "Corsair": "24 месяца",
            "be quiet!": "36 месяцев",
            "Fractal Design": "24 месяца",
            "DeepCool": "36 месяцев",
            "Lian Li": "24 месяца",
            "Phanteks": "24 месяца",
            "Cooler Master": "24 месяца",
            "Thermaltake": "24 месяца",
            "Zalman": "24 месяца",
        }

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(3, 20),
            warranty=warranty_map.get(item["brand"], "24 месяца")
        )
        p.categories.add(case_cat)
        created_count += 1
        print(f"✅ Создано: {p.title} | {item['specs']['case_type']} | {item['specs']['color']} | {item['price']} ₽")

    print(f"\n🎉 Готово! Добавлено {created_count} новых корпусов.")

if __name__ == '__main__':
    seed_cases()