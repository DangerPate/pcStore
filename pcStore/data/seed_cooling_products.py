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
cooling_cat, _ = Category.objects.get_or_create(title='Охлаждение', slug='pc-cooling')
fans_cat, _ = Category.objects.get_or_create(title='Вентиляторы', slug='case-fan', parent=cooling_cat)
coolers_cat, _ = Category.objects.get_or_create(title='Кулеры', slug='cpu-cooler', parent=cooling_cat)
aio_cat, _ = Category.objects.get_or_create(title='СЖО', slug='liquid-cooling', parent=cooling_cat)

# ==========================================
# ВЕНТИЛЯТОРЫ (20 товаров)
# ==========================================
REALISTIC_FANS = [
    # === TOP-TIER 120mm ===
    {
        "title": "Noctua NF-A12x25 PWM",
        "price": 3490, "brand": "Noctua",
        "info": "Легендарный 120-мм вентилятор с передовой аэродинамикой и минимальным уровнем шума.",
        "specs": {
            "size": "120x120 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Коричневый", "type": "Одиночный вентилятор",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "SSO2 Bearing (Noctua)",
            "noise_level": 22, "max_speed": 2000, "airflow": 60
        }
    },
    {
        "title": "be quiet! Silent Wings 4 120mm PWM",
        "price": 2490, "brand": "be quiet!",
        "info": "Премиальный вентилятор с воронкообразной рамкой для оптимального воздушного потока.",
        "specs": {
            "size": "120x120 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Чёрный", "type": "Одиночный вентилятор",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "Гидродинамический (FDB / HDB)",
            "noise_level": 19, "max_speed": 1900, "airflow": 66
        }
    },
    {
        "title": "Corsair iCUE QL120 RGB 3-Pack",
        "price": 4990, "brand": "Corsair",
        "info": "Комплект из 3 RGB вентиляторов с управлением через iCUE.",
        "specs": {
            "size": "120x120 мм", "lighting": "ARGB (5V 3-pin)", "fan_count": "3",
            "power_connector": "4-pin PWM", "color": "Чёрный", "type": "Комплект вентиляторов",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "Подшипник скольжения (Sleeve)",
            "noise_level": 26, "max_speed": 1500, "airflow": 54
        }
    },
    {
        "title": "Lian Li UNI FAN SL 120 (3-Pack) ARGB",
        "price": 7490, "brand": "Lian Li",
        "info": "Уникальные вентиляторы с соединением без проводов — стыкуются как пазлы.",
        "specs": {
            "size": "120x120 мм", "lighting": "ARGB (5V 3-pin)", "fan_count": "3",
            "power_connector": " proprietary (фирменный)", "color": "Чёрный", "type": "Комплект вентиляторов",
            "speed_control": "Через контроллер/хаб", "bearing_type": "Гидродинамический (FDB / HDB)",
            "noise_level": 25, "max_speed": 1900, "airflow": 68
        }
    },
    {
        "title": "Arctic P12 PWM PST",
        "price": 890, "brand": "Arctic",
        "info": "Бюджетный 120-мм вентилятор с режимом PST (последовательное подключение).",
        "specs": {
            "size": "120x120 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Чёрный", "type": "Одиночный вентилятор",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "Подшипник скольжения (Sleeve)",
            "noise_level": 23, "max_speed": 1800, "airflow": 56
        }
    },
    {
        "title": "DeepCool FC120 ARGB 3-in-1",
        "price": 2990, "brand": "DeepCool",
        "info": "Комплект из 3 вентиляторов с ARGB подсветкой и контроллером в комплекте.",
        "specs": {
            "size": "120x120 мм", "lighting": "ARGB (5V 3-pin)", "fan_count": "3",
            "power_connector": "4-pin PWM", "color": "Чёрный", "type": "Комплект вентиляторов",
            "speed_control": "Через контроллер/хаб", "bearing_type": "Гидродинамический (FDB / HDB)",
            "noise_level": 28, "max_speed": 1800, "airflow": 65
        }
    },

    # === TOP-TIER 140mm ===
    {
        "title": "Noctua NF-A14 PWM",
        "price": 3290, "brand": "Noctua",
        "info": "140-мм вентилятор премиум-класса для корпусов с поддержкой большого формата.",
        "specs": {
            "size": "140x140 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Коричневый", "type": "Одиночный вентилятор",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "SSO2 Bearing (Noctua)",
            "noise_level": 24, "max_speed": 1500, "airflow": 93
        }
    },
    {
        "title": "be quiet! Silent Wings 4 140mm PWM",
        "price": 2790, "brand": "be quiet!",
        "info": "Мощный 140-мм вентилятор с FDB подшипником для бесшумного охлаждения.",
        "specs": {
            "size": "140x140 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Чёрный", "type": "Одиночный вентилятор",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "Гидродинамический (FDB / HDB)",
            "noise_level": 20, "max_speed": 1600, "airflow": 82
        }
    },
    {
        "title": "Arctic P14 PWM PST",
        "price": 990, "brand": "Arctic",
        "info": "Доступный 140-мм вентилятор с высоким воздушным потоком и режимом PST.",
        "specs": {
            "size": "140x140 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Чёрный", "type": "Одиночный вентилятор",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "Подшипник скольжения (Sleeve)",
            "noise_level": 25, "max_speed": 1700, "airflow": 84
        }
    },

    # === БЮДЖЕТНЫЕ 120mm ===
    {
        "title": "DeepCool RF120 (3-Pack)",
        "price": 1990, "brand": "DeepCool",
        "info": "Три RGB вентилятора с пультом управления подсветкой.",
        "specs": {
            "size": "120x120 мм", "lighting": "RGB (12V 4-pin)", "fan_count": "3",
            "power_connector": "3-pin + Molex", "color": "Чёрный", "type": "Комплект вентиляторов",
            "speed_control": "Ручная (резистор/кабель)", "bearing_type": "Подшипник скольжения (Sleeve)",
            "noise_level": 29, "max_speed": 1500, "airflow": 50
        }
    },
    {
        "title": "Zalman ZM-SF3 120mm (3-Pack)",
        "price": 1490, "brand": "Zalman",
        "info": "Ультрабюджетный комплект из 3 вентиляторов с синей LED подсветкой.",
        "specs": {
            "size": "120x120 мм", "lighting": "Синяя LED", "fan_count": "3",
            "power_connector": "3-pin", "color": "Синий", "type": "Комплект вентиляторов",
            "speed_control": "Нет (фиксированная скорость)", "bearing_type": "Подшипник скольжения (Sleeve)",
            "noise_level": 30, "max_speed": 1200, "airflow": 42
        }
    },

    # === 80mm / 92mm ===
    {
        "title": "Noctua NF-A8 PWM",
        "price": 1990, "brand": "Noctua",
        "info": "80-мм вентилятор для компактных корпусов и блоков питания.",
        "specs": {
            "size": "80x80 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Коричневый", "type": "Одиночный вентилятор",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "SSO2 Bearing (Noctua)",
            "noise_level": 21, "max_speed": 2200, "airflow": 33
        }
    },
    {
        "title": "Arctic F9 PWM",
        "price": 690, "brand": "Arctic",
        "info": "92-мм вентилятор с оптимальным балансом шума и производительности.",
        "specs": {
            "size": "92x92 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Чёрный", "type": "Одиночный вентилятор",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "Подшипник скольжения (Sleeve)",
            "noise_level": 22, "max_speed": 1800, "airflow": 41
        }
    },

    # === 200mm ===
    {
        "title": "Noctua NF-A20 PWM",
        "price": 3490, "brand": "Noctua",
        "info": "Огромный 200-мм вентилятор для максимального воздушного потока при минимальных оборотах.",
        "specs": {
            "size": "200x200 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Коричневый", "type": "Одиночный вентилятор",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "SSO2 Bearing (Noctua)",
            "noise_level": 18, "max_speed": 800, "airflow": 140
        }
    },
    {
        "title": "be quiet! Silent Wings 3 180mm",
        "price": 2990, "brand": "be quiet!",
        "info": "180-мм вентилятор для больших корпусов с отличным соотношением шум/поток.",
        "specs": {
            "size": "180x180 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "3-pin", "color": "Чёрный", "type": "Одиночный вентилятор",
            "speed_control": "Автоматическая (DC/voltage)", "bearing_type": "Гидродинамический (FDB / HDB)",
            "noise_level": 22, "max_speed": 700, "airflow": 115
        }
    },

    # === СЕРВЕРНЫЕ / ВЫСОКОПРОИЗВОДИТЕЛЬНЫЕ ===
    {
        "title": "Noctua NF-A14 industrialPPC-IP67",
        "price": 4990, "brand": "Noctua",
        "info": "Промышленный вентилятор с защитой IP67 для серверных решений.",
        "specs": {
            "size": "140x140 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Серый", "type": "Серверный вентилятор",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "Двойной шарикоподшипник (Dual Ball)",
            "noise_level": 38, "max_speed": 3000, "airflow": 140
        }
    },
    {
        "title": "Delta AFC1212DE 120mm 3800 RPM",
        "price": 2490, "brand": "Delta",
        "info": "Промышленный вентилятор с экстремально высокими оборотами для серверов.",
        "specs": {
            "size": "120x120 мм", "lighting": "Без подсветки", "fan_count": "1",
            "power_connector": "3-pin", "color": "Чёрный", "type": "Промышленный вентилятор",
            "speed_control": "Автоматическая (DC/voltage)", "bearing_type": "Двойной шарикоподшипник (Dual Ball)",
            "noise_level": 50, "max_speed": 3800, "airflow": 150
        }
    },

    # === С RGB ПОДСВЕТКОЙ ===
    {
        "title": "Corsair iCUE AF120 RGB ELITE 3-Pack",
        "price": 5990, "brand": "Corsair",
        "info": "Флагманские RGB вентиляторы с 34 адресуемыми светодиодами каждый.",
        "specs": {
            "size": "120x120 мм", "lighting": "ARGB (5V 3-pin)", "fan_count": "3",
            "power_connector": "4-pin PWM", "color": "Чёрный", "type": "Комплект вентиляторов",
            "speed_control": "Программная (через ПО)", "bearing_type": "Гидродинамический (FDB / HDB)",
            "noise_level": 25, "max_speed": 1800, "airflow": 60
        }
    },
    {
        "title": "Thermaltake Toughfan 12 Turbo ARGB",
        "price": 2790, "brand": "Thermaltake",
        "info": "Мощный ARGB вентилятор с высоким статическим давлением для радиаторов.",
        "specs": {
            "size": "120x120 мм", "lighting": "ARGB (5V 3-pin)", "fan_count": "1",
            "power_connector": "4-pin PWM", "color": "Прозрачный", "type": "Вентилятор для радиатора",
            "speed_control": "Автоматическая (PWM)", "bearing_type": "Гидродинамический (FDB / HDB)",
            "noise_level": 27, "max_speed": 2000, "airflow": 62
        }
    },
    {
        "title": "NZXT F120 RGB Core (3-Pack)",
        "price": 4490, "brand": "NZXT",
        "info": "Комплект из 3 вентиляторов NZXT с управлением через CAM.",
        "specs": {
            "size": "120x120 мм", "lighting": "ARGB (5V 3-pin)", "fan_count": "3",
            "power_connector": "4-pin PWM", "color": "Белый", "type": "Комплект вентиляторов",
            "speed_control": "Программная (через ПО)", "bearing_type": "Гидродинамический (FDB / HDB)",
            "noise_level": 24, "max_speed": 1800, "airflow": 58
        }
    },
]

