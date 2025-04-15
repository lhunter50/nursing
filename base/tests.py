from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Medication

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