from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='scholar_share-home'),
    path('academic_integrity/',views.academic_integrity, name='scholar_share-academic_integrity'),
    path('civil_engineering/',views.civil_engineering, name='scholar_share-civil_engineering'),
    path('software_engineering/',views.software_engineering, name='scholar_share-software_engineering'),
    path('mechanical_engineering/',views.mechanical_engineering, name='scholar_share-mechanical_engineering'),
    path('chemical_engineering/',views.chemical_engineering, name='scholar_share-mechanical_engineering'),
    path('industrial_engineering/',views.industrial_engineering, name='scholar_share-industrial_engineering')
]