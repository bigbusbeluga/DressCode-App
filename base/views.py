from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'base.html')

def signup_view(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')