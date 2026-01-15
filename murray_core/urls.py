from django.contrib import admin
from django.urls import path, include  # <--- MAKE SURE 'include' IS IMPORTED

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This line tells Django: "For any other URL, go check main_web/urls.py"
    path('', include('main_web.urls')), 
]