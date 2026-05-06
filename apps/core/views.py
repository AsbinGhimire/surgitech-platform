from django.shortcuts import render
from products.models import Product, Category

def home(request):
    latest_products = Product.objects.all().order_by('-created_at')[:4]
    categories = Category.objects.all()
    context = {
        'latest_products': latest_products,
        'categories': categories
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
