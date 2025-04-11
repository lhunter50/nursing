from django.urls import path
from rest_framework.routers import DefaultRouter
from base.views import MedicationViewSet

router = DefaultRouter()
router.register(r'medications', MedicationViewSet)

urlpatterns = router.urls  # No need to manually add /api/ here; it’s handled by the base urls
