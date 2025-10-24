from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Teacher
from Aplicaciones.Career.models import Career

def inicioTeacher(request):
    teachers = Teacher.objects.select_related('career').all()
    return render(request, "inicioT.html", {"teachers": teachers})

def newTeacher(request):
    careers = Career.objects.all()
    return render(request, "nuevoT.html", {"careers": careers})

def saveTeacher(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST.get("email", "")
    phone = request.POST.get("phone", "")
    specialty = request.POST.get("specialty", "")
    academic_degree = request.POST.get("academic_degree", "")
    career_id = request.POST.get("career")  # select
    photo = request.FILES.get("photo")

    career = Career.objects.get(id_career=career_id) if career_id else None

    Teacher.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email or None,
        phone=phone or None,
        specialty=specialty or None,
        academic_degree=academic_degree or None,
        career=career,
        photo=photo
    )
    messages.success(request, "Teacher created successfully")
    return redirect("inicioTeacher")

def editTeacher(request, id):
    teacher = get_object_or_404(Teacher, professor_id=id)
    careers = Career.objects.all()
    return render(request, "editarT.html", {"teacher": teacher, "careers": careers})

def processEditTeacher(request):
    professor_id = request.POST["professor_id"]
    teacher = get_object_or_404(Teacher, professor_id=professor_id)

    teacher.first_name = request.POST["first_name"]
    teacher.last_name = request.POST["last_name"]
    teacher.email = request.POST.get("email", "") or None
    teacher.phone = request.POST.get("phone", "") or None
    teacher.specialty = request.POST.get("specialty", "") or None
    teacher.academic_degree = request.POST.get("academic_degree", "") or None

    career_id = request.POST.get("career")
    teacher.career = Career.objects.get(id_career=career_id) if career_id else None

    new_photo = request.FILES.get("photo")
    if new_photo:
        teacher.photo = new_photo

    teacher.save()
    messages.success(request, "Teacher updated successfully")
    return redirect("inicioTeacher")

def deleteTeacher(request, id):
    teacher = get_object_or_404(Teacher, professor_id=id)
    teacher.delete()
    messages.success(request, "Teacher deleted successfully")
    return redirect("inicioTeacher")
