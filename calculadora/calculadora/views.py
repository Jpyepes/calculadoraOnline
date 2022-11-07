from django.shortcuts import render
from calculadora.metodos import Biseccion, PuntoFijo, Newton, ReglaFalsa, Secante, Gauss
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import ast
import matlab.engine

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
    tipoDeError = request.POST["tipoDeError"]

    exp = sympify(funcion, convert_xor=True)
    grafica = plot(exp, show = False)
    grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")
    
    datos = PuntoFijo(valorInicial, tolerancia, numIteracciones, funcion, funciong, tipoDeError)
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
    tipoDeError = request.POST["tipoDeError"]

    exp = sympify(funcion, convert_xor=True)
    grafica = plot(exp, show = False)
    grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

    datos = Newton(valorInicial, tolerancia, numIteracciones, funcion, tipoDeError)
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
    tipoDeError = request.POST["tipoDeError"]

    exp = sympify(funcion, convert_xor=True)
    grafica = plot(exp, show = False)
    grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

    datos = ReglaFalsa(numeroMenor, numeroMayor, tolerancia, numIteracciones, funcion, tipoDeError)
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
    tipoDeError = request.POST["tipoDeError"]

    exp = sympify(funcion, convert_xor=True)
    grafica = plot(exp, show = False)
    grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

    datos = Secante(numeroMenor, numeroMayor, tolerancia, numIteracciones, funcion, tipoDeError)
    print(datos)
    n = len(datos[0])
    filas = []
    for i in range(n):
      celdas = [datos[0][i],datos[1][i],datos[2][i],datos[3][i]] 
      filas.append(celdas)
  if datos:
    return render(request, "secante.html", {"lista": filas})
  return render(request,"secante.html")

def settingsGauss(request):
  if request.method == 'POST':
    tamaño = request.POST["tamañoMatriz"]
    pivoteo = request.POST["tipoPivoteo"]
    return render(request, "gauss.html")
  return render(request, "settingsGauss.html")

def pageGauss(request):
  SistemaResuelto = ()
  datos = ()
  if request.method == 'POST':
    matrizA = request.POST["matrizA"]
    matrizB = request.POST["matrizB"]
    tipoPivoteo = request.POST["tipoPivoteo"]

    matrizA = ast.literal_eval(matrizA)
    matrizA = [list(x) for x in matrizA]
    matrizB = ast.literal_eval(matrizB)
    matrizB = [list(x) for x in matrizB]
    datos = Gauss(matrizA, matrizB, int(tipoPivoteo))
  
  if datos:
    return render(request, "gauss.html", {"data": datos})
  return render(request, "gauss.html")

def pageFactorizacionLU(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    matrizA = request.POST["matrizA"]
    matrizB = request.POST["matrizB"]
    tamaño = request.POST["tamañoMatrizA"]
    tipoFactorizacion = request.POST["tipoFactorizacion"]
    datos = eng.LU(matrizA, matrizB, int(tamaño), int(tipoFactorizacion), nargout=3)
    print(datos)
  if datos:
    return render(request, "factorizacionLU.html", {"data": datos})
  return render(request, "factorizacionLU.html")

def pageSOR(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    matrizA = request.POST["matrizA"]
    matrizB = request.POST["matrizB"]
    matrizX0 = request.POST["matrizX0"]
    tolerancia = request.POST["tolerancia"]
    numIteraciones = request.POST["numIteraciones"]
    valorW = request.POST["valorW"]
    datos = eng.SOR(matrizX0, matrizA, matrizB, float(tolerancia), int(numIteraciones), float(valorW), nargout=3)
    print(datos)
  if datos:
    return render(request, "sor.html", {"data": datos})
  return render(request, "sor.html")

def pageJacobiGauss(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    matrizA = request.POST["matrizA"]
    matrizB = request.POST["matrizB"]
    matrizX0 = request.POST["matrizX0"]
    tolerancia = request.POST["tolerancia"]
    numIteraciones = request.POST["numIteraciones"]
    metodo = request.POST["tipoMetodo"]
    datos = eng.MatJacobiSeid(matrizX0, matrizA, matrizB, float(tolerancia), int(numIteraciones), int(metodo), nargout=3)
    print(datos)
  if datos:
    return render(request, "jacobiGauss.html", {"data": datos})
  return render(request, "jacobiGauss.html")

def pageCDC(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    matrizA = request.POST["matrizA"]
    matrizB = request.POST["matrizB"]
    metodo = request.POST["tipoMetodo"]
    datos = eng.directLU(matrizA, int(metodo), nargout=2)
    print(datos)
  if datos:
    return render(request, "croDooCho.html", {"data": datos})
  return render(request, "croDooCho.html")

def pageVandermonde(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    valoresX = request.POST["valoresX"]
    valoresY = request.POST["valoresY"]
    datos = eng.vandermonde(valoresX, valoresY, nargout=2)
    print(datos)
  if datos:
    return render(request, "vandermonde.html", {"data": datos})
  return render(request, "vandermonde.html")

def pageSpline(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    valoresX = request.POST["valoresX"]
    valoresY = request.POST["valoresY"]
    tipoDeSpline = request.POST["tipoDeSpline"]
    datos = eng.Spline(valoresX, valoresY, int(tipoDeSpline))
    print(datos)
  if datos:
    return render(request, "spline.html", {"data": datos})
  return render(request, "spline.html")

def pageGraficas(request):
  return render(request, 'graficas.html') 
