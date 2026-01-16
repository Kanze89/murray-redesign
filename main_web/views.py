from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def history(request):
    return render(request, 'history.html')

def slogan(request):
    return render(request, 'slogan.html')

def social(request):
    return render(request, 'social.html')

def executives(request):
    return render(request, 'executives.html')