from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, FormView, UpdateView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Medication
from .forms import MedForm
from .serializers import *
# from .controller import search

# Create your views here.

# class based views 
# Django REST framework

class Home(ListView):
    template_name = 'base/home.html'
    model = Medication
    context_object_name = 'medications'
    ordering = ['name']
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        object_list = super(Home, self).get_queryset(*args, **kwargs)
        search = self.request.GET.get('q', None)
        if search:
            object_list = object_list.filter(name__icontains = search)
        return object_list
    
@api_view(['GET', 'POST'])
def medication_list(request):
    if request.method == 'GET':
        data = Medication.objects.all()

        serializer = MedicationSerializers(data, context={'reqest': request}, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MedicationSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT', 'DELETE'])
def medication_detail(request, pk):
    try:
        medication = Medication.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = MedicationSerializers(medication, data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        medication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MedicationView(ListView):
    template_name = 'base/medication.html'
    model = Medication
    context_object_name = 'medication'

class MedicationForm(FormView):
    template_name = 'base/meds_form.html'
    form_class = MedForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MedicationUpdateView(UpdateView):
    form_class = MedForm
    template_name = 'base/meds_form.html'
    model = Medication
    success_url='/'


    def get(self, request, **kwargs):
        self.object = Medication.objects.get(id=self.kwargs['pk'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)
    
    def get_object(self, queryset=None):
        obj = Medication.objects.get(id=self.kwargs['pk'])
        return obj