from django.urls import path, include
from . import views


# Create your url paths here
urlpatterns = [
   path('', views.home, name='home'),
]