from multiprocessing import context
import os
from unicodedata import category
from django.shortcuts import render, redirect
from numpy import product
from requests import post
from io import BytesIO
from Services.blockChainRegisterProperty import registerProperty
from Services.blockChainTransferService import transferProperty
from Services.privateKeyValidator import is_valid_rsa_key


from customers.models import CustomUser
from .models import Category, Products, Review
from .forms import ProductForm, ReviewForm
from PIL import Image
from django.http import HttpResponseRedirect, FileResponse
from django.contrib import messages
from django.contrib.auth.models import User
import hashlib
import base64
from django.core.files.uploadedfile import TemporaryUploadedFile

def index(request):
    products = Products.objects.all()
    category = Category.objects.all()
    return render(request, 'main/index.html', {'title':'Hub', 'products':products, 'category':category})


def about(request):
    return render(request, 'main/about.html')



def viewProduct(request, product_id):
    product = Products.objects.get(pk=product_id)
    review = Review.objects.all()
    product_owner = CustomUser.objects.get(pk=product.owner)
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
    product.futureOwner = request.user.id
    product.isAvailable = False
    product.requested = True
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


def acceptRequest(request, product_id):
    if request.method == "POST":
        private_key = request.POST.get('private_key')
        product = Products.objects.get(pk=product_id)

        if product.owner == request.user.id :
            currentOwner = CustomUser.objects.get(pk=product.owner)
            futureOwner= CustomUser.objects.get(pk=product.futureOwner)
            if is_valid_rsa_key(private_key) == True:
                data = transferProperty(currentOwner.blockchainPublicKey, private_key, futureOwner.blockchainPublicKey, product.fileEntityHashSSH256)
                print(data)
                if data['isSuccess'] == True:
                    
                    
                    product.owner = product.futureOwner
                    product.futureOwner = None
                    product.requested = False
                    product.save()  
                    return redirect ('ProfilePage')

                else:
                    # messages.error(request, data['Payload'])     
                    messages.error(request, data['error'])
            else:
                messages.error(request, 'Invalid private key')

        else:
            messages.error(request, 'Invalid private key')
            
    return redirect ('ProfilePage')


            
    

def autorisation(request):
    return render(request, 'main/autorisation.html')


def addProduct(request):
    error =''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        private_key = request.POST.get('product_private_key')

        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user.id
            
            # Read the file data from InMemoryUploadedFile
            file_data = request.FILES['fileEntity'].read()
            
            # Calculate the hash
            readable_hash = hashlib.sha256(file_data).digest()
            Hash = base64.b64encode(readable_hash).decode()
            
            # Save the hash to the product
            product.fileEntityHashSSH256 = Hash

            # Process the private key and register the property
            User = CustomUser.objects.get(pk=request.user.id)
            if is_valid_rsa_key(private_key):
                data = registerProperty(User.blockchainPublicKey, private_key, Hash)
                if data['isSuccess']:
                    product.save()
                    return redirect('/')
                else:
                    messages.error(request, data['error'])
            else:
                messages.error(request, 'Invalid private key')
        else:
            error = 'Incorrect Form'
    else:
        form = ProductForm()
    
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/addProduct.html', context)



# def addProduct(request):
#     error =''
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         private_key = request.POST.get('product_private_key')

        
#         if form.is_valid():
#             product = form.save(commit=False)
#             # with open(product.fileEntity, 'rb') as file:
#             # # with product.fileEntity.open('rb') as file:
#             #     bytes = file.read() # Read entire file as bytes
#             #     readable_hash = hashlib.sha256(bytes).digest() # Create SHA-256 hash
#             #     product.fileEntityHashSSH256 = base64.b64encode(readable_hash).decode()
#             # # product = form.save(commit=False)
#             product.owner = request.user.id
#             ProductFileField = product.fileEntity


#             with ProductFileField.open('rb') as file:
#                 bytes = file.read() # Read entire file as bytes
#                 readable_hash = hashlib.sha256(bytes).digest() # Create SHA-256 hash
#                 Hash = base64.b64encode(readable_hash).decode()
#                 product.fileEntityHashSSH256 = Hash
#                 User = CustomUser.objects.get(pk=request.user.id)
#             ProductFileField.close()
#             if is_valid_rsa_key(private_key) == True:
#                 data = registerProperty(User.blockchainPublicKey, private_key, Hash)
#                 if data['isSuccess'] == True:

#                     product.save()
#                     return redirect('/')
#                 else:
#                     # messages.error(request, data['Payload'])     
#                     messages.error(request, data['error'])
#             else:
#                 # messages.error(request, data['Payload'])     
#                 messages.error(request, data['error'])
#         else:
#             error = 'Incorrect Form'
#     form = ProductForm()
#     context = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'main/addProduct.html', context)

