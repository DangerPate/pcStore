

FILTERS_CONFIG = {

    'gpu': {
        'gpu_model': {
            'label': 'Графический процессор',
            'type': 'select',
            'options': [

                'GeForce RTX 5090', 'GeForce RTX 5080', 'GeForce RTX 5070 Ti', 'GeForce RTX 5070',
                'GeForce RTX 4090', 'GeForce RTX 4080 SUPER', 'GeForce RTX 4080', 'GeForce RTX 4070 Ti SUPER',
                'GeForce RTX 4070 Ti', 'GeForce RTX 4070 SUPER', 'GeForce RTX 4070', 'GeForce RTX 4060 Ti',
                'GeForce RTX 4060', 'GeForce RTX 3090 Ti', 'GeForce RTX 3090', 'GeForce RTX 3080 Ti',
                'GeForce RTX 3080', 'GeForce RTX 3070 Ti', 'GeForce RTX 3070', 'GeForce RTX 3060 Ti',
                'GeForce RTX 3060', 'GeForce RTX 3050', 'GeForce RTX 2080 Ti', 'GeForce RTX 2080 SUPER',
                'GeForce RTX 2080', 'GeForce RTX 2070 SUPER', 'GeForce RTX 2070', 'GeForce RTX 2060 SUPER',
                'GeForce RTX 2060', 'GeForce GTX 1660 Ti', 'GeForce GTX 1660 SUPER', 'GeForce GTX 1660',
                'GeForce GTX 1650 SUPER', 'GeForce GTX 1650', 'GeForce GTX 1080 Ti', 'GeForce GTX 1080',
                'GeForce GTX 1070 Ti', 'GeForce GTX 1070', 'GeForce GTX 1060', 'GeForce GTX 1050 Ti',
                'GeForce GTX 1050', 'GeForce GT 1030', 'GeForce GT 710',

                'Radeon RX 9070 XT', 'Radeon RX 9070', 'Radeon RX 7900 XTX', 'Radeon RX 7900 XT',
                'Radeon RX 7900 GRE', 'Radeon RX 7800 XT', 'Radeon RX 7700 XT', 'Radeon RX 7600 XT',
                'Radeon RX 7600', 'Radeon RX 6950 XT', 'Radeon RX 6900 XT', 'Radeon RX 6800 XT',
                'Radeon RX 6800', 'Radeon RX 6750 XT', 'Radeon RX 6700 XT', 'Radeon RX 6650 XT',
                'Radeon RX 6600 XT', 'Radeon RX 6600', 'Radeon RX 6500 XT', 'Radeon RX 6400',
                'Radeon RX 5700 XT', 'Radeon RX 5700', 'Radeon RX 5600 XT', 'Radeon RX 5500 XT',
                'Radeon RX Vega 64', 'Radeon RX Vega 56', 'Radeon RX 590', 'Radeon RX 580',
                'Radeon RX 570', 'Radeon RX 560', 'Radeon RX 480', 'Radeon RX 470', 'Radeon R9 390X',
                'Radeon R9 290X', 'Radeon R7 370', 'Radeon HD 7970',

                'Intel Arc A770', 'Intel Arc A750', 'Intel Arc A580', 'Intel Arc A380', 'Intel Arc A310'
            ],
        },
        'vram': {
            'label': 'Объём видеопамяти',
            'type': 'select',
            'options': ['1 ГБ', '2 ГБ', '3 ГБ', '4 ГБ', '5 ГБ', '6 ГБ', '8 ГБ', '10 ГБ', '11 ГБ', '12 ГБ', '16 ГБ', '20 ГБ', '24 ГБ', '32 ГБ', '48 ГБ', '64 ГБ', '80 ГБ', '96 ГБ'],
        },
        'gpu_vendor': {
            'label': 'Производитель GPU',
            'type': 'select',
            'options': ['NVIDIA', 'AMD', 'Intel'],
        },
        'purpose': {
            'label': 'Назначение',
            'type': 'select',
            'options': ['Игровая', 'Для офиса и дома', 'Для работы, рендеринга и монтажа', 'Для майнинга и вычислений', 'Серверная / Дата-центр', 'Универсальная'],
        },
        'memory_bus': {
            'label': 'Разрядность шины памяти',
            'type': 'select',
            'options': ['64 бит', '96 бит', '128 бит', '160 бит', '192 бит', '256 бит', '320 бит', '384 бит', '448 бит', '512 бит', '6144 бит (HBM)'],
        },
        'interface': {
            'label': 'Интерфейс подключения',
            'type': 'select',
            'options': ['PCIe 1.0 x16', 'PCIe 2.0 x16', 'PCIe 3.0 x16', 'PCIe 4.0 x16', 'PCIe 5.0 x16', 'AGP 8x', 'PCI'],
        },
        'cooling': {
            'label': 'Тип и количество вентиляторов',
            'type': 'select',
            'options': ['1 осевой', '2 осевых', '3 осевых', '1 центробежный (турбина)', 'Пассивное (без вентиляторов)', 'СЖО (водяное охлаждение)', 'Гибридное'],
        },
        'memory_type': {
            'label': 'Тип памяти',
            'type': 'select',
            'options': ['GDDR2', 'GDDR3', 'GDDR4', 'GDDR5', 'GDDR5X', 'GDDR6', 'GDDR6X', 'GDDR7', 'DDR3', 'DDR4', 'HBM', 'HBM2', 'HBM2e', 'HBM3'],
        },
        'gpu_series': {
            'label': 'Линейка графических процессоров',
            'type': 'select',
            'options': [
                'NVIDIA GeForce RTX 50', 'NVIDIA GeForce RTX 40', 'NVIDIA GeForce RTX 30',
                'NVIDIA GeForce RTX 20', 'NVIDIA GeForce GTX 16', 'NVIDIA GeForce GTX 10',
                'NVIDIA GeForce GTX 900/700', 'NVIDIA Quadro / RTX A-series',
                'AMD Radeon RX 9000', 'AMD Radeon RX 7000', 'AMD Radeon RX 6000',
                'AMD Radeon RX 5000', 'AMD Radeon RX 500/400', 'AMD Radeon R9/R7',
                'Intel Arc A700', 'Intel Arc A500/A300'
            ],
        },
        'color': {
            'label': 'Цвет',
            'type': 'select',
            'options': ['Черный', 'Белый', 'Серый / Серебристый', 'Красный', 'Синий', 'Зелёный', 'RGB-подсветка', 'Многоцветный / Кастом', 'Без кожуха (Reference/Open-air)'],
        },
        'length': {
            'label': 'Длина видеокарты',
            'type': 'select',
            'options': ['до 150 мм', '150–199 мм', '200–249 мм', '250–299 мм', '300–349 мм', '350–399 мм', 'от 400 мм'],
        },
    },

    'cpu': {
        'socket': {
            'label': 'Сокет',
            'type': 'select',
            'options': [
                'LGA1851', 'LGA1700', 'LGA1200', 'LGA1151', 'LGA1150', 'LGA1155', 'LGA1156', 'LGA2066', 'LGA3647',
                'LGA4189', 'LGA4677',
                'AM5', 'AM4', 'AM3+', 'AM3', 'AM2+', 'FM2+', 'FM2', 'TR5', 'sTR5', 'TR4', 'sTRX4', 'sWRX8', 'SP3', 'SP5'
            ]
        },
        'family': {
            'label': 'Семейство процессоров',
            'type': 'select',
            'options': [
                'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'Intel Core i9',
                'Intel Pentium', 'Intel Celeron', 'Intel Xeon', 'Intel Core Ultra',
                'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7', 'AMD Ryzen 9',
                'AMD Athlon', 'AMD EPYC', 'AMD Ryzen Threadripper'
            ]
        },
        'perf_cores': {
            'label': 'Количество производительных ядер',
            'type': 'select',
            'options': ['2', '4', '6', '8', '10', '12', '14', '16', '20', '24', '32', '40', '48', '64', '96', '128']
        },
        'generation': {
            'label': 'Поколение процессоров',
            'type': 'select',
            'options': [
                'Intel 14-e поколение', 'Intel 13-e поколение', 'Intel 12-e поколение', 'Intel 11-e поколение',
                'Intel 10-e поколение',
                'Intel Core Ultra (Series 1)', 'Intel Core Ultra (Series 2)',
                'AMD Ryzen 9000', 'AMD Ryzen 8000', 'AMD Ryzen 7000', 'AMD Ryzen 5000', 'AMD Ryzen 4000',
                'AMD Ryzen 3000', 'AMD Ryzen 2000', 'AMD Ryzen 1000',
                'AMD Threadripper 7000', 'AMD Threadripper 5000', 'AMD EPYC 9004', 'AMD EPYC 7003'
            ]
        },
        'igpu': {
            'label': 'Интегрированное графическое ядро',
            'type': 'select',
            'options': ['Есть', 'Нет']
        },
        'memory_type': {
            'label': 'Поддерживаемый тип памяти',
            'type': 'select',
            'options': ['DDR2', 'DDR3', 'DDR4', 'DDR5', 'LPDDR4', 'LPDDR5']
        },
        'purpose': {
            'label': 'Назначение',
            'type': 'select',
            'options': ['Игровой', 'Для офиса и дома', 'Для рабочих станций', 'Для серверов и дата-центров',
                        'Для рендеринга и монтажа', 'Универсальный']
        },
        'packaging': {
            'label': 'Тип поставки',
            'type': 'select',
            'options': ['BOX (розничная)', 'OEM (Tray / лоток)', 'Bulk (навалом)']
        },
        'base_clock': {
            'label': 'Номинальная частота (ГГц)',
            'type': 'range',
            'min': 0.8,
            'max': 6.0,
            'step': 0.1
        },
        'turbo_clock': {
            'label': 'Частота в турбо-режиме (ГГц)',
            'type': 'range',
            'min': 0.0,
            'max': 7.0,
            'step': 0.1
        },
        'tdp': {
            'label': 'Тепловыделение TDP (Вт)',
            'type': 'range',
            'min': 5,
            'max': 400,
            'step': 5
        }
    },

    'motherboard': {
        'socket': {
            'label': 'Сокет',
            'type': 'select',
            'options': [
                'LGA1851', 'LGA1700', 'LGA1200', 'LGA1151', 'LGA1155', 'LGA2066', 'LGA3647', 'LGA4189', 'LGA4677',
                'AM5', 'AM4', 'AM3+', 'TR5 (sTR5)', 'sWRX8', 'SP3', 'SP5', 'sTRX4'
            ]
        },
        'memory_type': {
            'label': 'Тип поддерживаемой памяти',
            'type': 'select',
            'options': ['DDR5', 'DDR4', 'DDR3', 'ECC DDR5', 'ECC DDR4', 'LPDDR5', 'CXL Memory']
        },
        'form_factor': {
            'label': 'Форм-фактор',
            'type': 'select',
            'options': ['ATX', 'Micro-ATX (mATX)', 'Mini-ITX', 'E-ATX', 'XL-ATX', 'SSI-EEB', 'SSI-CEB', 'Mini-DTX',
                        'Proprietary']
        },
        'chipset': {
            'label': 'Чипсет',
            'type': 'select',
            'options': [
                'Intel Z890', 'Intel B860', 'Intel H810', 'Intel Z790', 'Intel B760', 'Intel H770', 'Intel H610',
                'Intel Z690', 'Intel B660', 'Intel W790',
                'AMD X870E', 'AMD X870', 'AMD B850', 'AMD B650E', 'AMD B650', 'AMD A620', 'AMD X570', 'AMD B550',
                'AMD A520', 'AMD TRX50', 'AMD WRX80'
            ]
        },
        'pcie_version': {
            'label': 'Версия PCI Express',
            'type': 'select',
            'options': ['PCIe 5.0', 'PCIe 4.0', 'PCIe 3.0', 'PCIe 2.0']
        },
        'ram_slots': {
            'label': 'Количество слотов памяти',
            'type': 'select',
            'options': ['2', '4', '6', '8', '12', '16', '24', '32']
        },
        'cpu_support': {
            'label': 'Платформа процессора',
            'type': 'select',
            'options': ['Intel', 'AMD']
        },
        'm2_slots': {
            'label': 'Количество разъемов M.2',
            'type': 'select',
            'options': ['0', '1', '2', '3', '4', '5', '6', '8']
        },
        'wifi_std': {
            'label': 'Стандарт Wi-Fi',
            'type': 'select',
            'options': ['Нет Wi-Fi', 'Wi-Fi 5 (802.11ac)', 'Wi-Fi 6 (802.11ax)', 'Wi-Fi 6E', 'Wi-Fi 7 (802.11be)']
        }
    },
    'ram': {
        'memory_type': {
            'label': 'Тип памяти',
            'type': 'select',
            'options': ['DDR3', 'DDR4', 'DDR5', 'DDR4 ECC', 'DDR5 ECC', 'SODIMM DDR3', 'SODIMM DDR4', 'SODIMM DDR5',
                        'SODIMM DDR5 ECC', 'LPDDR5']
        },
        'total_capacity': {
            'label': 'Суммарный объем комплекта',
            'type': 'select',
            'options': ['4 ГБ', '8 ГБ', '16 ГБ', '32 ГБ', '48 ГБ', '64 ГБ', '96 ГБ', '128 ГБ', '192 ГБ', '256 ГБ',
                        '512 ГБ', '1 ТБ', '2 ТБ']
        },
        'module_capacity': {
            'label': 'Объем одного модуля',
            'type': 'select',
            'options': ['4 ГБ', '8 ГБ', '16 ГБ', '24 ГБ', '32 ГБ', '48 ГБ', '64 ГБ', '96 ГБ', '128 ГБ']
        },
        'frequency': {
            'label': 'Тактовая частота (МГц)',
            'type': 'select',
            'options': ['1333', '1600', '1866', '2133', '2400', '2666', '3000', '3200', '3600', '4000', '4400', '4800',
                        '5200', '5600', '6000', '6200', '6400', '6800', '7200', '7600', '8000', '8400', '8800']
        },
        'kit_size': {
            'label': 'Количество модулей в комплекте',
            'type': 'select',
            'options': ['1', '2', '4', '8']
        },
        'ram_purpose': {
            'label': 'Тип (назначение)',
            'type': 'select',
            'options': ['Desktop (UDIMM)', 'Laptop (SODIMM)', 'Server (RDIMM/LRDIMM)', 'Workstation (ECC UDIMM)']
        },
        'cas_latency': {
            'label': 'CAS Latency (CL)',
            'type': 'range',
            'min': 5,
            'max': 44,
            'step': 1
        },
        'heatsink': {
            'label': 'Наличие радиатора',
            'type': 'select',
            'options': ['Есть', 'Нет']
        }
    },
    'psu': {
        'wattage': {
            'label': 'Мощность (Вт)',
            'type': 'range',
            'min': 300,
            'max': 2000,
            'step': 50
        },
        'certification': {
            'label': 'Сертификат 80 PLUS / Cybenetics',
            'type': 'select',
            'options': [
                'Нет сертификата', '80 Plus Standard', '80 Plus White', '80 Plus Bronze',
                '80 Plus Silver', '80 Plus Gold', '80 Plus Platinum', '80 Plus Titanium',
                'Cybenetics Standard', 'Cybenetics Gold', 'Cybenetics Platinum', 'Cybenetics A+'
            ]
        },
        'modularity': {
            'label': 'Тип модульности',
            'type': 'select',
            'options': ['Немодульный', 'Полумодульный', 'Полностью модульный']
        },
        'form_factor': {
            'label': 'Форм-фактор',
            'type': 'select',
            'options': ['ATX', 'SFX', 'SFX-L', 'TFX', 'FlexATX', 'EPS 12V (Server)', 'SFX Gold']
        },

        'pci_e_connectors': {
            'label': 'Разъемы для видеокарты (PCI-E)',
            'type': 'select',
            'options': [
                '6-pin', '8-pin (6+2)', '2x 6-pin', '2x 8-pin (6+2)',
                '3x 8-pin (6+2)', '4x 8-pin (6+2)',
                '1x 16-pin (12V-2x6)', '2x 16-pin (12V-2x6)',
                '1x 12+4 pin (12VHPWR)', '2x 12+4 pin (12VHPWR)'
            ]
        },

        'atx_standard': {
            'label': 'Соответствие стандартам ATX',
            'type': 'select',
            'options': [
                'ATX 12V 1.3', 'ATX 12V 2.0', 'ATX 12V 2.03', 'ATX 12V 2.2',
                'ATX 12V 2.3', 'ATX 12V 2.31', 'ATX 12V 2.4', 'ATX 12V 2.5',
                'ATX 12V 2.51', 'ATX 12V 2.52', 'ATX 3.0', 'ATX 3.1',
                'EPS 12V'
            ]
        },
        'pfc': {
            'label': 'Корректор коэффициента мощности (PFC)',
            'type': 'select',
            'options': ['Активный (Active PFC)', 'Пассивный (Passive PFC)', 'Без PFC']
        },

        'cpu_connectors': {
            'label': 'Разъемы для питания процессора',
            'type': 'select',
            'options': [
                '4-pin', '4+4 pin', '8-pin (4+4)', '8+4 pin', '8+8 pin', '2x 8-pin (4+4)'
            ]
        },
        'cable_sleeving': {
            'label': 'Оплетка проводов',
            'type': 'select',
            'options': ['В оплетке', 'Без оплетки', 'Красная/Цветная', 'Плоские кабели', 'Silicone Cables']
        }
    },

    'pc-case': {
        'mb_support': {
            'label': 'Форм-фактор совместимых плат',
            'type': 'select',
            'options': ['ATX', 'Micro-ATX (mATX)', 'Mini-ITX', 'E-ATX', 'SSI-EEB', 'SSI-CEB', 'XL-ATX', 'Mini-DTX',
                        'FlexATX', 'Proprietary']
        },
        'case_type': {
            'label': 'Типоразмер корпуса',
            'type': 'select',
            'options': ['Full Tower', 'Mid Tower', 'Mini Tower', 'Micro Tower', 'Small Form Factor (SFF)', 'Cube',
                        'HTPC', 'Open Frame / Open Case', 'Rackmount', 'Server Case']
        },
        'color': {
            'label': 'Основной цвет',
            'type': 'select',
            'options': ['Черный', 'Белый', 'Серебристый', 'Серый', 'Красный', 'Синий', 'Зеленый', 'Желтый', 'Розовый',
                        'RGB / Прозрачный', 'Дерево / Финиш под дерево', 'Матовый черный', 'Матовый белый']
        },
        'aquarium_style': {
            'label': 'Корпус-аквариум',
            'type': 'select',
            'options': ['Да', 'Нет']
        },
        'included_fans': {
            'label': 'Вентиляторы в комплекте',
            'type': 'select',
            'options': ['Без вентиляторов', '1 шт', '2 шт', '3 шт', '4 шт', '5 шт', '6 шт', '7+ шт']
        },
        'psu_location': {
            'label': 'Размещение блока питания',
            'type': 'select',
            'options': ['Снизу', 'Сверху']
        },
        'window_material': {
            'label': 'Материал окна',
            'type': 'select',
            'options': ['Закаленное стекло', 'Оргстекло (акрил)', 'Перфорация (Mesh)', 'Без окна']
        },
        'max_cooler_height': {
            'label': 'Макс. высота процессорного кулера (мм)',
            'type': 'range',
            'min': 50,
            'max': 200,
            'step': 5
        },
        'max_gpu_length': {
            'label': 'Макс. длина видеокарты (мм)',
            'type': 'range',
            'min': 150,
            'max': 500,
            'step': 10
        },
        'has_side_window': {
            'label': 'Наличие окна на боковой стенке',
            'type': 'select',
            'options': ['Есть', 'Нет']
        }
    },
    'case-fan': {
        'size': {
            'label': 'Размер вентилятора',
            'type': 'select',
            'options': [
                '40x40 мм', '50x50 мм', '60x60 мм', '70x70 мм',
                '80x80 мм', '92x92 мм', '120x120 мм', '140x140 мм',
                '180x180 мм', '200x200 мм', '220x220 мм', '230x230 мм',
                '250x250 мм', '280x280 мм', '360x360 мм'
            ],
        },
        'lighting': {
            'label': 'Тип подсветки',
            'type': 'select',
            'options': [
                'Без подсветки', 'ARGB (5V 3-pin)', 'RGB (12V 4-pin)',
                'Фиксированный цвет (LED)', 'Белая LED', 'Красная LED',
                'Синяя LED', 'Зелёная LED', 'UV (ультрафиолет)',
                'D-RGB (адресуемая)', 'Halo / кольцевая подсветка',
                'Боковая подсветка (edge-lit)'
            ],
        },
        'fan_count': {
            'label': 'Количество вентиляторов в комплекте',
            'type': 'select',
            'options': ['1', '2', '3', '4', '5', '6', 'Комплект (набор)'],
        },
        'power_connector': {
            'label': 'Тип разъёма питания',
            'type': 'select',
            'options': [
                '2-pin', '3-pin', '4-pin PWM', '3-pin + Molex',
                '4-pin PWM + Molex', 'Molex (только)', 'SATA (для контроллера)',
                'Комбинированный (3-pin/4-pin)', ' proprietary (фирменный)'
            ],
        },
        'color': {
            'label': 'Цвет',
            'type': 'select',
            'options': [
                'Чёрный', 'Белый', 'Серый', 'Прозрачный',
                'Дымчатый (smoke)', 'RGB-подсветка', 'ARGB-подсветка',
                'Красный', 'Синий', 'Зелёный', 'Жёлтый', 'Розовый',
                'Фиолетовый', 'Многоцветный'
            ],
        },
        'type': {
            'label': 'Тип',
            'type': 'select',
            'options': [
                'Одиночный вентилятор', 'Комплект вентиляторов',
                'Вентилятор для корпуса', 'Вентилятор для радиатора',
                'Вентилятор для блока питания', 'Серверный вентилятор',
                'Промышленный вентилятор', 'Вентилятор с рамкой',
                'Вентилятор без рамки (open-frame)', 'Турбинный вентилятор'
            ],
        },
        'speed_control': {
            'label': 'Регулировка оборотов',
            'type': 'select',
            'options': [
                'Нет (фиксированная скорость)', 'Ручная (резистор/кабель)',
                'Автоматическая (PWM)', 'Автоматическая (DC/voltage)',
                'PWM + DC (гибридная)', 'Через контроллер/хаб',
                'Через материнскую плату', 'Программная (через ПО)'
            ],
        },
        'bearing_type': {
            'label': 'Тип подшипника',
            'type': 'select',
            'options': [
                'Подшипник скольжения (Sleeve)', 'Подшипник качения (Ball)',
                'Гидродинамический (FDB / HDB)', 'Магнитно-levitation (MagLev)',
                'Двойной шарикоподшипник (Dual Ball)', 'Rifle Bearing',
                'SSO Bearing (Noctua)', 'SSO2 Bearing (Noctua)',
                'Rifle Bearing (Corsair)', 'Fluid Dynamic Bearing (FDB)',
                'Hydro Dynamic Bearing (HDB)', 'Rifle Bearing',
                'Ceramic Bearing', 'Направляющий подшипник (Rifle)'
            ],
        },
        'noise_level': {
            'label': 'Максимальный уровень шума (дБ)',
            'type': 'range',
            'min': 0,
            'max': 50,
            'step': 1,
        },
        'max_speed': {
            'label': 'Максимальная скорость вращения (об/мин)',
            'type': 'range',
            'min': 300,
            'max': 3000,
            'step': 50,
        },
        'airflow': {
            'label': 'Воздушный поток на максимальной скорости (CFM)',
            'type': 'range',
            'min': 10,
            'max': 150,
            'step': 5,
        },
    },
    'cpu-cooler': {
        'socket': {
            'label': 'Сокет процессора',
            'type': 'select',
            'options': [
                'LGA1851', 'LGA1700', 'LGA1200', 'LGA115x (1150/1151/1155)',
                'LGA2066', 'LGA3647', 'LGA4189',
                'AM5', 'AM4', 'AM3+', 'AM2+', 'FM2+',
                'TR5 (sTR5)', 'TR4 (sTRX4)', 'sWRX8', 'SP3', 'SP5',
                'Универсальный (мульти-сокет)'
            ],
        },
        'tdp_rating': {
            'label': 'Рассеиваемая мощность (TDP, Вт)',
            'type': 'range',
            'min': 50,
            'max': 400,
            'step': 5,
        },
        'construction_type': {
            'label': 'Тип конструкции',
            'type': 'select',
            'options': [
                'Башенный (Single Tower)', 'Двухбашенный (Dual Tower)',
                'Низкопрофильный (Low Profile)', 'Пассивный (без вентиляторов)',
                'Супер-башня (3+ вентилятора)', 'Top-Flow (горизонтальный)',
                'Компактный / Slim', 'С жидкометаллическим охлаждением'
            ],
        },
        'heatpipes': {
            'label': 'Количество тепловых трубок',
            'type': 'select',
            'options': [
                '0 (пассивный)', '2', '3', '4', '5', '6', '7', '8', '9', '10 и более'
            ],
        },
        'height': {
            'label': 'Высота кулера (мм)',
            'type': 'range',
            'min': 30,
            'max': 185,
            'step': 5,
        },
        'rgb_type': {
            'label': 'Тип подсветки',
            'type': 'select',
            'options': [
                'Без подсветки', 'Статичная LED (однотонная)',
                'ARGB (5V 3-pin)', 'RGB (12V 4-pin)',
                'Синхронизация с материнской платой', 'Адресуемая (Addressable RGB)',
                'Фиксированный цвет (красный, синий, белый)'
            ],
        },
        'fan_sizes': {
            'label': 'Размеры комплектных вентиляторов',
            'type': 'select',
            'options': [
                '80 мм', '92 мм', '102 мм', '120 мм', '135 мм', '140 мм',
                '2x 120 мм', '2x 140 мм', '3x 120 мм', '3x 140 мм',
                '1x 120 + 1x 140 мм', 'Вентиляторы не прилагаются'
            ],
        },
        'fan_count': {
            'label': 'Количество вентиляторов в комплекте',
            'type': 'select',
            'options': ['0', '1', '2', '3', '4', '5'],
        },
        'noise_level': {
            'label': 'Максимальный уровень шума (дБ)',
            'type': 'range',
            'min': 10,
            'max': 50,
            'step': 1,
        },
        'fan_connector': {
            'label': 'Разъем для подключения вентиляторов',
            'type': 'select',
            'options': [
                '3-pin DC', '4-pin PWM', 'ARGB (5V 3-pin)', 'RGB (12V 4-pin)',
                'Molex', 'Y-кабель (разветвитель)', 'Встроенный хаб/контроллер',
                'Комбинированный (PWM + RGB)'
            ],
        },
        'speed_control': {
            'label': 'Регулировка скорости вращения',
            'type': 'select',
            'options': [
                'Нет (фиксированная скорость)', 'Ручная (кабель-резистор)',
                'Автоматическая (PWM)', 'Автоматическая (DC / Voltage)',
                'Гибридная (PWM/DC)', 'Через материнскую плату',
                'Через внешний контроллер/хаб', 'Программная (через ПО)'
            ],
        },
    },
    'liquid-cooling': {
        'socket': {
            'label': 'Сокет процессора',
            'type': 'select',
            'options': [
                'LGA1851', 'LGA1700', 'LGA1200', 'LGA115x (1150/1151/1155)',
                'LGA2066', 'LGA3647', 'LGA4189',
                'AM5', 'AM4', 'AM3+', 'AM2+', 'FM2+',
                'TR5 (sTR5)', 'TR4 (sTRX4)', 'sWRX8', 'SP3', 'SP5',
                'Универсальный (мульти-сокет)'
            ],
        },
        'fan_count': {
            'label': 'Количество вентиляторов в комплекте',
            'type': 'select',
            'options': ['0', '1', '2', '3', '4', '5', '6'],
        },
        'radiator_size': {
            'label': 'Монтажный размер радиатора',
            'type': 'select',
            'options': [
                '120 мм (1 секция)', '180 мм', '240 мм (2 секции)',
                '280 мм', '360 мм (3 секции)', '420 мм', '480 мм (4 секции)',
                '560 мм', 'Custom (под заказ)'
            ],
        },
        'color': {
            'label': 'Цвет',
            'type': 'select',
            'options': [
                'Чёрный', 'Белый', 'Серебристый', 'Серый',
                'Чёрный / Белый', 'RGB-подсветка', 'Прозрачный',
                'Красный', 'Синий', 'Зелёный', 'Многоцветный'
            ],
        },
        'lcd_display': {
            'label': 'LCD дисплей',
            'type': 'select',
            'options': [
                'Нет', 'Есть (монохромный)', 'Есть (цветной IPS)',
                'Есть (круглый, 1.7")', 'Есть (квадратный, 2.1")',
                'Есть (сенсорный)', 'С поддержкой GIF/видео'
            ],
        },
        'tdp_rating': {
            'label': 'Рассеиваемая мощность (TDP, Вт)',
            'type': 'range',
            'min': 100,
            'max': 500,
            'step': 10,
        },
        'rgb_type': {
            'label': 'Тип подсветки',
            'type': 'select',
            'options': [
                'Без подсветки', 'Статичная LED (однотонная)',
                'ARGB (5V 3-pin)', 'RGB (12V 4-pin)',
                'Синхронизация с материнской платой (Aura Sync, Mystic Light, RGB Fusion и т.д.)',
                'Адресуемая (Addressable RGB)',
                'Фиксированный цвет (красный, синий, белый)',
                'Встроенный контроллер с пультом ДУ'
            ],
        },
        'fan_sizes': {
            'label': 'Размеры вентиляторов',
            'type': 'select',
            'options': [
                '120 мм', '140 мм', '180 мм', '240 мм', '280 мм',
                '2x 120 мм', '2x 140 мм', '3x 120 мм', '3x 140 мм',
                '4x 120 мм', '4x 140 мм', 'Вентиляторы не прилагаются'
            ],
        },
        'maintenance_type': {
            'label': 'Обслуживаемая СЖО',
            'type': 'select',
            'options': [
                'Нет (AIO — необслуживаемая, готовая)',
                'Да (Custom Loop — пользовательская сборка)',
                'Полуобслуживаемая (дозаправка без замены контура)'
            ],
        },
        'noise_level': {
            'label': 'Максимальный уровень шума (дБ)',
            'type': 'range',
            'min': 15,
            'max': 50,
            'step': 1,
        },
        'pump_connector': {
            'label': 'Разъем подключения помпы',
            'type': 'select',
            'options': [
                '3-pin DC', '4-pin PWM', 'SATA (питание) + 3-pin/4-pin (управление)',
                'Molex (только питание)', '2x 3-pin (Y-кабель)',
                'Встроенный хаб/контроллер', 'USB 2.0 (для RGB/дисплея)',
                ' proprietary (фирменный разъём)'
            ],
        },
    },
    'ssd-25': {
        'capacity': {
            'label': 'Объём накопителя (ГБ)',
            'type': 'range',
            'min': 60,
            'max': 8000,
            'step': 100,
        },
        'interface': {
            'label': 'Разъем подключения / Интерфейс',
            'type': 'select',
            'options': [
                'SATA III (6 Гбит/с)', 'SATA II (3 Гбит/с)',
                'SAS 12 Гбит/с', 'SAS 6 Гбит/с', 'U.2 (SFF-8639)'
            ],
        },
        'tbw': {
            'label': 'Максимальный ресурс записи (TBW, ТБ)',
            'type': 'range',
            'min': 30,
            'max': 144000,
            'step': 50,
        },
        'dram_cache': {
            'label': 'DRAM-буфер',
            'type': 'select',
            'options': [
                'Есть', 'Нет (DRAM-less)', 'HMB (Host Memory Buffer)',
                'SLC-кэширование (псевдо-SLC)'
            ],
        },
        'read_speed': {
            'label': 'Макс. скорость последовательного чтения (МБ/с)',
            'type': 'range',
            'min': 100,
            'max': 1100,
            'step': 10,
        },
        'nand_type': {
            'label': 'Количество бит на ячейку (Тип NAND)',
            'type': 'select',
            'options': [
                'SLC (1 бит)', 'MLC (2 бита)', '3D MLC (2 бита)',
                'TLC (3 бита)', '3D TLC (3 бита)',
                'QLC (4 бита)', '3D QLC (4 бита)', 'PLC (5 бит)'
            ],
        },
        'write_speed': {
            'label': 'Макс. скорость последовательной записи (МБ/с)',
            'type': 'range',
            'min': 50,
            'max': 1000,
            'step': 10,
        },
        'nand_structure': {
            'label': 'Структура памяти (Слоистость NAND)',
            'type': 'select',
            'options': [
                '2D NAND (Planar / плоская)', '3D NAND (до 64 слоев)',
                '3D NAND (96–128 слоев)', '3D NAND (144–176 слоев)',
                '3D NAND (232+ слоя)', 'Samsung V-NAND (4-5 поколение)',
                'Samsung V-NAND (6-7 поколение)', 'SK Hynix 4D NAND',
                'Micron 3D NAND (Gen3/Gen4)', 'Kioxia BiCS FLASH (5-6 поколение)'
            ],
        },
        'dwpd': {
            'label': 'DWPD (Drive Writes Per Day)',
            'type': 'select',
            'options': [
                'Не указано (Потребительский)', '0.3 (Read Intensive)',
                '1 (Mixed Use)', '3 (Write Intensive)', '10 (Endurance)'
            ],
        },
        'controller': {
            'label': 'Контроллер',
            'type': 'select',
            'options': [
                'Phison S11', 'Phison S12 / S12DC', 'Phison E12 / E12S',
                'Phison E16', 'Phison E18', 'Phison E21T', 'Phison E25 / E25T',
                'Phison E31T', 'Marvell 88SS1074', 'Marvell 88SS1372',
                'Silicon Motion SM2246', 'Silicon Motion SM2258 / SM2259',
                'Silicon Motion SM2262 / SM2263', 'Silicon Motion SM2267 / SM2267XT',
                'Silicon Motion SM2281', 'Samsung MJX / MKX / MEX',
                'WD / SanDisk (собственный)', 'Micron (собственный)',
                'Realtek RTS5763', 'Неизвестный / Другой'
            ],
        },
    },
    'ssd-m2': {
        'capacity': {
            'label': 'Объём накопителя (ГБ)',
            'type': 'range',
            'min': 64,
            'max': 8192,
            'step': 64,
        },
        'has_nvme': {
            'label': 'Поддержка NVMe',
            'type': 'select',
            'options': ['Да (NVMe)', 'Нет (SATA M.2)'],
        },
        'interface': {
            'label': 'Физический интерфейс',
            'type': 'select',
            'options': [
                'PCIe 3.0 x4', 'PCIe 4.0 x4', 'PCIe 5.0 x4',
                'PCIe 3.0 x2', 'PCIe 2.0 x2', 'SATA III (6 Гбит/с)',
                'U.2 (SFF-8639)', 'E1.S (EDSFF)'
            ],
        },
        'form_factor': {
            'label': 'Форм-фактор (размер)',
            'type': 'select',
            'options': [
                '2230', '2242', '2260', '2280', '22110',
                '2230 (Short)', '2242 (Medium)', '2280 (Стандарт)', '22110 (Long)'
            ],
        },
        'has_dram': {
            'label': 'DRAM-буфер',
            'type': 'select',
            'options': [
                'Есть', 'Нет (DRAM-less)',
                'HMB (Host Memory Buffer)', 'SLC-кэширование (псевдо-SLC)'
            ],
        },
        'read_speed': {
            'label': 'Макс. скорость последовательного чтения (МБ/с)',
            'type': 'range',
            'min': 500,
            'max': 14500,
            'step': 100,
        },
        'tbw': {
            'label': 'Максимальный ресурс записи (TBW, ТБ)',
            'type': 'range',
            'min': 40,
            'max': 144000,
            'step': 100,
        },
        'write_speed': {
            'label': 'Макс. скорость последовательной записи (МБ/с)',
            'type': 'range',
            'min': 300,
            'max': 13000,
            'step': 100,
        },
        'has_heatsink': {
            'label': 'Радиатор в комплекте',
            'type': 'select',
            'options': [
                'Есть (в комплекте)', 'Нет',
                'Опционально / Съемный', 'Графеновый / ультратонкий'
            ],
        },
        'nand_type': {
            'label': 'Количество бит на ячейку (Тип NAND)',
            'type': 'select',
            'options': [
                'SLC (1 бит)', 'MLC (2 бита)', '3D MLC (2 бита)',
                'TLC (3 бита)', '3D TLC (3 бита)',
                'QLC (4 бита)', '3D QLC (4 бита)', 'PLC (5 бит)'
            ],
        },
        'm_key': {
            'label': 'Ключ разъема M.2',
            'type': 'select',
            'options': [
                'M-Key (PCIe NVMe / SATA)', 'B-Key (SATA / PCIe x2)',
                'B+M Key (SATA)', 'E-Key (Wi-Fi / Bluetooth)',
                'A+E-Key (Wi-Fi / Bluetooth)', 'Нет данных'
            ],
        },
        # Дополнительные полезные поля (можешь оставить или удалить):
        'pcie_lanes': {
            'label': 'Количество линий PCIe',
            'type': 'select',
            'options': ['x2', 'x4', 'x8', 'x16'],
        },
        'controller': {
            'label': 'Контроллер',
            'type': 'select',
            'options': [
                'Phison E18', 'Phison E21T', 'Phison E25 / E25T', 'Phison E31T',
                'Silicon Motion SM2264', 'Silicon Motion SM2267 / SM2267XT',
                'Silicon Motion SM2281', 'WD / SanDisk (собственный)',
                'Samsung (собственный)', 'Micron (собственный)', 'Realtek RTS5771DL'
            ],
        },
    },
    'hdd-35': {
        'capacity': {
            'label': 'Объём накопителя (ТБ)',
            'type': 'range',
            'min': 0.5,
            'max': 24,
            'step': 0.5,
        },
        'purpose': {
            'label': 'Назначение',
            'type': 'select',
            'options': [
                'Для настольных ПК (Desktop)',
                'Для NAS (сетевых хранилищ)',
                'Для серверов (Enterprise / Data Center)',
                'Для видеонаблюдения (Surveillance)',
                'Для внешних накопителей (External)',
                'Универсальный'
            ],
        },
        'rpm': {
            'label': 'Скорость вращения шпинделя (об/мин)',
            'type': 'select',
            'options': [
                '4200 RPM', '4500 RPM', '5400 RPM', '5700 RPM',
                '5900 RPM', '6400 RPM', '7200 RPM',
                '10000 RPM', '15000 RPM'
            ],
        },
        'recording_technology': {
            'label': 'Технология записи',
            'type': 'select',
            'options': [
                'CMR (Conventional Magnetic Recording)',
                'SMR (Shingled Magnetic Recording)',
                'HAMR (Heat-Assisted Magnetic Recording)',
                'MAMR (Microwave-Assisted Magnetic Recording)',
                'PMR (Perpendicular Magnetic Recording)',
                'EAMR (Energy-Assisted Magnetic Recording)'
            ],
        },
        'cache_size': {
            'label': 'Объём кэш-памяти',
            'type': 'select',
            'options': [
                '32 МБ', '64 МБ', '128 МБ', '256 МБ', '512 МБ'
            ],
        },
        'raid_optimized': {
            'label': 'Оптимизация под RAID-массивы',
            'type': 'select',
            'options': [
                'Есть (поддержка TLER / ERC / CCTL)',
                'Нет (стандартный режим)'
            ],
        },
        'helium_filled': {
            'label': 'Гелиевое наполнение',
            'type': 'select',
            'options': [
                'Да (гелиевый корпус)',
                'Нет (воздушный корпус)'
            ],
        },
        'load_unload_cycles': {
            'label': 'Число циклов позиционирования-парковки (Load/Unload Cycles)',
            'type': 'range',
            'min': 300000,
            'max': 600000,
            'step': 50000,
        },
        'noise_level': {
            'label': 'Уровень шума во время работы (дБ)',
            'type': 'range',
            'min': 15,
            'max': 45,
            'step': 1,
        },
        'thickness': {
            'label': 'Толщина накопителя (мм)',
            'type': 'range',
            'min': 20,
            'max': 30,
            'step': 1,
        },
    },
    'hdd-25': {
        'capacity': {
            'label': 'Объём накопителя (ТБ)',
            'type': 'range',
            'min': 0.125,
            'max': 5,
            'step': 0.125,
        },
        'interface': {
            'label': 'Интерфейс подключения',
            'type': 'select',
            'options': [
                'SATA III (6 Гбит/с)', 'SATA II (3 Гбит/с)', 'SATA I (1.5 Гбит/с)',
                'SAS 12 Гбит/с', 'SAS 6 Гбит/с', 'SAS 3 Гбит/с',
                'USB 3.0 (внешний)', 'USB 3.1 (внешний)', 'USB-C (внешний)'
            ],
        },
        'rpm': {
            'label': 'Скорость вращения шпинделя (об/мин)',
            'type': 'select',
            'options': [
                '4200 RPM', '4500 RPM', '5200 RPM', '5400 RPM',
                '5700 RPM', '5900 RPM', '7200 RPM', '10000 RPM'
            ],
        },
        'recording_technology': {
            'label': 'Технология записи',
            'type': 'select',
            'options': [
                'CMR (Conventional Magnetic Recording)',
                'SMR (Shingled Magnetic Recording)',
                'PMR (Perpendicular Magnetic Recording)',
                'HAMR (Heat-Assisted Magnetic Recording)',
                'MAMR (Microwave-Assisted Magnetic Recording)'
            ],
        },
        'cache_size': {
            'label': 'Объём буфера (кэш-памяти)',
            'type': 'select',
            'options': [
                '8 МБ', '16 МБ', '32 МБ', '64 МБ', '128 МБ', '256 МБ'
            ],
        },
        'thickness': {
            'label': 'Стандартная толщина',
            'type': 'select',
            'options': [
                '5 мм (ультратонкий)', '7 мм (стандартный для ноутбуков)',
                '9.5 мм (стандартный)', '12.5 мм (увеличенный)',
                '15 мм (серверный/enterprise)'
            ],
        },
        'noise_level_active': {
            'label': 'Уровень шума во время работы (дБ)',
            'type': 'range',
            'min': 18,
            'max': 36,
            'step': 1,
        },
        'data_transfer_rate': {
            'label': 'Скорость обмена данными (МБ/с)',
            'type': 'range',
            'min': 50,
            'max': 280,
            'step': 5,
        },
        'noise_level_idle': {
            'label': 'Уровень шума в простое (дБ)',
            'type': 'range',
            'min': 15,
            'max': 30,
            'step': 1,
        },
        'load_unload_cycles': {
            'label': 'Число циклов позиционирования-парковки',
            'type': 'range',
            'min': 300000,
            'max': 600000,
            'step': 50000,
        },
    },
    '_common': {
        'brand': {
            'label': 'Бренд',
            'type': 'select',
            'options': [],
        },
        'price': {
            'label': 'Цена',
            'type': 'range',
            'min': 0,
            'max': 200000,
            'step': 100,
        },
        'in_stock': {
            'label': 'В наличии',
            'type': 'checkbox',
        },
    }
}