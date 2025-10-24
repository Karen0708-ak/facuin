"""
URL configuration for facuin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Aplicaciones.Faculty import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # esto hace que al abrir 127.0.0.1:8000/ se cargue tu vista directamente
    path('', views.inicioFaculty, name='home'),

    # y este include maneja las demás rutas de Faculty
    path('Faculty/', include('Aplicaciones.Faculty.urls')),
    path('Career/', include('Aplicaciones.Career.urls')),

]
