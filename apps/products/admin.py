from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage


# ─── Product Image Inline ───────────────────────────────────────────────────

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('image_preview',)

    @admin.display(description='Preview')
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:60px;height:auto;border-radius:4px;" />',
                obj.image.url
            )
        return "—"


# ─── Product Admin ───────────────────────────────────────────────────────────

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display   = ('get_thumbnail', 'name', 'category', 'brand', 'price', 'created_at')
    list_filter    = ('category', 'brand', 'created_at')
    list_editable  = ('price',)
    search_fields  = ('name', 'description', 'brand')
    prepopulated_fields = {'slug': ('name',)}
    inlines        = [ProductImageInline]
    date_hierarchy = 'created_at'
    list_per_page  = 20

    fieldsets = (
        ('Basic Info', {
            'fields': ('category', 'name', 'slug', 'brand', 'badge')
        }),
        ('Description & Specs', {
            'fields': ('description', 'specifications'),
            'classes': ('collapse',),
        }),
        ('Media', {
            'fields': ('main_image', 'bg_color'),
        }),
        ('Pricing', {
            'fields': ('price',),
        }),
        ('Ratings', {
            'fields': ('rating', 'review_count'),
        }),
    )

    @admin.display(description='Image')
    def get_thumbnail(self, obj):
        if obj.main_image:
            return format_html(
                '<img src="{}" style="width:45px;height:auto;border-radius:4px;" />',
                obj.main_image.url
            )
        return "No Image"


# ─── Category Admin ──────────────────────────────────────────────────────────

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display        = ('icon', 'name', 'parent', 'slug', 'product_count')
    list_filter         = ('parent',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields       = ('name',)
    list_per_page       = 20

    @admin.display(description='Products')
    def product_count(self, obj):
        count = obj.products.count()
        return format_html(
            '<span style="font-weight:600;color:#0066cc;">{}</span>',
            count
        )