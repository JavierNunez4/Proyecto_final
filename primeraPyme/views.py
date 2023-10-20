from django.shortcuts import render

# Create your views here.


def pyme1(request):
    data = {"img":"imagenes\logo_pyme.jpg"}
    return render(request, "primeraPyme/snakedreams.html",data)