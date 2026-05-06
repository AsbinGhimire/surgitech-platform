from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    """
    Displays all products grouped by category on a single page.
    """
    from django.db.models import Count, Q
    categories_with_products = Category.objects.filter(parent=None).annotate(
        product_count=Count('products', distinct=True),
        child_product_count=Count('children__products', distinct=True)
    ).filter(Q(product_count__gt=0) | Q(child_product_count__gt=0)).prefetch_related('children', 'products', 'children__products').all()
    
    # For the Quick Jump menu: Top 12 categories by product count
    popular_categories = Category.objects.annotate(
        total_products=Count('products')
    ).order_by('-total_products')[:12]
    
    return render(request, 'products/list.html', {
        'categories_with_products': categories_with_products,
        'popular_categories': popular_categories,
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