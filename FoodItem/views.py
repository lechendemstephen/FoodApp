from django.shortcuts import render, HttpResponse # type: ignore
from .models import FoodItem
# Create your views here.

def home(request): 
    fooditem = FoodItem.objects.all()

    context = {
        'fooditems': fooditem,
    }

    return render(request, 'FoodApp/pages/home.html', context)

def single_food(request, slug): 
    fooditem = FoodItem.objects.get(slug=slug)

    context = {
        'fooditem': fooditem,
    }


    return render(request, 'FoodApp/pages/single_food.html', context)