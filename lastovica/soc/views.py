from django.shortcuts import render
from . models import *

# Create your views here.

def index(request):
    temy = Tema.objects.all()
    return render(request, 'soc/index.html', {
        "temy" : temy,
    })