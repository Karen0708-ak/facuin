from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicioTeacher, name='inicioTeacher'),
    path('teachers/', views.inicioTeacher, name='inicioTeacher'),
    path('teachers/new/', views.newTeacher, name='newTeacher'),
    path('teachers/save/', views.saveTeacher, name='saveTeacher'),
    path('teachers/edit/<int:id>/', views.editTeacher, name='editTeacher'),
    path('teachers/process-edit/', views.processEditTeacher, name='processEditTeacher'),
    path('teachers/delete/<int:id>/', views.deleteTeacher, name='deleteTeacher'),
]