# ==========================================
# КУЛЕРЫ (15 товаров)
# ==========================================
REALISTIC_COOLERS = [
    # === TOP-TIER БИТАШЕННЫЕ ===
    {
        "title": "Noctua NH-D15 chromax.black",
        "price": 10990, "brand": "Noctua",
        "info": "Легендарный двухбашенный кулер с двумя вентиляторами NF-A15. Один из лучших на рынке.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 250,
            "construction_type": "Двухбашенный (Dual Tower)", "heatpipes": "6",
            "height": 160, "rgb_type": "Без подсветки", "fan_sizes": "2x 140 мм",
            "fan_count": "2", "noise_level": 24, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },
    {
        "title": "be quiet! Dark Rock Pro 4",
        "price": 8990, "brand": "be quiet!",
        "info": "Двухбашенный кулер с тихим вентилятором Silent Wings и черной керамической отделкой.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 250,
            "construction_type": "Двухбашенный (Dual Tower)", "heatpipes": "6",
            "height": 163, "rgb_type": "Без подсветки", "fan_sizes": "120 мм, 135 мм",
            "fan_count": "2", "noise_level": 24, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },
    {
        "title": "DeepCool AK620",
        "price": 5990, "brand": "DeepCool",
        "info": "Двухбашенный кулер с 6 тепловыми трубками и двумя 120-мм вентиляторами.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 260,
            "construction_type": "Двухбашенный (Dual Tower)", "heatpipes": "6",
            "height": 160, "rgb_type": "Без подсветки", "fan_sizes": "2x 120 мм",
            "fan_count": "2", "noise_level": 28, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },

    # === ОДНОБАШЕННЫЕ TOP ===
    {
        "title": "Noctua NH-U12S redux",
        "price": 5490, "brand": "Noctua",
        "info": "Компактный однобашенный кулер с вентилятором NF-F12 и универсальной совместимостью.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 150,
            "construction_type": "Башенный (Single Tower)", "heatpipes": "4",
            "height": 155, "rgb_type": "Без подсветки", "fan_sizes": "120 мм",
            "fan_count": "1", "noise_level": 22, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },
    {
        "title": "be quiet! Pure Rock 2",
        "price": 3490, "brand": "be quiet!",
        "info": "Популярный кулер среднего класса с вентилятором Pure Wings 2.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 150,
            "construction_type": "Башенный (Single Tower)", "heatpipes": "4",
            "height": 155, "rgb_type": "Без подсветки", "fan_sizes": "120 мм",
            "fan_count": "1", "noise_level": 27, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },
    {
        "title": "DeepCool AK400",
        "price": 2990, "brand": "DeepCool",
        "info": "Компактный и эффективный кулер для процессоров до 220W TDP.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 220,
            "construction_type": "Башенный (Single Tower)", "heatpipes": "4",
            "height": 155, "rgb_type": "Без подсветки", "fan_sizes": "120 мм",
            "fan_count": "1", "noise_level": 27, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },

    # === С ARGB ПОДСВЕТКОЙ ===
    {
        "title": "DeepCool AK620 DIGITAL",
        "price": 6990, "brand": "DeepCool",
        "info": "Двухбашенный кулер с цифровым дисплеем температуры на верхней панели.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 260,
            "construction_type": "Двухбашенный (Dual Tower)", "heatpipes": "6",
            "height": 160, "rgb_type": "Статичная LED (однотонная)", "fan_sizes": "2x 120 мм",
            "fan_count": "2", "noise_level": 28, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },
    {
        "title": "Thermalright Peerless Assassin 120 SE ARGB",
        "price": 4490, "brand": "Thermalright",
        "info": "Кулер-убийца флагманов с ARGB подсветкой и двумя башнями.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 260,
            "construction_type": "Двухбашенный (Dual Tower)", "heatpipes": "6",
            "height": 155, "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "2x 120 мм",
            "fan_count": "2", "noise_level": 27, "fan_connector": "ARGB (5V 3-pin)",
            "speed_control": "Автоматическая (PWM)"
        }
    },
    {
        "title": "Corsair iCUE H100i Elite CAPELLIX XT",
        "price": 8990, "brand": "Corsair",
        "info": "Топовый кулер с 33 светодиодами CAPELLIX и управлением через iCUE.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 200,
            "construction_type": "Башенный (Single Tower)", "heatpipes": "5",
            "height": 158, "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "140 мм",
            "fan_count": "1", "noise_level": 26, "fan_connector": "ARGB (5V 3-pin)",
            "speed_control": "Программная (через ПО)"
        }
    },

    # === LOW PROFILE / КОМПАКТНЫЕ ===
    {
        "title": "Noctua NH-L9i",
        "price": 4490, "brand": "Noctua",
        "info": "Низкопрофильный кулер высотой всего 37 мм для компактных корпусов Mini-ITX.",
        "specs": {
            "socket": "LGA1700", "tdp_rating": 65,
            "construction_type": "Низкопрофильный (Low Profile)", "heatpipes": "4",
            "height": 37, "rgb_type": "Без подсветки", "fan_sizes": "92 мм",
            "fan_count": "1", "noise_level": 23, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },
    {
        "title": "be quiet! Shadow Rock LP",
        "price": 2990, "brand": "be quiet!",
        "info": "Компактный кулер высотой 72 мм с медным основанием.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 130,
            "construction_type": "Низкопрофильный (Low Profile)", "heatpipes": "4",
            "height": 72, "rgb_type": "Без подсветки", "fan_sizes": "120 мм",
            "fan_count": "1", "noise_level": 26, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },

    # === ПАССИВНЫЕ ===
    {
        "title": "Noctua NH-P1",
        "price": 8990, "brand": "Noctua",
        "info": "Полностью пассивный кулер без вентиляторов для абсолютно бесшумных систем.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 95,
            "construction_type": "Пассивный (без вентиляторов)", "heatpipes": "6",
            "height": 158, "rgb_type": "Без подсветки", "fan_sizes": "Вентиляторы не прилагаются",
            "fan_count": "0", "noise_level": 10, "fan_connector": "4-pin PWM",
            "speed_control": "Нет (фиксированная скорость)"
        }
    },

    # === СУПЕР-БАШНЯ ===
    {
        "title": "Phanteks PH-TC14P",
        "price": 6990, "brand": "Phanteks",
        "info": "Супербашня с тремя 140-мм вентиляторами для экстремального охлаждения.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 300,
            "construction_type": "Супер-башня (3+ вентилятора)", "heatpipes": "8",
            "height": 178, "rgb_type": "Без подсветки", "fan_sizes": "3x 140 мм",
            "fan_count": "3", "noise_level": 26, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },

    # === ТОП-ХИТЫ ===
    {
        "title": "Thermalright Peerless Assassin 120 SE",
        "price": 3490, "brand": "Thermalright",
        "info": "Народный кулер #1 — соотношение цена/производительность вне конкуренции.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 260,
            "construction_type": "Двухбашенный (Dual Tower)", "heatpipes": "6",
            "height": 155, "rgb_type": "Без подсветки", "fan_sizes": "2x 120 мм",
            "fan_count": "2", "noise_level": 27, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },
    {
        "title": "ID-Cooling SE-224-XTS",
        "price": 1990, "brand": "ID-Cooling",
        "info": "Бюджетный кулер с 4 тепловыми трубками для процессоров до 180W.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "tdp_rating": 180,
            "construction_type": "Башенный (Single Tower)", "heatpipes": "4",
            "height": 153, "rgb_type": "Без подсветки", "fan_sizes": "120 мм",
            "fan_count": "1", "noise_level": 27, "fan_connector": "4-pin PWM",
            "speed_control": "Автоматическая (PWM)"
        }
    },
]

