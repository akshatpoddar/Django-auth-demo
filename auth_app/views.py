from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'auth_app/home.html')
    
def signIn_user(request):
    if request.user.is_authenticated: 
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'Signed in succesfully!')
                return redirect('home')
            else:
                messages.error(request,'Invalid credentials, try again!')
                return redirect('signin')
    else:  
        form = AuthenticationForm()  
    context = {'form':form}
    return render(request, 'auth_app/signin.html', context)

def signUp_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form['username']
            if User.objects.filter(username=username).exists():
                messages.error(request,'User already exists with same username!')
                return redirect('signup')
            else:
                form.save() 
                messages.success(request,'Account created succesfully!')
                return redirect('signin')
    else:  
        form = UserCreationForm()  
    context = {'form': form}
    return render(request, 'auth_app/signup.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')
