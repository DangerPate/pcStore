# catalog/admin.py
from django.contrib import admin
from .models import Product, Category, Review, ReviewAttachment, ReviewVote, ReviewComment, ProductImage


# 🔥 Inline для изображений — ОПРЕДЕЛЯЕМ ПЕРЕД ИСПОЛЬЗОВАНИЕМ
class ProductImageInline(admin.TabularInline):
    """Inline для управления изображениями товара"""
    model = ProductImage
    extra = 1
    fields = ['image', 'is_main', 'order']
    ordering = ['order']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'in_stock', 'is_active', 'created_at']
    list_filter = ['is_active', 'categories', 'created_at']
    search_fields = ['title', 'sku', 'brand']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['categories']
    inlines = [ProductImageInline]

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'slug', 'sku', 'brand', 'categories', 'variant_group')
        }),
        ('Цены и наличие', {
            'fields': ('price', 'old_price', 'in_stock', 'is_active')
        }),
        ('Описание', {
            'fields': ('info', 'description'),
            'classes': ('collapse',)
        }),
        # 🔥 Только РЕДАКТИРУЕМЫЕ поля маркеров:
        ('Маркетинг (ручное управление)', {
            'fields': ('force_hit', 'force_new'),
            'classes': ('collapse',),
            'description': 'Эти флаги переопределяют автоматические статусы "хит" и "новинка"'
        }),
        ('Технические', {
            'fields': ('weight', 'warranty', 'specifications'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at', 'updated_at', 'views']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'author_name', 'rating', 'created_at', 'is_verified_purchase']
    list_filter = ['rating', 'is_verified_purchase', 'created_at']
    search_fields = ['comment', 'author_name', 'product__title']
    readonly_fields = ['created_at']


@admin.register(ReviewAttachment)
class ReviewAttachmentAdmin(admin.ModelAdmin):
    list_display = ['review', 'file_type', 'uploaded_at']
    list_filter = ['file_type', 'uploaded_at']


@admin.register(ReviewVote)
class ReviewVoteAdmin(admin.ModelAdmin):
    list_display = ['review', 'user', 'vote', 'created_at']
    list_filter = ['vote', 'created_at']


@admin.register(ReviewComment)
class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ['review', 'user', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'is_main', 'order', 'created_at']
    list_filter = ['is_main', 'created_at']
    list_editable = ['is_main', 'order']