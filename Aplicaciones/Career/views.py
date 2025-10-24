from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Career
from Aplicaciones.Faculty.models import Faculty

def inicioCareer(request):
    careers_list = Career.objects.select_related('faculty').all()
    return render(request, "inicioC.html", {'careers': careers_list})

def newCareer(request):
    faculties = Faculty.objects.all()
    return render(request, "nuevoC.html", {'faculties': faculties})

def saveCareer(request):
    faculty_id = request.POST["faculty"]                
    career_name = request.POST["career_name"]
    duration = request.POST.get("duration", "")
    career_code = request.POST.get("career_code", "")
    description = request.POST.get("description", "")
    modality = request.POST.get("modality", "")

    faculty = get_object_or_404(Faculty, id=faculty_id)
    Career.objects.create(
        career_name=career_name,
        duration=duration,
        career_code=career_code,
        description=description,
        modality=modality,
        faculty=faculty
    )
    messages.success(request, "Career created successfully")
    return redirect('inicioCareer')

def editCareer(request, id):
    career = get_object_or_404(Career, id_career=id)
    faculties = Faculty.objects.all()
    return render(request, "editarC.html", {'career': career, 'faculties': faculties})

def processEditCareer(request):
    id_career = request.POST["id_career"]
    career = get_object_or_404(Career, id_career=id_career)
    faculty = get_object_or_404(Faculty, id=request.POST["faculty"])

    career.career_name = request.POST["career_name"]
    career.duration = request.POST.get("duration", "")
    career.career_code = request.POST.get("career_code", "")
    career.description = request.POST.get("description", "")
    career.modality = request.POST.get("modality", "")
    career.faculty = faculty
    career.save()

    messages.success(request, "Career updated successfully")
    return redirect('inicioCareer')

def deleteCareer(request, id):
    career = get_object_or_404(Career, id_career=id)
    career.delete()
    messages.success(request, "Career deleted successfully")
    return redirect('inicioCareer')
