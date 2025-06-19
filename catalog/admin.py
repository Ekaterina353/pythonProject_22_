from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name', 'description')
    list_filter = ('name',)
    ordering = ('id', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', )
    list_filter = ('category', 'created_at', 'changed_at', )
    search_fields = ('name', 'description', )
    ordering = ('-created_at', )
    actions = [
        'publish_selected_products',
        'unpublish_selected_products'
    ]

    def publish_selected_products(self, request, queryset):
        queryset.update(status='PU')
    publish_selected_products.short_description = "Publish selected products"

    def unpublish_selected_products(self, request, queryset):
        queryset.update(status='PU')
    unpublish_selected_products.short_description = "Unpublish selected products"
