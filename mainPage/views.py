from django.shortcuts import render
from templates import *

# Create your views here.


def main(request):
    return render(request, "mainPage/main.html")


def pyme1(request):
    return render(request, "primeraPyme/SnakeDreams.html")