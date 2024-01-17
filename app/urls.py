from django.urls import path, include
from . import views


# Create your url paths here
urlpatters = [
   path('', views.home, name=home),
]