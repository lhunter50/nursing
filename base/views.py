from django.shortcuts import render, redirect
from .models import Medication
from .forms import MedForm

# Create your views here.

def home(request):
    medications = Medication.objects.all()

    context = {'medications': medications}
    return render(request, 'base/home.html', context)

def patients(request):
    return render (request, 'base/patients.html')

def medication(request,pk):
    medications = Medication.objects.get(id=pk)
    context = {'medications': medications}
    return render(request, 'base/medication.html', context)


def createMed(request):
    form = MedForm()

    if request.method == "POST":
        form = MedForm(request.POST)
        if form.is_valid():
            meds = form.save(commit=False)
            meds.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/meds_form.html', context)
