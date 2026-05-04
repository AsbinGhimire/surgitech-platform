from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    """
    Displays all available products, optimized with select_related.
    """
    products = Product.objects.select_related('category').all()
    categories = Category.objects.all()
    return render(request, 'products/list.html', {
        'products': products,
        'categories': categories,
    })  

def product_detail(request, slug):
    """
    Displays a single product detail, optimized with prefetch_related for the gallery.
    """
    product = get_object_or_404(Product.objects.prefetch_related('images'), slug=slug)
    return render(request, 'products/detail.html', {
        'product': product
    })

def category_products(request, slug):
    """
    Filters products by category.
    """
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category).select_related('category')

    return render(request, 'products/category.html', {
        'category': category,
        'products': products
    })