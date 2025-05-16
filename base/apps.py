from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    
    def ready(self):
        from .models import Category
        defaults = ['Top', 'Bottom', 'Shoe', 'Accessory', 'Hat']
        try: 
            for name in defaults:
                Category.objects.get_or_create(name=name.strip().title())
        except (OperationalError, ProgrammingError):
            pass