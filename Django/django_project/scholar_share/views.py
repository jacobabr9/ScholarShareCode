from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'scholar_share/home.html')

def homepage(request):
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

def electrical_engineering(request):
    return render(request, 'scholar_share/electrical_engineering.html')

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

def algebra(request):
    return render(request, 'scholar_share/algebra.html')

def applied_mathematics(request):
    return render(request, 'scholar_share/applied_mathematics.html')

def calculus(request):
    return render(request, 'scholar_share/calculus.html')

def computational_mathematics(request):
    return render(request, 'scholar_share/computational_mathematics.html')

def geometry(request):
    return render(request, 'scholar_share/geometry.html')

def probability_and_statistics(request):
    return render(request, 'scholar_share/probability_and_statistics.html')

def information_management_page(request):
    return render(request, 'scholar_share/information_management_page.html')

def information_technology_page(request):
    return render(request, 'scholar_share/information_technology_page.html')