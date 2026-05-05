from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    """
    Displays all products grouped by category on a single page.
    """
    categories_with_products = Category.objects.prefetch_related('products').all()
    # Filter out categories that have no products if desired, 
    # but for a catalog, showing empty categories might be fine too.
    return render(request, 'products/list.html', {
        'categories_with_products': categories_with_products,
    })  

def product_detail(request, slug):
    """
    Displays a single product detail with its gallery and related products.
    """
    product = get_object_or_404(Product.objects.prefetch_related('images'), slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    return render(request, 'products/detail.html', {
        'product': product,
        'related_products': related_products
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