# ==========================================
# СЖО / AIO (12 товаров)
# ==========================================
REALISTIC_AIO = [
    # === ФЛАГМАНСКИЕ 360mm ===
    {
        "title": "NZXT Kraken Elite 360 RGB",
        "price": 24990, "brand": "NZXT",
        "info": "Флагманская СЖО с цветным IPS дисплеем на помпе и управлением через CAM.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "3",
            "radiator_size": "360 мм (3 секции)", "color": "Чёрный",
            "lcd_display": "Есть (цветной IPS)", "tdp_rating": 350,
            "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "3x 120 мм",
            "maintenance_type": "Нет (AIO — необслуживаемая, готовая)",
            "noise_level": 28, "pump_connector": "USB 2.0 (для RGB/дисплея)"
        }
    },
    {
        "title": "Corsair iCUE H150i ELITE CAPELLIX XT",
        "price": 22990, "brand": "Corsair",
        "info": "Премиальная 360-мм СЖО с 33 светодиодами CAPELLIX и насосом с нулевой задержкой.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "3",
            "radiator_size": "360 мм (3 секции)", "color": "Чёрный",
            "lcd_display": "Нет", "tdp_rating": 400,
            "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "3x 140 мм",
            "maintenance_type": "Нет (AIO — необслуживаемая, готовая)",
            "noise_level": 25, "pump_connector": "USB 2.0 (для RGB/дисплея)"
        }
    },
    {
        "title": "Arctic Liquid Freezer III 360 A-RGB",
        "price": 16990, "brand": "Arctic",
        "info": "СЖО с уникальным VRM-вентилятором на помпе для охлаждения зоны питания процессора.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "3",
            "radiator_size": "360 мм (3 секции)", "color": "Чёрный",
            "lcd_display": "Нет", "tdp_rating": 350,
            "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "3x 120 мм",
            "maintenance_type": "Нет (AIO — необслуживаемая, готовая)",
            "noise_level": 23, "pump_connector": "4-pin PWM"
        }
    },

    # === ТОПОВЫЕ 240mm ===
    {
        "title": "Lian Li Galahad II LCD 240",
        "price": 19990, "brand": "Lian Li",
        "info": "СЖО с LCD дисплеем 2.1 дюйма на помпе для отображения GIF и телеметрии.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "2",
            "radiator_size": "240 мм (2 секции)", "color": "Чёрный",
            "lcd_display": "Есть (квадратный, 2.1\")", "tdp_rating": 300,
            "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "2x 120 мм",
            "maintenance_type": "Нет (AIO — необслуживаемая, готовая)",
            "noise_level": 26, "pump_connector": "USB 2.0 (для RGB/дисплея)"
        }
    },
    {
        "title": "be quiet! Silent Loop 2 280mm",
        "price": 15990, "brand": "be quiet!",
        "info": "Тихая 280-мм СЖО с вентиляторами Silent Wings 2 и керамическим насосом.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "2",
            "radiator_size": "280 мм", "color": "Чёрный",
            "lcd_display": "Нет", "tdp_rating": 320,
            "rgb_type": "Без подсветки", "fan_sizes": "2x 140 мм",
            "maintenance_type": "Полуобслуживаемая (дозаправка без замены контура)",
            "noise_level": 22, "pump_connector": "3-pin DC"
        }
    },
    {
        "title": "DeepCool LT720",
        "price": 14990, "brand": "DeepCool",
        "info": "Мощная 360-мм СЖО с зеркальной верхней панелью и RGB подсветкой.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "3",
            "radiator_size": "360 мм (3 секции)", "color": "Чёрный",
            "lcd_display": "Нет", "tdp_rating": 350,
            "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "3x 120 мм",
            "maintenance_type": "Нет (AIO — необслуживаемая, готовая)",
            "noise_level": 27, "pump_connector": "4-pin PWM"
        }
    },

    # === 120mm / КОМПАКТНЫЕ ===
    {
        "title": "Corsair iCUE H100i RGB ELITE",
        "price": 11990, "brand": "Corsair",
        "info": "Классическая 240-мм СЖО с отличной производительностью и управлением iCUE.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "2",
            "radiator_size": "240 мм (2 секции)", "color": "Чёрный",
            "lcd_display": "Нет", "tdp_rating": 280,
            "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "2x 120 мм",
            "maintenance_type": "Нет (AIO — необслуживаемая, готовая)",
            "noise_level": 25, "pump_connector": "USB 2.0 (для RGB/дисплея)"
        }
    },
    {
        "title": "NZXT Kraken X53 RGB 240mm",
        "price": 12990, "brand": "NZXT",
        "info": "СЖО с вращающимся RGB кольцом Infinium вокруг помпы.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "2",
            "radiator_size": "240 мм (2 секции)", "color": "Белый",
            "lcd_display": "Есть (монохромный)", "tdp_rating": 250,
            "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "2x 120 мм",
            "maintenance_type": "Нет (AIO — необслуживаемая, готовая)",
            "noise_level": 26, "pump_connector": "USB 2.0 (для RGB/дисплея)"
        }
    },

    # === БЮДЖЕТНЫЕ ===
    {
        "title": "DeepCool LE520",
        "price": 6990, "brand": "DeepCool",
        "info": "Доступная 240-мм СЖО с ARGB вентиляторами и зеркальной помпой.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "2",
            "radiator_size": "240 мм (2 секции)", "color": "Чёрный",
            "lcd_display": "Нет", "tdp_rating": 240,
            "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "2x 120 мм",
            "maintenance_type": "Нет (AIO — необслуживаемая, готовая)",
            "noise_level": 28, "pump_connector": "4-pin PWM"
        }
    },
    {
        "title": "ID-Cooling ZOOMFLOW 240 ARGB",
        "price": 5990, "brand": "ID-Cooling",
        "info": "Бюджетная 240-мм СЖО с ARGB подсветкой помпы и вентиляторов.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "2",
            "radiator_size": "240 мм (2 секции)", "color": "Чёрный",
            "lcd_display": "Нет", "tdp_rating": 220,
            "rgb_type": "ARGB (5V 3-pin)", "fan_sizes": "2x 120 мм",
            "maintenance_type": "Нет (AIO — необслуживаемая, готовая)",
            "noise_level": 29, "pump_connector": "4-pin PWM"
        }
    },

    # === CUSTOM LOOP / ЭНТУЗИАСТСКИЕ ===
    {
        "title": "EK-Loop Kinetic 240",
        "price": 34990, "brand": "EK Water Blocks",
        "info": "Премиальная СЖО для кастомных контуров с помпой EK-Loop и радиатором 240.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "2",
            "radiator_size": "240 мм (2 секции)", "color": "Прозрачный",
            "lcd_display": "Нет", "tdp_rating": 400,
            "rgb_type": "Без подсветки", "fan_sizes": "2x 120 мм",
            "maintenance_type": "Да (Custom Loop — пользовательская сборка)",
            "noise_level": 25, "pump_connector": "SATA (питание) + 3-pin/4-pin (управление)"
        }
    },
    {
        "title": "Alphacool Eisbaer 240 Pro",
        "price": 29990, "brand": "Alphacool",
        "info": "Разборная СЖО с возможностью замены жидкости и подключения доп. радиаторов.",
        "specs": {
            "socket": "Универсальный (мульти-сокет)", "fan_count": "2",
            "radiator_size": "240 мм (2 секции)", "color": "Чёрный",
            "lcd_display": "Нет", "tdp_rating": 350,
            "rgb_type": "Без подсветки", "fan_sizes": "2x 120 мм",
            "maintenance_type": "Да (Custom Loop — пользовательская сборка)",
            "noise_level": 24, "pump_connector": "4-pin PWM"
        }
    },
]


