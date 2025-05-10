from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'base/base.html')

def signup_view(request):
    return render(request, 'base/signup.html')

def login_view(request):
    return render(request, 'base/login.html')

def mixmatch_view(request):
    return render(request, 'base/mixmatch.html')