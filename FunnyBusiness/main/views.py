from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from numpy import product
from .models import Category, Products
from .forms import ProductForm
from PIL import Image
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User




def index(request):
    products = Products.objects.all()
    category = Category.objects.all()
    return render(request, 'main/index.html', {'title':'Hub', 'products':products, 'category':category})


def about(request):
    return render(request, 'main/about.html')


def addProduct(request):
    error =''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user.id
            product.save()
            return redirect('/')
        else:
            error = 'Incorrect Form'

    form = ProductForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/addProduct.html', context)


def viewProduct(request, product_id):
    product = Products.objects.get(pk=product_id)
    product_owner = User.objects.get(pk=product.owner)
    return render(request, 'main/viewProduct.html', {'product': product, 'product_owner' : product_owner})


def editProduct(request, product_id):
    product = Products.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect ('ProfilePage')
    return render(request, 'main/editProduct.html', {'product': product, 'form': form})
        

def deleteProduct(request, product_id):
    product = Products.objects.get(pk=product_id)
    if request.user.id ==  product.owner:
        product.delete()
        messages.success(request, ("Product Deleted"))
        return redirect ('ProfilePage')
    else:
        messages.success(request, ("Ooo0oppss"))
        return redirect ('ProfilePage')


def autorisation(request):
    return render(request, 'main/autorisation.html')
