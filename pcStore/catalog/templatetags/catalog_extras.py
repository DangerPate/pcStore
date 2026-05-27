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