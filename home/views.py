from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Registration, Gallery
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def gallery(request):
    if request.method == "POST":
        title= request.POST.get('title')
        detail= request.POST.get('detail')
        gallery = gallery(title=title, detail=detail)
        gallery.save()
        messages.success(request, 'Your message has been sent..!')
    return render(request, 'gallery.html')

def pricing(request):
    return render(request, 'pricing.html')

def myaccount(request):
    return render(request, 'login.html')

def registration(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        registration = Registration(name=name, email=email, phone=phone, date=datetime.today())
        registration.save()
        messages.success(request, 'Your message has been sent..!')

    return render(request, 'registration.html')


