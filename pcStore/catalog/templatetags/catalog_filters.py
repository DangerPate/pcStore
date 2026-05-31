from django import template

register = template.Library()

@register.filter
def get_range_value(get_dict, key):
    """Возвращает значение для range-фильтра из GET-параметров"""
    # Для price используем price_min/price_max
    if key == 'price':
        return get_dict.get('price_min') or get_dict.get('price_max')
    # Для остальных спецификаций: key_min / key_max
    return get_dict.get(f'{key}_min') or get_dict.get(f'{key}_max')