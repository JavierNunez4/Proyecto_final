from django.shortcuts import render
from templates import *

# Create your views here.


def main(request):
    data = {"img":"imagenes\logo_pyme.jpg"}
    return render(request, "mainPage/main.html", data)

