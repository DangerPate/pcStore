from django import template

register = template.Library()


@register.filter
def add_page_filter(value, page_number):
    """
    Добавляет ?page=X к текущему URL, сохраняя остальные фильтры.
    Пример: было ?brand=nvidia&price_min=10000
    стало: ?brand=nvidia&price_min=10000&page=2
    """
    request = value.request  # Мы передаем request в фильтр
    get_params = request.GET.copy()

    # Если есть page, удаляем его, чтобы не было ?page=1&page=2
    if 'page' in get_params:
        del get_params['page']

    # Если пустые параметры, убираем знак вопроса
    if not get_params:
        return f'?page={page_number}'

    get_params['page'] = page_number
    return f'?{get_params.urlencode()}'

@register.filter
def humanize_key(key):
    """Превращает 'gpu_model' в 'Графический процессор'"""
    mapping = {
        'gpu_model': 'Графический процессор',
        'vram': 'Объём видеопамяти',
        'gpu_vendor': 'Производитель GPU',
        'purpose': 'Назначение',
        'memory_bus': 'Шина памяти',
        'interface': 'Интерфейс',
        'cooling': 'Охлаждение',
        'memory_type': 'Тип памяти',
        'gpu_series': 'Линейка',
        'color': 'Цвет',
        'length': 'Длина',
        'socket': 'Сокет',
        'family': 'Семейство',
        'perf_cores': 'Производительные ядра',
        'generation': 'Поколение',
        'igpu': 'Встроенная графика',
        'packaging': 'Упаковка',
        'base_clock': 'Базовая частота',
        'turbo_clock': 'Турбо-частота',
        'tdp': 'TDP',
        'tdp_rating': 'Рассеиваемая мощность',
        'chipset': 'Чипсет',
        'form_factor': 'Форм-фактор',
        'pcie_version': 'Версия PCIe',
        'ram_slots': 'Слоты памяти',
        'cpu_support': 'Поддержка процессоров',
        'm2_slots': 'Слоты M.2',
        'wifi_std': 'Wi-Fi стандарт',
        'total_capacity': 'Общий объём',
        'module_capacity': 'Объём модуля',
        'frequency': 'Частота',
        'kit_size': 'Модулей в комплекте',
        'ram_purpose': 'Тип',
        'cas_latency': 'Тайминги (CL)',
        'heatsink': 'Радиатор',
        'wattage': 'Мощность',
        'certification': 'Сертификат',
        'modularity': 'Модульность',
        'pci_e_connectors': 'Разъёмы PCI-E',
        'atx_standard': 'Стандарт ATX',
        'pfc': 'PFC',
        'cpu_connectors': 'Питание CPU',
        'cable_sleeving': 'Оплетка кабелей',
        'mb_support': 'Поддержка плат',
        'case_type': 'Тип корпуса',
        'aquarium_style': 'Аквариум',
        'included_fans': 'Вентиляторы в комплекте',
        'psu_location': 'Расположение БП',
        'window_material': 'Материал окна',
        'max_cooler_height': 'Макс. высота кулера',
        'max_gpu_length': 'Макс. длина видеокарты',
        'has_side_window': 'Окно сбоку',
        'construction_type': 'Конструкция',
        'heatpipes': 'Тепловые трубки',
        'height': 'Высота',
        'rgb_type': 'Подсветка',
        'fan_sizes': 'Размеры вентиляторов',
        'fan_count': 'Вентиляторов в комплекте',
        'fan_connector': 'Разъём вентилятора',
        'noise_level': 'Уровень шума',
    }
    return mapping.get(key, key.replace('_', ' ').title())

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)