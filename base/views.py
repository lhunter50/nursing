from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def patients(request):
    return render (request, 'base/patients.html')