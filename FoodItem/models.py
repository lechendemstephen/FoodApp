from django.db import models # type: ignore
from django.urls import reverse # type: ignore
# Create your models here.

class FoodItem(models.Model): 
    name = models.CharField(max_length=50)
    des = models.TextField(max_length=100)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='food/',)
    slug = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)


    def food_url(self): 
        return reverse('single_food', args=[self.slug])


    def __str__(self): 
        return self.name