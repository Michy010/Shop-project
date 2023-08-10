from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # Save user to Database
        username = form.cleaned_data.get('username') # Get the username that is submitted
        messages.success(request, f'Your account {username} has been created! You are now able to log in') # Show sucess message when account is created
            
        return redirect('login') # Redirect user to home page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
    
def login_page (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        
        return render(request, 'login.html')
    else:
        messages.info(request, 'Username or Password is incorrect')


@login_required
def profile (request):
    return render (request, 'users/profile.html')

def update_profile(request):
    return render(request , 'users/update_profile.html')