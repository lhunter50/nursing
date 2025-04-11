from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, FormView, UpdateView
from rest_framework import viewsets

from .models import Medication
from .serializers import *
# from .controller import search

# Create your views here.

# class based views 
# Django REST framework
    
class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializers
    