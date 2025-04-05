from django.forms import ModelForm
from .models import Medication

class MedForm(ModelForm):
    class Meta:
        model = Medication
        fields = '__all__'