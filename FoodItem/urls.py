from django.urls import path # type: ignore
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.single_food, name='single_food')
]
