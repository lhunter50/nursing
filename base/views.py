from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from base.models import Medication
from base.serializers import MedicationSerializer
# Create your views here.

class MedicationList(ListAPIView):
  queryset = Medication.objects.all()
  serializer_class = MedicationSerializer
    
class CreateMedication(CreateAPIView):
  queryset = Medication.objects.all()
  serializer_class = MedicationSerializer

class MedicationDetail(RetrieveAPIView):
  queryset = Medication.objects.all()
  serializer_class = MedicationSerializer
  lookup_url_kwarg = 'medication_id'

class MedicationUpdate(UpdateAPIView):
  queryset = Medication.objects.all()
  serializer_class = MedicationSerializer

class MedicationDelete(DestroyAPIView):
  queryset = Medication.objects.all()
  serializer_class = MedicationSerializer