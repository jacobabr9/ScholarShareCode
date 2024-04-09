from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='scholar_share-home'),
    path('home/',views.homepage, name='scholar_share-home'),
    path('academic_integrity/',views.academic_integrity, name='scholar_share-academic_integrity'),
    path('about_us/',views.about_us, name='scholar_share-about_us'),
    path('contact_us/',views.contact_us, name='scholar_share-contact_us'),
    path('faq/',views.faq, name='scholar_share-faq'),
    path('upload_resources_page/',views.upload_resources_page, name='scholar_share-upload_resources_page'),
    path('civil_engineering/',views.civil_engineering, name='scholar_share-civil_engineering'),
    path('software_engineering/',views.software_engineering, name='scholar_share-software_engineering'),
    path('mechanical_engineering/',views.mechanical_engineering, name='scholar_share-mechanical_engineering'),
    path('chemical_engineering/',views.chemical_engineering, name='scholar_share-mechanical_engineering'),
    path('industrial_engineering/',views.industrial_engineering, name='scholar_share-industrial_engineering'),
    path('electrical_engineering/',views.electrical_engineering, name='scholar_share-electrical_engineering'),
    path('biochemistry_page/',views.biochemistry_page, name='scholar_share-biochemistry_page'),
    path('biology_page/',views.biology_page, name='scholar_share-biology_page'),
    path('chemistry_page/',views.chemistry_page, name='scholar_share-chemistry_page'),
    path('earth_space_page/',views.earth_space_page, name='scholar_share-earth_space_page'),
    path('physics_page/',views.physics_page, name='scholar_share-physics_page'),
    path('algebra/',views.algebra, name='scholar_share-algebra_page'),
    path('applied_mathematics/',views.applied_mathematics, name='scholar_share-applied_mathematics_page'),
    path('calculus/',views.calculus, name='scholar_share-calculus_page'),
    path('computational_mathematics/',views.computational_mathematics, name='scholar_share-computational_mathematics_page'),
    path('geometry/',views.geometry, name='scholar_share-geometry_page'),
    path('probability_and_statistics/',views.probability_and_statistics, name='scholar_share-probability_and_statistics_page'),
    path('information_management_page/',views.information_management_page, name='scholar_share-information_management_page'),
    path('information_technology_page',views.information_technology_page, name='scholar_share-information_technology_page'),
    # path('login/', views.login, name='login')
]