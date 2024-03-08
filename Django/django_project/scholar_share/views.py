from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'scholar_share/home.html')

def academic_integrity(request):
    return render(request, 'scholar_share/academic_integrity.html')