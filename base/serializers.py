from rest_framework import serializers
from base.models import Medication

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ['id', 'name', 'intention', 'classification', 'implications', 'dose', 'route', 'frequency']