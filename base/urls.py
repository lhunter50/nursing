from django.contrib import admin
from django.urls import path, include
from base.views import MedicationList, CreateMedication

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medication/',
         MedicationList.as_view(),
         name='medication-list'),
    path('medication/create/', CreateMedication.as_view(), name='create-medication')    
]
