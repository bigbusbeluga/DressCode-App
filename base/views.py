from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'base/base.html')

def mixmatch(request):
    return render(request, 'base/mixmatch.html')

def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'base/signup.html')