from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Medication

def get(request):
    q = request.GET.get('q', None)

    if not q:
        medications = Medication.objects.all().order_by('name')

    else:
        medications = Medication.objects.filter(
            Q(name__icontains = q)
        ).order_by('name')

    context = {'medications': medications}
    return render(request, 'base/home.html', context)

def post(self, request):
    pass

