from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_thumbnail', 'name', 'category', 'price', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    list_editable = ('is_featured', 'price')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    date_hierarchy = 'created_at'

    @admin.display(description='Image')
    def get_thumbnail(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" style="width: 45px; height: auto; border-radius: 4px;" />', obj.main_image.url)
        return "No Image"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_thumbnail', 'name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

    @admin.display(description='Image')
    def get_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height: auto; border-radius: 4px;" />', obj.image.url)
        return "No Image"