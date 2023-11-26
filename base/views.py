from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Medication
from .forms import MedForm

# Create your views here.

def home(request):
    q = request.GET.get('q', None)

    if not q:
        medications = Medication.objects.all().order_by('name')
        print(f"Searched with no query")

    else:
        medications = Medication.objects.filter(
            Q(name__icontains = q)
        ).order_by('name')
        print(f"Searched with query {q}")

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
