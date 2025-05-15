from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Clothing

class SingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
        widgets = {
            "username": forms.TextInput(attrs={"class": "w-full rounded border px-4 py-2"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({"class": "w-full rounded border px-4 py-2"})
        self.fields['password2'].widget.attrs.update({"class": "w-full rounded border px-4 py-2"})

class addClothingForm(ModelForm):
    class Meta:
        model = Clothing
        fields = ['name', 'brand', 'description', 'isFavorite', 'image', 'category']