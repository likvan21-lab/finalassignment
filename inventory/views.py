from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


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