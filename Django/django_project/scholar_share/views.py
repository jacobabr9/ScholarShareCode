from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'scholar_share/home.html')

def academic_integrity(request):
    return render(request, 'scholar_share/academic_integrity.html')

def about_us(request):
    return render(request, 'scholar_share/about_us.html')

def contact_us(request):
    return render(request, 'scholar_share/contact_us.html')

def upload_resources_page(request):
    return render(request, 'scholar_share/upload_resources_page.html')

def civil_engineering(request):
    return render(request, 'scholar_share/civil_engineering.html')

def software_engineering(request):
    return render(request, 'scholar_share/software_engineering.html')

def mechanical_engineering(request):
    return render(request, 'scholar_share/mechanical_engineering.html')

def chemical_engineering(request):
    return render(request, 'scholar_share/chemical_engineering.html')

def industrial_engineering(request):
    return render(request, 'scholar_share/industrial_engineering.html')

def biochemistry_page(request):
    return render(request, 'scholar_share/biochemistry_page.html')

def biology_page(request):
    return render(request, 'scholar_share/biology_page.html')

def chemistry_page(request):
    return render(request, 'scholar_share/chemistry_page.html')

def earth_space_page(request):
    return render(request, 'scholar_share/earth_space_page.html')

def physics_page(request):
    return render(request, 'scholar_share/physics_page.html')