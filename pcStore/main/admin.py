# main/admin.py
from django.contrib import admin
from .models import Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'is_current', 'created_at']
    list_filter = ['is_active', 'link_type', 'created_at']
    search_fields = ['title', 'subtitle', 'description']
    ordering = ['order', '-created_at']
    filter_horizontal = ['products']  # Удобный виджет для ManyToMany

    fieldsets = (
        ('Изображение', {
            'fields': ('image', 'overlay_color'),
            'description': 'Загрузите баннер или задайте цвет фона'
        }),
        ('Текстовый контент', {
            'fields': ('title', 'subtitle', 'description'),
            'classes': ('collapse',)  # Сворачиваемая секция
        }),
        ('Кнопка', {
            'fields': ('button_text', 'button_color'),
            'classes': ('collapse',)
        }),
        ('Ссылка', {
            'fields': ('link_type', 'link_category', 'link_product', 'link_url'),
            'description': 'Выберите тип ссылки и укажите целевой объект'
        }),
        ('Товары акции', {
            'fields': ('products',),
            'description': 'Выберите товары, участвующие в этой акции'
        }),
        ('Настройки', {
            'fields': ('is_active', 'order', 'start_date', 'end_date'),
        }),
    )

    readonly_fields = ['created_at', 'updated_at']