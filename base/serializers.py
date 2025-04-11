from rest_framework import serializers
from .models import Medication

class MedicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'name', 'classification', 'implications', 'dose', 'route', 'frequency']