from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, FormView

from .models import Medication
from .forms import MedForm
# from .controller import search

# Create your views here.

# class based views 
# Django REST framework

class Home(ListView):
    template_name = 'base/home.html'
    model = Medication
    context_object_name = 'medications'
    ordering = ['name']

    def get_queryset(self, *args, **kwargs):
        object_list = super(Home, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get('q', None)
        if search:
            object_list = object_list.filter(name__icontains = search)
        return object_list

class MedicationForm(FormView):
    template_name = 'base/meds_form.html'
    form_class = MedForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
