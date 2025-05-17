from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from .models import Medication
from .serializers import MedicationSerializer
# Create your views here.
    

@csrf_exempt
def medication_list(request):
  """
   List all medication, or create a new medication 
  """

  if request.method == 'GET':
    medication = Medication.objects.all()
    serializer = MedicationSerializer(medication, many=True)
    return JsonResponse(serializer.data, safe=False)
  
  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = MedicationSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)
  
@csrf_exempt
def medication_detail(request, pk):
  # Check to see if the medication exists before continuing using the primary key
  try:
    # Pull the single medication
    medication = Medication.objects.get(pk)
  except Medication.DoesNotExist:
    # If the medication doesn't exist we return error 404, does not exist.
    return HttpResponse(status=404)
  
  # GET
  if request.method == 'GET':
    serializer = MedicationSerializer(medication)
    return JsonResponse(serializer.data)

  # PUT (update)
  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = MedicationSerializer(medication, data=data)

    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

  # DELETE
  elif request.method == 'DELETE':
    medication.delete()
    return HttpResponse(status=204)
