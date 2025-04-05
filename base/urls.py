from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.Home.as_view(), name='home'),
    # path('patients/', views.patients, name='patients'),

    path('medication/', views.MedicationView.as_view(), name='medication-detail'),
    path('create-med/', views.MedicationForm.as_view(), name='create-meds'),
    path('update-med/<int:pk>/', views.MedicationUpdateView.as_view(), name='medication-update'),
]