from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from .models import Clothing, Category, Outfit
from .forms import SingUpForm, addClothingForm
from django.http import JsonResponse
import json

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
    outfits = None
    if request.user.is_authenticated:
        clothing = Clothing.objects.filter(user=request.user)
        if category_filter == 'Outfits':
            outfits = Outfit.objects.filter(user=request.user).prefetch_related('clothes')
            clothing = Clothing.objects.none()
        elif category_filter and category_filter != "All":
            clothing = clothing.filter(category__name__iexact=category_filter)
    else:
        clothing = Clothing.objects.none()
    categories = Category.objects.all()
    context = {
        'clothing': clothing,
        'categories': categories,
        'selected_category': category_filter or 'All',
        'outfits': outfits
    }
    return render(request, 'base/mixmatch.html', context)

@login_required(login_url='login')
def wardrobe(request):
    category_filter = request.GET.get('category')
    outfits = None
    if request.user.is_authenticated:
        clothing = Clothing.objects.filter(user=request.user)
        if category_filter == 'Outfits':
            outfits = Outfit.objects.filter(user=request.user).prefetch_related('clothes')
            clothing = Clothing.objects.none()
        elif category_filter and category_filter != "All":
            clothing = clothing.filter(category__name__iexact=category_filter)
    else:
        clothing = Clothing.objects.none()
    categories = Category.objects.all()
    
    context = {
        'clothing': clothing,
        'categories': categories,
        'selected_category': category_filter or 'All',
        'outfits': outfits,
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

@login_required(login_url='login')
def saveOutfit(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_urls = data.get('images', [])
        if not image_urls:
            return JsonResponse({'success': False, 'error': 'No images provided.'})
        # Find Clothing objects by image URL
        clothing_items = Clothing.objects.filter(user=request.user, image__in=[url.replace(request.build_absolute_uri('/media/'), '') for url in image_urls])
        if not clothing_items.exists():
            return JsonResponse({'success': False, 'error': 'No matching clothing found.'})
        # Create Outfit object
        outfit = Outfit.objects.create(user=request.user)
        outfit.clothes.set(clothing_items)
        outfit.save()
        return JsonResponse({'success': True, 'count': clothing_items.count()})
    return JsonResponse({'success': False, 'error': 'Invalid request.'})

