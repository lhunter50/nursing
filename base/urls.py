from django.contrib import admin
from django.urls import path
from base.views import MedicationList, CreateMedication, MedicationDetail, MedicationUpdate, MedicationDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medication/', MedicationList.as_view(), name='medication-list'),
    path('medication/create/', CreateMedication.as_view(), name='create-medication'),
    path('medication/<uuid:medication_id>/', MedicationDetail.as_view(), name='medication-detail'),
    path('medication/<uuid:medication_id>/update/', MedicationUpdate.as_view(), name='medication-update'),
    path('medication/<uuid:medication_id/delete', MedicationDelete.as_view(), name='medication-delete'),
]
