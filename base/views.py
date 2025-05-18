from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from .models import Clothing, Category
from .forms import SingUpForm, addClothingForm, ClothingForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

def landing(request):
    return render(request, 'base/landing.html')

def home(request):
    return render(request, 'base/base.html')

def homepage(request):
    return render(request, 'base/homepage.html')

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

def login_user(request):
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

def logout_user(request):
    logout(request)
    return redirect('landing')
    
@login_required(login_url='login')
def mixmatch(request):
    category_filter = request.GET.get('category')
    if request.user.is_authenticated:
        clothing = Clothing.objects.filter(user=request.user)
        if category_filter and category_filter != "All":
            clothing = clothing.filter(category__name__iexact=category_filter)
    else:
        clothing = Clothing.objects.none()  # Show nothing for anonymous users
    categories = Category.objects.all()
    context = {
        'clothing': clothing,
        'categories': categories,
        'selected_category': category_filter or 'All'
    }
    return render(request, 'base/mixmatch.html', context)

@login_required(login_url='login')
def wardrobe(request):
    category_filter = request.GET.get('category')
    if request.user.is_authenticated:
        clothing = Clothing.objects.filter(user=request.user)
        if category_filter and category_filter != "All":
            clothing = clothing.filter(category__name__iexact=category_filter)
    else:
        clothing = Clothing.objects.none()
    categories = Category.objects.all()
    
    context = {
        'clothing': clothing,
        'categories': categories,
        'selected_category': category_filter or 'All'
    }
    return render(request, 'base/wardrobe.html', context)

def laundry(request):
    return render(request, 'base/laundry.html')

@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteClothing(request, pk):
    clothing = get_object_or_404(Clothing, id=pk, user=request.user)
    if request.method == "POST":
        clothing.delete()
        return redirect('wardrobe')  # Redirect to mixmatch after deletion
    context = {'clothing': clothing}
    return render(request, 'base/delete_clothing.html', context)

@csrf_protect  # or use CSRF middleware
def upload_clothing(request):
    if request.method == 'POST':
        form = ClothingForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user  # if auth enabled
            item.save()
            return JsonResponse({'status': 'success', 'item_id': item.id})
        else: 
            print(form.errors)
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    else: 
        print(form.errors)
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
        