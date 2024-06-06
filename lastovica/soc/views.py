from django.shortcuts import render
from . models import *

# Create your views here.

def index(request):
    temy = Tema.objects.all().order_by('dostupnost_id')
    ucitelia = Ucitel.objects.all()
    dostupnosti = Dostupnost.objects.all()
    odbory = Odbor.objects.all()
    return render(request, 'soc/index.html', {
        "temy" : temy,
        "ucitelia" : ucitelia,
        "dostupnosti" : dostupnosti,
        "odbory" : odbory
    })