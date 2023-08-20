from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from Services import blockChainService
from customers.models import CustomUser
from main.models import Products, Category
from .forms import RegisterUserForm     



def profile_page(request):
    products = Products.objects.all()
    category = Category.objects.all()
    
    return render(request, 'authenticate/profilePage.html', {'title':'ProfilePage','products':products, 'category':category})

def login_user(request):
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
            login(request, user)
            return redirect('Hub')
        else:
            messages.success(request, ("Not possible to log in"))
            return redirect('LogIn')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):

    logout(request)
    messages.success(request, ("You were loged Out"))
    return redirect('Hub')
   

def register_user(request):
    
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            user = authenticate(username=username, password=password1)
            login(request, user)
            messages.success(request, ("You were successfully registered"))
            return redirect('registration_successful')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {'form':form})

def registration_success(request):
    if request.session.get('registration_success'):
        # User has already accessed the page, handle accordingly
        return render(request, 'access_denied.html')

    blockChainService.create_new_user(request)
    data = blockChainService.create_new_user(request)
    
    customUser = request.user

    # Set session variable to indicate successful registration
    request.session['registration_success'] = True

    return render(request, 'authenticate/registration_successful.html', 
    {
        'customUser': customUser,
        'blockchainPrivateKey': data['private']
    })



# def registration_success(request):

#     # CustomUser.blockchainPublicKey = blockChainService.create_new_user.public
#     blockChainService.create_new_user(request)
#     data = blockChainService.create_new_user(request)
    
#     customUser = request.user
#     # customUser = CustomUser.objects.all()

#     return render(request, 'authenticate/registration_successful.html', 
#     {
#         'customUser':customUser,
#         'blockchainPrivateKey': data['private']
#     })
