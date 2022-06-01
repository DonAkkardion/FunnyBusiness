from multiprocessing import context
from unicodedata import category
from django.shortcuts import render, redirect
from numpy import product
from requests import post
from .models import Category, Products, Review
from .forms import ProductForm, ReviewForm
from PIL import Image
from django.http import HttpResponseRedirect, FileResponse
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
    review = Review.objects.all()
    product_owner = User.objects.get(pk=product.owner)
    return render(request, 'main/viewProduct.html', 
    {
        'product': product,
        'product_owner': product_owner,
        'review': review, 
    })


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


def buyProduct(request, product_id):
    product = Products.objects.get(pk=product_id)
    product.owner = request.user.id
    product.isAvailable = False
    product.save()

    context = {
        'product': product
        
    }
    return render(request, 'buyProduct.html', context)

def downloadFile(request, product_id):
    product = Products.objects.get(pk=product_id)
    prod = product.fileEntity
    name = product.name

    return FileResponse(prod, as_attachment=True)
    


def rateProduct(request, product_id):
    error =''
    if request.method == 'POST':
        product = Products.objects.get(pk=product_id)
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            Review = form.save(commit=False)
            Review.target = product.id
            Review.save()
            return redirect('/')
        else:
            error = 'Incorrect Form'

    form = ReviewForm()
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/rateProduct.html', context)


def searchProduct(request):

    if request.method == "POST":
        searched = request.POST["searched"]

        products = Products.objects.filter(name__contains=searched)
        products = products.union(Products.objects.filter(category__name__contains=searched))  

        context = {
        'searched': searched,
        'products': products
        }

        return render(request, 'main/searchProduct.html', context)
    
    else:
        return render(request, 'main/searchProduct.html')

def autorisation(request):
    return render(request, 'main/autorisation.html')



