from django.shortcuts import render
from calculadora.metodos import Biseccion

def index(request):
  return render(request, "index.html")

def pageBiseccion(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    numeroMenor = request.POST["numeroMenor"]
    numeroMayor = request.POST["numeroMayor"]
    tolerancia = request.POST["tolerancia"]
    numIteracciones = request.POST["numIteraciones"]
    
    datos = Biseccion(numeroMenor, numeroMayor, tolerancia, numIteracciones, funcion)
  print(datos)
  if datos:
    return render(request, "Bisección.html", {"lista": datos})
  return render(request, "Bisección.html")