from django.shortcuts import render, redirect
from .models import Faculty
from django.contrib import messages

def inicioFaculty(request):
    faculties_list = Faculty.objects.all()
    return render(request, "inicioF.html", {'faculties': faculties_list})

def newFaculty(request):
    return render(request, "nuevoF.html")

def saveFaculty(request):
    name = request.POST["name"]
    acronym = request.POST["acronym"]
    dean_name = request.POST["dean_name"]
    phone = request.POST["phone"]
    email = request.POST["email"]
    year_foundation = request.POST["year_foundation"]

    Faculty.objects.create(
        name=name,
        acronym=acronym,
        dean_name=dean_name,
        phone=phone,
        email=email,
        year_foundation=year_foundation
    )
    messages.success(request, "Faculty created successfully")
    return redirect('inicioFaculty')

def editFaculty(request, id):
    faculty_to_edit = Faculty.objects.get(id=id)
    return render(request, "editarF.html", {'faculty': faculty_to_edit})

def processEditFaculty(request):
    id = request.POST["id"]
    name = request.POST["name"]
    acronym = request.POST["acronym"]
    dean_name = request.POST["dean_name"]
    phone = request.POST["phone"]
    email = request.POST["email"]
    year_foundation = request.POST["year_foundation"]

    faculty = Faculty.objects.get(id=id)

    faculty.name = name
    faculty.acronym = acronym
    faculty.dean_name = dean_name
    faculty.phone = phone
    faculty.email = email
    faculty.year_foundation = year_foundation

    faculty.save()
    messages.success(request, "Faculty updated successfully")
    return redirect('inicioFaculty')

def deleteFaculty(request, id):
    faculty_to_delete = Faculty.objects.get(id=id)
    faculty_to_delete.delete()
    messages.success(request, "Faculty deleted successfully")
    return redirect('inicioFaculty')
