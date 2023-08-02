from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login , logout

def register_View(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save() # save passed data
            login(request, user) # login the user
            messages.success(request, "Registration Successful")
            return redirect("/")
        messages.error(request, "Invalid information")
        
    context = {
        "form": form,
    }
        
    return render(request, "register.html", context)

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
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username') # viny
            password = request.POST.get('password') # viny@123!
            user = authenticate(request, username=username, password=password)
            #TRUE/FASLE

            if user is not None:
                login(request, user)
                return redirect('shop:home')
            else:
                messages.info(request, 'username or password is incorrect!') 
        return render(request, 'accounts/login.html')
    
def login_page (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 

        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        messages.info(request, 'Username or Password is incorrect')


@login_required
def profile (request):
    return render (request, 'users/profile.html')

def update_profile(request):
    return render(request , 'users/update_profile.html')