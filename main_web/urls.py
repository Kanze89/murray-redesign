from django.urls import path
from . import views

# This list defines the URLs specifically for this app
urlpatterns = [
    path('', views.home, name='home'),       # Homepage
    path('contact/', views.contact, name='contact'), # Contact page
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('slogan/', views.slogan, name='slogan'),
    path('social/', views.social, name='social'),
]