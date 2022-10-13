from django.shortcuts import render
from calculadora.metodos import Biseccion, PuntoFijo, Newton, ReglaFalsa, Secante, Gauss
import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def index(request):
  return render(request, "index.html")

def sobreNosotros(request):
  return render(request, "sobreNosotros.html")

def pageBiseccion(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    numeroMenor = request.POST["numeroMenor"]
    numeroMayor = request.POST["numeroMayor"]
    tolerancia = request.POST["tolerancia"]
    numIteracciones = request.POST["numIteraciones"]
    
    exp = sympify(funcion, convert_xor=True)
    grafica = plot(exp, show = False)
    grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

    datos = Biseccion(numeroMenor, numeroMayor, tolerancia, numIteracciones, funcion)
    print(datos)
    n = len(datos[0])
    filas = []
    for i in range(n):
      celdas = [datos[0][i],datos[1][i],datos[2][i]] 
      filas.append(celdas)

  if datos:
    return render(request, "Bisección.html", {"lista": filas})
  return render(request, "Bisección.html")

def pagePuntoFijo(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    funciong = request.POST["funciong"]
    valorInicial = request.POST["valInicial"]
    tolerancia = request.POST["tolerancia"]
    numIteracciones = request.POST["numIteraciones"]

    exp = sympify(funcion, convert_xor=True)
    grafica = plot(exp, show = False)
    grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")
    
    datos = PuntoFijo(valorInicial, tolerancia, numIteracciones, funcion, funciong)
    print(datos)
    n = len(datos[0])
    filas = []
    for i in range(n):
      celdas = [datos[0][i],datos[1][i],datos[2][i],datos[3][i]] 
      filas.append(celdas)
  if datos:
    return render(request, "puntoFijo.html", {"lista": filas})
  return render(request, "puntoFijo.html")

def pageNewton(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    valorInicial = request.POST["valInicial"]
    tolerancia = request.POST["tolerancia"]
    numIteracciones = request.POST["numIteraciones"]

    exp = sympify(funcion, convert_xor=True)
    grafica = plot(exp, show = False)
    grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

    datos = Newton(valorInicial, tolerancia, numIteracciones, funcion)
    print(datos)
    n = len(datos[0])
    filas = []
    for i in range(n):
      celdas = [datos[0][i],datos[1][i],datos[2][i],datos[3][i]] 
      filas.append(celdas)
  if datos:
    return render(request, "newton.html", {"lista": filas})
  return render(request, "newton.html")
  
def pageReglaFalsa(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    numeroMenor = request.POST["numeroMenor"]
    numeroMayor = request.POST["numeroMayor"]
    tolerancia = request.POST["tolerancia"]
    numIteracciones = request.POST["numIteraciones"]

    exp = sympify(funcion, convert_xor=True)
    grafica = plot(exp, show = False)
    grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

    datos = ReglaFalsa(numeroMenor, numeroMayor, tolerancia, numIteracciones, funcion)
    print(datos)
    n = len(datos[0])
    filas = []
    for i in range(n):
      celdas = [datos[0][i],datos[1][i],datos[2][i],datos[3][i]] 
      filas.append(celdas)
  if datos:
    return render(request, "reglaFalsa.html", {"lista": filas})
  return render(request,"reglaFalsa.html")

def pageMetodoSecante(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    numeroMenor = request.POST["numeroMenor"]
    numeroMayor = request.POST["numeroMayor"]
    tolerancia = request.POST["tolerancia"]
    numIteracciones = request.POST["numIteraciones"]

    exp = sympify(funcion, convert_xor=True)
    grafica = plot(exp, show = False)
    grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

    datos = Secante(numeroMenor, numeroMayor, tolerancia, numIteracciones, funcion)
    print(datos)
    n = len(datos[0])
    filas = []
    for i in range(n):
      celdas = [datos[0][i],datos[1][i],datos[2][i],datos[3][i]] 
      filas.append(celdas)
  if datos:
    return render(request, "secante.html", {"lista": filas})
  return render(request,"secante.html")

def pageGauss(request):
  SistemaResuelto = ()
  datos = [1, 2, 3]
  if request.method == 'POST':
    matriz = request.POST["entradaM"]
    vector = request.POST["entradaV"]

    vectorDatos =[]
    Gauss(vectorDatos)
    print(matriz)
    print(vector)
  return render(request, "gauss.html", {"data": datos})