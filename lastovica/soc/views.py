import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from . models import *

# Create your views here.

def index(request):
    temy = Tema.objects.all().order_by('dostupnost_id', "nazov")
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
    if request.method == "GET":
        ucitel = get_object_or_404(Ucitel, id=pk)
        temy = Tema.objects.filter(konzultant=ucitel).order_by("dostupnost_id", "nazov")
        range_filter = list(range(1, 4))
        return render(request, "soc/teacher.html", {
            "ucitel" : ucitel,
            "temy" : temy,
            "range_filter" : range_filter
        })

def student(request, pk):
    student = get_object_or_404(Student, id=pk)
    temy = Tema.objects.filter(student=student).order_by("dostupnost_id", "nazov")
    range_filter = list(range(1,4))
    return render(request, 'soc/student.html', {
        "student" : student,
        "temy" : temy,
        "range_filter" : range_filter
    })

def tema(request, pk):
    tema = get_object_or_404(Tema, id=pk)
    range_filter = list(range(1,4))
    return render(request, 'soc/topic.html', {
        "tema" : tema,
        "range_filter" : range_filter
    })

def statistiky(request):
    pocet_tem = Tema.objects.count()
    dostupnosti = Dostupnost.objects.annotate(temy=Count('tema'))
    studenti = Student.objects.count()
    ucitelia = Ucitel.objects.count()
    return render(request, 'soc/statistics.html', {
        "pocet_tem" : pocet_tem,
        "dostupnosti" : dostupnosti,
        "studenti" : studenti, 
        "ucitelia" : ucitelia
    })

def update_konzultacie(request):
    if request.method == 'POST':
        try: 
            data = json.loads(request.body)
            id = data['id']
            value = data['value']

            tema = Tema.objects.get(pk=id)
            tema.pocet_konzultacii = value
            tema.save()
            return JsonResponse({'status' : 'success'})
        except Tema.DoesNotExist:
            return JsonResponse({'status' : 'error', 'message' : 'Model not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status' : 'error', 'message' : str(e)}, status=404)
            