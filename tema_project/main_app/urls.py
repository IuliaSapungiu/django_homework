from django.urls import path
from main_app import views

urlpatterns = [
    path('Home', views.home, name ='Homepage'),
]