def seed_cooling():
    print("🚀 Начинаю создание товаров категории Охлаждение...")

    # === ВЕНТИЛЯТОРЫ ===
    print("\n=== ВЕНТИЛЯТОРЫ ===")
    created_fans = 0
    for item in REALISTIC_FANS:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"⏭️  Пропуск: {item['title']}")
            continue

        warranty_map = {
            "Noctua": "72 месяца",
            "be quiet!": "36 месяцев",
            "Corsair": "24 месяца",
            "Lian Li": "12 месяцев",
            "Arctic": "72 месяца",
            "DeepCool": "36 месяцев",
            "Zalman": "12 месяцев",
            "NZXT": "24 месяца",
            "Thermaltake": "24 месяца",
            "Delta": "12 месяцев",
        }

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(5, 100),
            warranty=warranty_map.get(item["brand"], "24 месяца")
        )
        p.categories.add(fans_cat)
        created_fans += 1
        print(f"✅ {p.title} | {item['specs']['size']} | {item['price']} ₽")

    print(f"\n🎉 Вентиляторы: добавлено {created_fans}")

    # === КУЛЕРЫ ===
    print("\n=== КУЛЕРЫ ===")
    created_coolers = 0
    for item in REALISTIC_COOLERS:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"️  Пропуск: {item['title']}")
            continue

        warranty_map = {
            "Noctua": "72 месяца",
            "be quiet!": "36 месяцев",
            "DeepCool": "36 месяцев",
            "Thermalright": "36 месяцев",
            "Corsair": "60 месяцев",
            "Phanteks": "60 месяцев",
            "Thermalright": "36 месяцев",
            "ID-Cooling": "24 месяца",
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
        p.categories.add(coolers_cat)
        created_coolers += 1
        print(
            f"✅ {p.title} | {item['specs']['construction_type']} | {item['specs']['tdp_rating']}W TDP | {item['price']} ₽")

    print(f"\n🎉 Кулеры: добавлено {created_coolers}")

    # === СЖО ===
    print("\n=== СЖО ===")
    created_aio = 0
    for item in REALISTIC_AIO:
        if Product.objects.filter(title=item["title"]).exists():
            print(f"⏭️  Пропуск: {item['title']}")
            continue

        warranty_map = {
            "NZXT": "72 месяца",
            "Corsair": "60 месяцев",
            "Arctic": "72 месяца",
            "Lian Li": "24 месяца",
            "be quiet!": "36 месяцев",
            "DeepCool": "36 месяцев",
            "ID-Cooling": "24 месяца",
            "EK Water Blocks": "24 месяца",
            "Alphacool": "24 месяца",
        }

        p = Product.objects.create(
            title=item["title"],
            price=item["price"],
            brand=item["brand"],
            info=item["info"],
            specifications=item["specs"],
            is_active=True,
            in_stock=random.randint(2, 30),
            warranty=warranty_map.get(item["brand"], "36 месяцев")
        )
        p.categories.add(aio_cat)
        created_aio += 1
        print(
            f"✅ {p.title} | {item['specs']['radiator_size']} | {item['specs']['tdp_rating']}W TDP | {item['price']} ₽")

    print(f"\n🎉 СЖО: добавлено {created_aio}")

    print(f"\n{'=' * 50}")
    print(f"🏆 ИТОГО: вентиляторы={created_fans}, кулеры={created_coolers}, СЖО={created_aio}")
    print(f"🏆 ВСЕГО: {created_fans + created_coolers + created_aio} товаров")


if __name__ == '__main__':
    seed_cooling()