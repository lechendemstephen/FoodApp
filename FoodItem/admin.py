from django.contrib import admin # type: ignore
from .models import FoodItem
# Register your models here.

class FoodItemAdmin(admin.ModelAdmin): 
    list_display = ('name', 'des', 'author', 'image', 'slug', 'created_date')
    prepopulated_fields = {
        'slug': ('name',),
    }



admin.site.register(FoodItem, FoodItemAdmin)



