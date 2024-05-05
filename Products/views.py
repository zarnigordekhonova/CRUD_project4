from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Products
from .forms import ProductsForm

# Create your views here.

def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def get_products(request, pk):
    products = Products.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)

def detail(request, pk):
    product = Products.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)

def add_products(request):
    form = ProductsForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Products:get_info')
    context = {
        'form': form
    }
    return render(request, 'create.html', context=context)


def update_products(request, pk):
    data = Products.objects.get(pk=pk)
    form = ProductsForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('Products:get_info')
    context = {
        'form': form
    }
    return render(request, 'update.html', context=context)


def delete_products(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('Products:get_info')

    return render(request, 'delete.html', {'product': product})



