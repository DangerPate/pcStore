from django import template

register = template.Library()

@register.filter
def get_range_value(get_dict, key):
    """Возвращает значение для range-фильтра из GET-параметров"""

    if key == 'price':
        return get_dict.get('price_min') or get_dict.get('price_max')

    return get_dict.get(f'{key}_min') or get_dict.get(f'{key}_max')