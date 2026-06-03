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

cpu_cat, _ = Category.objects.get_or_create(title='Процессоры', slug='cpu')

REALISTIC_CPUS = [
    # === Intel Core i9 ===
    {
        "title": "Intel Core i9-14900K",
        "price": 52990, "brand": "Intel",
        "info": "Флагманский процессор 14-го поколения для энтузиастов и профессионалов.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i9", "perf_cores": "8",
            "generation": "Intel 14-e поколение", "igpu": "Есть", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.2, "turbo_clock": 6.0, "tdp": 125
        }
    },
    {
        "title": "Intel Core i9-13900K",
        "price": 44990, "brand": "Intel",
        "info": "Мощный процессор 13-го поколения с гибридной архитектурой.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i9", "perf_cores": "8",
            "generation": "Intel 13-e поколение", "igpu": "Есть", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.0, "turbo_clock": 5.8, "tdp": 125
        }
    },
    {
        "title": "Intel Core i9-14900KF",
        "price": 49990, "brand": "Intel",
        "info": "Версия без встроенной графики для систем с дискретной видеокартой.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i9", "perf_cores": "8",
            "generation": "Intel 14-e поколение", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.2, "turbo_clock": 6.0, "tdp": 125
        }
    },

    # === Intel Core i7 ===
    {
        "title": "Intel Core i7-14700K",
        "price": 36990, "brand": "Intel",
        "info": "Оптимальный выбор для high-end игровых систем и рабочих станций.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i7", "perf_cores": "6",
            "generation": "Intel 14-e поколение", "igpu": "Есть", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.4, "turbo_clock": 5.6, "tdp": 125
        }
    },
    {
        "title": "Intel Core i7-13700K",
        "price": 32990, "brand": "Intel",
        "info": "Производительный процессор для игр и многопоточных задач.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i7", "perf_cores": "6",
            "generation": "Intel 13-e поколение", "igpu": "Есть", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.4, "turbo_clock": 5.4, "tdp": 125
        }
    },
    {
        "title": "Intel Core i7-14700KF",
        "price": 34990, "brand": "Intel",
        "info": "Версия i7-14700K без встроенной графики.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i7", "perf_cores": "6",
            "generation": "Intel 14-e поколение", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.4, "turbo_clock": 5.6, "tdp": 125
        }
    },

    # === Intel Core i5 ===
    {
        "title": "Intel Core i5-14600K",
        "price": 26990, "brand": "Intel",
        "info": "Средний сегмент для игровых ПК с отличной производительностью.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i5", "perf_cores": "6",
            "generation": "Intel 14-e поколение", "igpu": "Есть", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.5, "turbo_clock": 5.3, "tdp": 125
        }
    },
    {
        "title": "Intel Core i5-13600K",
        "price": 24990, "brand": "Intel",
        "info": "Популярный выбор для игровых сборок среднего бюджета.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i5", "perf_cores": "6",
            "generation": "Intel 13-e поколение", "igpu": "Есть", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.5, "turbo_clock": 5.1, "tdp": 125
        }
    },
    {
        "title": "Intel Core i5-14400F",
        "price": 19990, "brand": "Intel",
        "info": "Бюджетный процессор без встроенной графики для игровых ПК.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i5", "perf_cores": "6",
            "generation": "Intel 14-e поколение", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "OEM (Tray / лоток)",
            "base_clock": 2.5, "turbo_clock": 4.7, "tdp": 65
        }
    },
    {
        "title": "Intel Core i5-13400F",
        "price": 17990, "brand": "Intel",
        "info": "Экономичный вариант для игровых систем среднего уровня.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i5", "perf_cores": "6",
            "generation": "Intel 13-e поколение", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "OEM (Tray / лоток)",
            "base_clock": 2.5, "turbo_clock": 4.6, "tdp": 65
        }
    },

    # === Intel Core i3 ===
    {
        "title": "Intel Core i3-14100",
        "price": 12990, "brand": "Intel",
        "info": "Бюджетный процессор для офисных и домашних ПК.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i3", "perf_cores": "4",
            "generation": "Intel 14-e поколение", "igpu": "Есть", "memory_type": "DDR5",
            "purpose": "Для офиса и дома", "packaging": "BOX (розничная)",
            "base_clock": 3.5, "turbo_clock": 4.7, "tdp": 60
        }
    },
    {
        "title": "Intel Core i3-13100",
        "price": 11990, "brand": "Intel",
        "info": "Начальный уровень для базовых задач и нетребовательных игр.",
        "specs": {
            "socket": "LGA1700", "family": "Intel Core i3", "perf_cores": "4",
            "generation": "Intel 13-e поколение", "igpu": "Есть", "memory_type": "DDR4",
            "purpose": "Для офиса и дома", "packaging": "BOX (розничная)",
            "base_clock": 3.4, "turbo_clock": 4.5, "tdp": 60
        }
    },

    # === AMD Ryzen 9 ===
    {
        "title": "AMD Ryzen 9 9950X",
        "price": 59990, "brand": "AMD",
        "info": "Флагманский процессор Zen 5 для рабочих станций и энтузиастов.",
        "specs": {
            "socket": "AM5", "family": "AMD Ryzen 9", "perf_cores": "16",
            "generation": "AMD Ryzen 9000", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Для рабочих станций", "packaging": "BOX (розничная)",
            "base_clock": 4.3, "turbo_clock": 5.7, "tdp": 170
        }
    },
    {
        "title": "AMD Ryzen 9 7950X",
        "price": 49990, "brand": "AMD",
        "info": "Мощный процессор Zen 4 для профессиональных задач.",
        "specs": {
            "socket": "AM5", "family": "AMD Ryzen 9", "perf_cores": "16",
            "generation": "AMD Ryzen 7000", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Для рабочих станций", "packaging": "BOX (розничная)",
            "base_clock": 4.5, "turbo_clock": 5.7, "tdp": 170
        }
    },
    {
        "title": "AMD Ryzen 9 7900X",
        "price": 39990, "brand": "AMD",
        "info": "12-ядерный процессор для многопоточных рабочих нагрузок.",
        "specs": {
            "socket": "AM5", "family": "AMD Ryzen 9", "perf_cores": "12",
            "generation": "AMD Ryzen 7000", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Для рабочих станций", "packaging": "BOX (розничная)",
            "base_clock": 4.7, "turbo_clock": 5.6, "tdp": 170
        }
    },

    # === AMD Ryzen 7 ===
    {
        "title": "AMD Ryzen 7 9700X",
        "price": 34990, "brand": "AMD",
        "info": "Новейший 8-ядерный процессор Zen 5 для игр и творчества.",
        "specs": {
            "socket": "AM5", "family": "AMD Ryzen 7", "perf_cores": "8",
            "generation": "AMD Ryzen 9000", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.8, "turbo_clock": 5.5, "tdp": 65
        }
    },
    {
        "title": "AMD Ryzen 7 7700X",
        "price": 28990, "brand": "AMD",
        "info": "Популярный игровой процессор Zen 4 с высокой частотой.",
        "specs": {
            "socket": "AM5", "family": "AMD Ryzen 7", "perf_cores": "8",
            "generation": "AMD Ryzen 7000", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 4.5, "turbo_clock": 5.4, "tdp": 105
        }
    },
    {
        "title": "AMD Ryzen 7 5800X3D",
        "price": 32990, "brand": "AMD",
        "info": "Легендарный игровой процессор с технологией 3D V-Cache.",
        "specs": {
            "socket": "AM4", "family": "AMD Ryzen 7", "perf_cores": "8",
            "generation": "AMD Ryzen 5000", "igpu": "Нет", "memory_type": "DDR4",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.4, "turbo_clock": 4.5, "tdp": 105
        }
    },
    {
        "title": "AMD Ryzen 7 5700X",
        "price": 22990, "brand": "AMD",
        "info": "Энергоэффективный 8-ядерный процессор для игр и работы.",
        "specs": {
            "socket": "AM4", "family": "AMD Ryzen 7", "perf_cores": "8",
            "generation": "AMD Ryzen 5000", "igpu": "Нет", "memory_type": "DDR4",
            "purpose": "Игровой", "packaging": "OEM (Tray / лоток)",
            "base_clock": 3.4, "turbo_clock": 4.6, "tdp": 65
        }
    },

    # === AMD Ryzen 5 ===
    {
        "title": "AMD Ryzen 5 9600X",
        "price": 24990, "brand": "AMD",
        "info": "6-ядерный процессор Zen 5 для игровых систем среднего уровня.",
        "specs": {
            "socket": "AM5", "family": "AMD Ryzen 5", "perf_cores": "6",
            "generation": "AMD Ryzen 9000", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.9, "turbo_clock": 5.4, "tdp": 65
        }
    },
    {
        "title": "AMD Ryzen 5 7600X",
        "price": 21990, "brand": "AMD",
        "info": "Отличный игровой процессор Zen 4 для платформы AM5.",
        "specs": {
            "socket": "AM5", "family": "AMD Ryzen 5", "perf_cores": "6",
            "generation": "AMD Ryzen 7000", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 4.7, "turbo_clock": 5.3, "tdp": 105
        }
    },
    {
        "title": "AMD Ryzen 5 5600X",
        "price": 16990, "brand": "AMD",
        "info": "Народный выбор для игровых ПК на платформе AM4.",
        "specs": {
            "socket": "AM4", "family": "AMD Ryzen 5", "perf_cores": "6",
            "generation": "AMD Ryzen 5000", "igpu": "Нет", "memory_type": "DDR4",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.7, "turbo_clock": 4.6, "tdp": 65
        }
    },
    {
        "title": "AMD Ryzen 5 5600",
        "price": 14990, "brand": "AMD",
        "info": "Бюджетный 6-ядерный процессор для игр и повседневных задач.",
        "specs": {
            "socket": "AM4", "family": "AMD Ryzen 5", "perf_cores": "6",
            "generation": "AMD Ryzen 5000", "igpu": "Нет", "memory_type": "DDR4",
            "purpose": "Игровой", "packaging": "OEM (Tray / лоток)",
            "base_clock": 3.5, "turbo_clock": 4.4, "tdp": 65
        }
    },

    # === AMD Ryzen 3 ===
    {
        "title": "AMD Ryzen 3 4100",
        "price": 8990, "brand": "AMD",
        "info": "Базовый 4-ядерный процессор для офисных и учебных ПК.",
        "specs": {
            "socket": "AM4", "family": "AMD Ryzen 3", "perf_cores": "4",
            "generation": "AMD Ryzen 4000", "igpu": "Нет", "memory_type": "DDR4",
            "purpose": "Для офиса и дома", "packaging": "OEM (Tray / лоток)",
            "base_clock": 3.8, "turbo_clock": 4.0, "tdp": 65
        }
    },

    # === Intel Core Ultra ===
    {
        "title": "Intel Core Ultra 9 285K",
        "price": 64990, "brand": "Intel",
        "info": "Новейший флагман платформы LGA1851 с AI-ускорителями.",
        "specs": {
            "socket": "LGA1851", "family": "Intel Core Ultra", "perf_cores": "8",
            "generation": "Intel Core Ultra (Series 2)", "igpu": "Есть", "memory_type": "DDR5",
            "purpose": "Для рабочих станций", "packaging": "BOX (розничная)",
            "base_clock": 3.7, "turbo_clock": 5.7, "tdp": 125
        }
    },
    {
        "title": "Intel Core Ultra 7 265K",
        "price": 44990, "brand": "Intel",
        "info": "High-end процессор нового поколения с улучшенной эффективностью.",
        "specs": {
            "socket": "LGA1851", "family": "Intel Core Ultra", "perf_cores": "8",
            "generation": "Intel Core Ultra (Series 2)", "igpu": "Есть", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 3.9, "turbo_clock": 5.5, "tdp": 125
        }
    },
    {
        "title": "Intel Core Ultra 5 245K",
        "price": 32990, "brand": "Intel",
        "info": "Средний сегмент платформы LGA1851 для игровых систем.",
        "specs": {
            "socket": "LGA1851", "family": "Intel Core Ultra", "perf_cores": "6",
            "generation": "Intel Core Ultra (Series 2)", "igpu": "Есть", "memory_type": "DDR5",
            "purpose": "Игровой", "packaging": "BOX (розничная)",
            "base_clock": 4.2, "turbo_clock": 5.2, "tdp": 125
        }
    },

    # === AMD Threadripper ===
    {
        "title": "AMD Ryzen Threadripper 7970X",
        "price": 189990, "brand": "AMD",
        "info": "32-ядерный монстр для профессиональных рабочих станций.",
        "specs": {
            "socket": "sTR5", "family": "AMD Ryzen Threadripper", "perf_cores": "32",
            "generation": "AMD Threadripper 7000", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Для рабочих станций", "packaging": "BOX (розничная)",
            "base_clock": 4.0, "turbo_clock": 5.3, "tdp": 350
        }
    },
    {
        "title": "AMD Ryzen Threadripper 7960X",
        "price": 149990, "brand": "AMD",
        "info": "24-ядерный процессор для ресурсоемких задач.",
        "specs": {
            "socket": "sTR5", "family": "AMD Ryzen Threadripper", "perf_cores": "24",
            "generation": "AMD Threadripper 7000", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Для рабочих станций", "packaging": "BOX (розничная)",
            "base_clock": 4.2, "turbo_clock": 5.3, "tdp": 350
        }
    },

    # === Intel Xeon (серверные) ===
    {
        "title": "Intel Xeon W-3475X",
        "price": 299990, "brand": "Intel",
        "info": "Серверный процессор для профессиональных рабочих станций.",
        "specs": {
            "socket": "LGA4677", "family": "Intel Xeon", "perf_cores": "36",
            "generation": "Intel Xeon W-3400", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Для серверов и дата-центров", "packaging": "BOX (розничная)",
            "base_clock": 3.0, "turbo_clock": 4.8, "tdp": 300
        }
    },

    # === AMD EPYC (серверные) ===
    {
        "title": "AMD EPYC 9354",
        "price": 249990, "brand": "AMD",
        "info": "32-ядерный серверный процессор для дата-центров.",
        "specs": {
            "socket": "SP5", "family": "AMD EPYC", "perf_cores": "32",
            "generation": "AMD EPYC 9004", "igpu": "Нет", "memory_type": "DDR5",
            "purpose": "Для серверов и дата-центров", "packaging": "OEM (Tray / лоток)",
            "base_clock": 3.25, "turbo_clock": 3.75, "tdp": 280
        }
    },
]

def seed_cpus():
    print("🚀 Начинаю создание реалистичных процессоров...")
    created_count = 0

    for item in REALISTIC_CPUS:
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
            in_stock=random.randint(5, 50),
            warranty="36 месяцев"
        )
        p.categories.add(cpu_cat)
        created_count += 1
        print(f"✅ Создано: {p.title} | Цена: {p.price} ₽ | Сокет: {item['specs']['socket']}")

    print(f"\n🎉 Готово! Добавлено {created_count} новых процессоров.")

if __name__ == '__main__':
    seed_cpus()