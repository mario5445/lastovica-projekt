from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers import serialize
from . models import *

# Create your views here.

def index(request):
    temy = Tema.objects.all().order_by('dostupnost_id')
    ucitelia = Ucitel.objects.all()
    dostupnosti = Dostupnost.objects.all()
    odbory = Odbor.objects.all()
    range_filter = list(range(1, 4))

    return render(request, 'soc/index.html', {
        "temy" : temy,
        "ucitelia" : ucitelia,
        "dostupnosti" : dostupnosti,
        "odbory" : odbory,
        "range_filter" : range_filter
    })

def nova_tema(request):
    if request.method == "GET":
        ucitelia = Ucitel.objects.all()
        odbory = Odbor.objects.all()
        return render(request, "soc/new.html", {
            "ucitelia" : ucitelia,
            "odbory" : odbory
        })
    elif request.method == "POST":
        data = request.POST
        nazov = data.get('nazov').strip() 
        popis = data.get('popis').strip()
        konzultant = Ucitel.objects.get(pk=data.get('konzultant')) 
        odbor = Odbor.objects.get(pk= data.get('odbor'))
        tema = Tema(nazov=nazov, popis=popis, konzultant=konzultant, odbor=odbor)
        tema.save()
        return redirect(index)

def ucitel(request, pk):
    ucitel = get_object_or_404(Ucitel, id=pk)
    temy = Tema.objects.filter(konzultant=ucitel)
    range_filter = list(range(1, 4))
    return render(request, "soc/teacher.html", {
        "ucitel" : ucitel,
        "temy" : temy,
        "range_filter" : range_filter
    })

def student(request, pk):
    student = get_object_or_404(Student, id=pk)
    temy = Tema.objects.filter(student=student)
    range_filter = list(range(1,4))
    return render(request, 'soc/student.html', {
        "student" : student,
        "temy" : temy,
        "range_filter" : range_filter
    })