from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Appmvt.models import Familiares


# Create your views here.

# Se genera función de vista
def listaFamiliares(request):

    dato1 = Familiares(nombre ="Branko", edad=20, fecha="06-01-2002")

    dato2 = Familiares(nombre ="Juan", edad=78, fecha="1-04-1943")

    dato3 = Familiares(nombre ="Pablo", edad=30, fecha="5-11-1992")

    return render(request, r"D:\Familiar\DSAFIO_FAMILIAR-main\Familiar\Appmvt\Templete\index.html", {"familia":[dato1,dato2,dato3]})




