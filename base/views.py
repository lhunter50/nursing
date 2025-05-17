from rest_framework.generics import ListAPIView, CreateAPIView

from base.models import Medication
from base.serializers import MedicationSerializer
# Create your views here.

class MedicationList(ListAPIView):
  queryset = Medication.objects.all()
  serializer_class = MedicationSerializer
    

class CreateMedication(CreateAPIView):
  queryset = Medication.objects.all()
  serializer_class = MedicationSerializer

