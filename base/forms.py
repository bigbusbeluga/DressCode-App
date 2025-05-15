from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        labels = {
            'isFavorite': 'Add to Favorites?',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full rounded border px-4 py-2'}),
            'brand': forms.TextInput(attrs={'class': 'w-full rounded border px-4 py-2'}),
            'description': forms.Textarea(attrs={'class': 'w-full rounded border px-4 py-2', 'rows': 2}),
            'isFavorite': forms.CheckboxInput(attrs={'class': 'rounded border px-4 py-2'}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full text-sm text-slate-500 rounded border file:cursor-pointer cursor-pointer file:border-0 file:py-3 file:px-4 file:mr-4 file:bg-gray-100'}),
            'category': forms.Select(attrs={'class': 'w-full rounded border px-4 py-2'}),
        }
