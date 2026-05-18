from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from .models import Product, Category, Supplier
from .forms import CategoryForm
from .forms import SupplierForm
from .forms import StockForm
from django.contrib.auth.decorators import login_required


def product_list(request):
    products = Product.objects.all()

    return render(request, 'product_list.html', {
        'products': products
    })


def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProductForm()

    return render(request, 'add_product.html', {
        'form': form
    })
def edit_product(request, id):

    product = Product.objects.get(id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ProductForm(instance=product)

    return render(request, 'add_product.html', {
        'form': form
    })
def delete_product(request, id):

    product = Product.objects.get(id=id)

    product.delete()

    return redirect('/')
@login_required
def dashboard(request):

    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    total_suppliers = Supplier.objects.count()

    return render(request, 'dashboard.html', {
        'total_products': total_products,
        'total_categories': total_categories,
        'total_suppliers': total_suppliers,
    })
@login_required
def category_list(request):

    categories = Category.objects.all()

    if request.method == 'POST':

        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/categories')

    else:
        form = CategoryForm()

    return render(request, 'categories.html', {
        'categories': categories,
        'form': form
    })
@login_required
def supplier_list(request):

    suppliers = Supplier.objects.all()

    if request.method == 'POST':

        form = SupplierForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/suppliers')

    else:
        form = SupplierForm()

    return render(request, 'suppliers.html',  {
        'suppliers': suppliers,
        'form': form
    })
@login_required
def stock_management(request):

    message = ''

    if request.method == 'POST':

        form = StockForm(request.POST)

        if form.is_valid():

            product = form.cleaned_data['product']
            quantity = form.cleaned_data['quantity']
            action = form.cleaned_data['action']

            if action == 'IN':
                product.quantity += quantity

            elif action == 'OUT':

                if product.quantity >= quantity:
                    product.quantity -= quantity
                else:
                    message = 'Not enough stock'

            product.save()

            if message == '':
                message = 'Stock updated successfully'

    else:
        form = StockForm()

    return render(request, 'stock.html', {
        'form': form,
        'message': message
    })