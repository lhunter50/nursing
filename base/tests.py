from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Medication
from .serializers import MedicationSerializers

# Create your tests here.

class MedicationModelTest(TestCase):
  
  def setUp(self):
    Medication.objects.create(
      name= 'Tyenol', intention= 'Headaches', classification= 'Idk what it is', implications= 'Liver problems',dose= '2 pills', route= 'PO', frequency= 'Daily',
    )
  
  def test_medication_name(self):
    medication = Medication.objects.get(name='Tyenol')
    self.assertEqual(medication.name, 'Tyenol')

  def test_medication_intention(self):
    medication = Medication.objects.get(intention='Headaches')
    self.assertEqual(medication.intention, 'Headaches')

  def test_medication_classification(self):
    medication = Medication.objects.get(classification='Idk what it is')
    self.assertEqual(medication.classification, 'Idk what it is')

  def test_medication_implications(self):
    medication = Medication.objects.get(implications='Liver problems')
    self.assertEqual(medication.implications, 'Liver problems')

  def test_medication_dose(self):
    medication = Medication.objects.get(dose='2 pills')
    self.assertEqual(medication.dose, '2 pills')

  def test_medication_route(self):
    medication = Medication.objects.get(route='PO')
    self.assertEqual(medication.route, 'PO')

  def test_medication_frequency(self):
    medication = Medication.objects.get(frequency='Daily')
    self.assertEqual(medication.frequency, 'Daily')


class MedicationViewsTest(APITestCase):
  @classmethod
  def setUpTestData(cls):
    cls.medications = [
      Medication.objects.create(
        name=f"Med {i}",
        intention="Pain relief",
        classification="Analgesic",
        implications="Drowsiness",
        dose="1 pill",
        route="PO",
        frequency="Daily"
      ) for i in range(3)
    ]
    cls.medication = cls.medications[0]

  def test_can_list_all_medications(self):
    response = self.client.get('/api/medications/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), len(self.medications))

  def test_can_get_one_medication(self):
    response = self.client.get(f'/api/medications/{self.medication.id}/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['name'], self.medication.name)

  def test_can_create_medication(self):
    data = {
      'name': 'New Med',
      'intention': 'Allergy Relief',
      'classification' : 'Something',
      'implications' : 'Prob Tired',
      'dose' : '300pills', 
      'route' : 'PO',
      'frequency' : 'Hourly'
    }
    response = self.client.post('/api/medications/', data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Medication.objects.count(), 4)

  def test_can_update_medication(self):
    url = f'/api/medications/{self.medication.id}/'
    data = {
      'name' : 'Updated Name',
      'intention' : self.medication.intention,
      'classification' : self.medication.classification,
      'implications' : self.medication.implications,
      'dose' : self.medication.dose,
      'route' : self.medication.route,
      'frequency' : self.medication.frequency
    }
    response = self.client.put(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    self.medication.refresh_from_db()
    self.assertEqual(self.medication.name, 'Updated Name')

  def test_can_delete_medication(self):
    response = self.client.delete(f'/api/medications/{self.medication.id}/')
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertFalse(Medication.objects.filter(id=self.medication.id).exists())


class MedicationSerializerTest(APITestCase):
  @classmethod
  def setUpTestData(cls):
    cls.medications = [
      Medication.objects.create(
        name=f"Med {i}",
        intention="Pain relief",
        classification="Analgesic",
        implications="Drowsiness",
        dose="1 pill",
        route="PO",
        frequency="Daily"
      ) for i in range(3)
    ]
    cls.medication = cls.medications[0]

  def test_serializer_valid_data(self):
    data = {
      'name': 'New Med',
      'intention': 'Allergy Relief',
      'classification' : 'Something',
      'implications' : 'Prob Tired',
      'dose' : '300pills', 
      'route' : 'PO',
      'frequency' : 'Hourly'
    }

    serializer = MedicationSerializers(data=data)

    self.assertTrue(serializer.is_valid())

    self.assertEqual(serializer.validated_data['name'], 'New Med')


  def test_serializer_invalid_data(self):
      data = {
        'name': 'New Med',
        'intention': 'Allergy Relief',
        'classification' : 'Something',
        'implications' : 'Prob Tired',
        'dose' : '300pills', 
        'route' : 'PO',
        # 'frequency' : 'Hourly'
      }
      
      serializer = MedicationSerializers(data=data)
      self.assertFalse(serializer.is_valid())
      self.assertIn('frequency', serializer.errors)

  def test_serializer_create_instance(self):
      data = {
        'name': 'New Med',
        'intention': 'Allergy Relief',
        'classification' : 'Something',
        'implications' : 'Prob Tired',
        'dose' : '300pills', 
        'route' : 'PO',
        'frequency' : 'Hourly'
      }

      serializer = MedicationSerializers(data=data)
      self.assertTrue(serializer.is_valid())

      instance = serializer.save()

      self.assertEqual(instance.name, 'New Med')
      self.assertEqual(instance.intention, 'Allergy Relief')
      self.assertEqual(instance.classification, 'Something')
      self.assertEqual(instance.implications, 'Prob Tired')
      self.assertEqual(instance.dose, '300pills')
      self.assertEqual(instance.route, 'PO')
      self.assertEqual(instance.frequency, 'Hourly')

  def test_serializer_update_instance(self):
    data = {
        'name': 'Updated Med',
        'intention': 'Updated Intention',
        'classification' : 'Updated Classification',
        'implications' : 'Updated Implications',
        'dose' : 'Updated Dose', 
        'route' : 'Updated Route',
        'frequency' : 'Updated Frequency'
      }
    
    serializer = MedicationSerializers(instance=self.medication, data=data)
    self.assertTrue(serializer.is_valid())

    updated_instance = serializer.save()

    self.assertEqual(updated_instance.name, 'Updated Med')
    self.assertEqual(updated_instance.intention, 'Updated Intention')
    self.assertEqual(updated_instance.classification, 'Updated Classification')
    self.assertEqual(updated_instance.implications, 'Updated Implications')
    self.assertEqual(updated_instance.dose, 'Updated Dose')
    self.assertEqual(updated_instance.route, 'Updated Route')
    self.assertEqual(updated_instance.frequency, 'Updated Frequency')
