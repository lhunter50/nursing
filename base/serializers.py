from rest_framework import serializers
from .models import Medication

class MedicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ('pk', 'name', 'classification', 'intention', 'implications', 'dose', 'route', 'frequency')