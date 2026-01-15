from django.urls import path
from . import views

# This list defines the URLs specifically for this app
urlpatterns = [
    path('', views.home, name='home'),       # Homepage
    path('contact/', views.contact, name='contact'), # Contact page
]