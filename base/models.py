from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Clothing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    isFavorite = models.BooleanField(default=False)
    image = models.ImageField(upload_to='clothing_images', null=False, blank=False, default='clothing_images/default.jpg')

    def __str__(self):
        return self.name

class Outfit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    clothes = models.ManyToManyField(Clothing, related_name='outfits')
    date = models.DateField(blank=True, null=True)  # New attribute for scheduling

    def __str__(self):
        return self.name or f"Outfit {self.pk}"
