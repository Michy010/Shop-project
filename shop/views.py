from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index (request):
    return render (request, 'shop/index.html')

def register (request):
    return render (request, 'users/register.html')

def product_list (request):
    products = Product.objects.all()
    context = {'products':products}
    return render (request, 'shop/Product.html',context)

def login (request):
    return render (request, 'shop/login.html')
