from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index (request):
    return render (request, 'shop/index.html')

#def register (request):
    #return render (request, 'users/register.html')

def product_list (request):
       products = Product.objects.all()
       context = {'products':products}
       return render (request, 'shop/Product.html',context)
    
#def login_page (request):
    #return render (request, 'registration/login.html')

def logout_page (request):
    return render (request, 'registration/logout.html')

def profile (request):
    return render (request, 'registration/profile.html')

def update_profile (request):
    return render (request, 'registration/update.html')
