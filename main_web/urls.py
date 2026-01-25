from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('history/', views.history, name='history'),
    path('slogan/', views.slogan, name='slogan'),
    path('social/', views.social, name='social'),
    
    # ADD THIS LINE:
    path('executives/', views.executives, name='executives'),
]