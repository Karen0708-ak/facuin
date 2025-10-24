from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioCareer, name='inicioCareer'),  # root of the app
    path('careers/', views.inicioCareer, name='inicioCareer'),
    path('careers/new/', views.newCareer, name='newCareer'),
    path('careers/save/', views.saveCareer, name='saveCareer'),
    path('careers/edit/<int:id>/', views.editCareer, name='editCareer'),
    path('careers/process-edit/', views.processEditCareer, name='processEditCareer'),
    path('careers/delete/<int:id>/', views.deleteCareer, name='deleteCareer'),
]
