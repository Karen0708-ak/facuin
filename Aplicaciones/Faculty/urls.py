from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioFaculty, name='inicioFaculty'),  # raíz de la app
    path('faculties/', views.inicioFaculty, name='inicioFaculty'),
    path('faculties/new/', views.newFaculty, name='newFaculty'),
    path('faculties/save/', views.saveFaculty, name='saveFaculty'),
    path('faculties/edit/<int:id>/', views.editFaculty, name='editFaculty'),
    path('faculties/process-edit/', views.processEditFaculty, name='processEditFaculty'),
    path('faculties/delete/<int:id>/', views.deleteFaculty, name='deleteFaculty'),
]
