from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product, Category
from .forms import ContactForm

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
    initial_data = {}
    product_id = request.GET.get('product')
    if product_id:
        try:
            product = Product.objects.get(id=product_id)
            initial_data['subject'] = f"Inquiry about {product.name}"
            initial_data['message'] = f"I am interested in learning more about the {product.name}. Please provide details regarding pricing and availability."
        except Product.DoesNotExist:
            pass

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully! We'll get back to you shortly.")
            return redirect('core:contact')
    else:
        form = ContactForm(initial=initial_data)

    return render(request, 'core/contact.html', {'form': form})
