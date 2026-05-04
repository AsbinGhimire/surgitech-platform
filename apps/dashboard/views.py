from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from products.models import Category, Product
from .forms import CategoryForm, ProductForm


# ─── Home ────────────────────────────────────────────────────────────────────

@staff_member_required(login_url='/admin/login/')
def dashboard_home(request):
    context = {
        'total_categories': Category.objects.count(),
        'total_products':   Product.objects.count(),
        'featured_count':   Product.objects.filter(is_featured=True).count(),
        'recent_products':  Product.objects.select_related('category').order_by('-created_at')[:6],
        'categories':       Category.objects.all(),
    }
    return render(request, 'dashboard/home.html', context)


# ─── Categories ──────────────────────────────────────────────────────────────

@staff_member_required(login_url='/admin/login/')
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/categories/list.html', {'categories': categories})


@staff_member_required(login_url='/admin/login/')
def category_add(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Category added successfully!')
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/categories/form.html', {'form': form, 'title': 'Add Category'})


@staff_member_required(login_url='/admin/login/')
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Category updated successfully!')
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/categories/form.html', {'form': form, 'title': 'Edit Category', 'obj': category})


@staff_member_required(login_url='/admin/login/')
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted.')
        return redirect('dashboard:category_list')
    return render(request, 'dashboard/confirm_delete.html', {'obj': category, 'type': 'Category'})


# ─── Products ────────────────────────────────────────────────────────────────

@staff_member_required(login_url='/admin/login/')
def product_list(request):
    category_id = request.GET.get('category')
    q = request.GET.get('q')
    
    products = Product.objects.select_related('category').order_by('-created_at')
    
    if category_id:
        products = products.filter(category_id=category_id)
    
    if q:
        products = products.filter(name__icontains=q) | products.filter(brand__icontains=q)
        
    categories = Category.objects.all()
    return render(request, 'dashboard/products/list.html', {
        'products': products,
        'categories': categories,
        'selected_cat': int(category_id) if category_id else None,
        'q': q,
    })


@staff_member_required(login_url='/admin/login/')
def product_add(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Product added successfully!')
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/products/form.html', {'form': form, 'title': 'Add Product'})


@staff_member_required(login_url='/admin/login/')
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Product updated successfully!')
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/products/form.html', {'form': form, 'title': 'Edit Product', 'obj': product})


@staff_member_required(login_url='/admin/login/')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted.')
        return redirect('dashboard:product_list')
    return render(request, 'dashboard/confirm_delete.html', {'obj': product, 'type': 'Product'})
