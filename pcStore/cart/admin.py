from django.contrib import admin
from .models import Order, OrderItem, Cart, CartItem, Favorite


@admin.action(description='🗑 Удалить выбранные заказы')
def delete_selected_orders(modeladmin, request, queryset):
    count = queryset.count()
    queryset.delete()
    modeladmin.message_user(request, f'✅ Удалено заказов: {count}')


@admin.action(description=' Экспортировать в CSV')
def export_orders_csv(modeladmin, request, queryset):
    import csv
    from django.http import HttpResponse

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Пользователь', 'Имя', 'Телефон', 'Email', 'Адрес', 'Сумма', 'Статус', 'Дата'])

    for order in queryset:
        writer.writerow([
            order.id,
            order.user.email if order.user else '—',
            order.first_name,
            order.phone,
            order.email or '—',
            order.address,
            order.total_price,
            order.get_status_display(),
            order.created_at.strftime('%d.%m.%Y %H:%M')
        ])

    return response


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'price', 'quantity', 'get_total_price')

    def get_total_price(self, obj):
        return obj.get_total_price()

    get_total_price.short_description = 'Сумма'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'phone', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'first_name', 'phone', 'email', 'user__email')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    inlines = [OrderItemInline]

    # Действия
    actions = [delete_selected_orders, export_orders_csv]

    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'first_name', 'phone', 'email')
        }),
        ('Доставка', {
            'fields': ('address', 'comment')
        }),
        ('Оплата и статус', {
            'fields': ('total_price', 'status', 'created_at')
        }),
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'get_total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email', 'product__title')

    def get_total_price(self, obj):
        return obj.get_total_price()

    get_total_price.short_description = 'Сумма'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'added_at')
    search_fields = ('user__email', 'product__title')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__email',)