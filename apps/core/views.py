from django.shortcuts import render
from products.models import Product, Category

def home(request):
    featured_products = Product.objects.filter(is_featured=True).order_by('-created_at')[:4]
    categories = Category.objects.all()
    context = {
        'featured_products': featured_products,
        'categories': categories
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
