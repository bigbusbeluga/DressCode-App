from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.forms import ModelForm
from .models import Clothing
from .forms import SingUpForm, addClothingForm

def home(request):
    return render(request, 'base/base.html')

def signup(request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('mixmatch')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SingUpForm()
    return render(request, 'base/signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('mixmatch')
        else:
            messages.error(request, 'Username or password is incorrect')
    else:
        form = AuthenticationForm()
    return render(request, 'base/login.html', {'form': form})

def mixmatch(request):
    if request.user.is_authenticated:
        clothing = Clothing.objects.filter(user=request.user)
    else:
        clothing = Clothing.objects.none()  # Show nothing for anonymous users
    context = {'clothing': clothing}
    return render(request, 'base/mixmatch.html', context)

def addClothing(request):
    if request.method == "POST":
        form = addClothingForm(request.POST, request.FILES)
        if form.is_valid():
            clothing = form.save(commit=False)
            clothing.user = request.user  # Assign the current user
            clothing.save()
            return redirect('mixmatch')
    else:
        form = addClothingForm()
    context = {'form': form}
    return render(request, 'base/add_clothing.html', context)