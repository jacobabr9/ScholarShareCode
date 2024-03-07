from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='scholar_share-home'),
    path('academic_integrity/',views.academic_integrity, name='scholar_share-academic_integrity')
]