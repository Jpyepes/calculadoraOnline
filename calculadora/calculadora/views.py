from django.shortcuts import render
from calculadora.metodos import Biseccion, PuntoFijo, Newton, ReglaFalsa, Secante, Gauss,RaicesMultiples, busquedasIncrementales
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import ast
import matlab.engine

def index(request):
  return render(request, "index.html")

def sobreNosotros(request):
  return render(request, "sobreNosotros.html")

def pageBusquedasIncrementales(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    numeroInicial = request.POST["numeroInicial"]
    delta = request.POST["delta"]
    numIteracciones = request.POST["numIteraciones"]
    try:
      datos = busquedasIncrementales(numeroInicial, delta, numIteracciones, funcion)
      print(datos)
    except:
      error = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "BI.html", {"error":error})

  if datos:
    print(datos)
    if datos[0] == 'F':
      return render(request, "BI.html", {"error": datos})
    else:
      return render(request, "BI.html", {"lista": datos})
  return render(request, "BI.html")

def pageBiseccion(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    numeroMenor = request.POST["numeroMenor"]
    numeroMayor = request.POST["numeroMayor"]
    tolerancia = request.POST["tolerancia"]
    numIteracciones = request.POST["numIteraciones"]

    try:
      exp = sympify(funcion, convert_xor=True)
      grafica = plot(exp, show = False)
      grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

      datos = Biseccion(numeroMenor, numeroMayor, tolerancia, numIteracciones, funcion)
      print(datos)
    except:
      error = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "Bisección.html", {"error":error})

    if datos:
      if type(datos) is not str:
        n = len(datos[0])
        filas = []
        for i in range(n):
          celdas = [datos[0][i],datos[1][i],datos[2][i]] 
          filas.append(celdas)
        return render(request, "Bisección.html", {"lista": filas, "msg":datos[-1]})
      else:
        return render(request, "Bisección.html", {"error": datos})

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
    
    try:
      exp = sympify(funcion, convert_xor=True)
      grafica = plot(exp, show = False)
      grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

      datos = PuntoFijo(valorInicial, tolerancia, numIteracciones, funcion, funciong, tipoDeError)
      print(datos)
    except:
      error = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "puntoFijo.html", {"error":error})

    if datos:
      if type(datos) is not str:
        n = len(datos[0])
        filas = []
        for i in range(n):
          celdas = [datos[0][i],datos[1][i],datos[2][i],datos[3][i]] 
          filas.append(celdas)
        return render(request, "puntoFijo.html", {"lista": filas, "msg":datos[-1]})
      else:
        return render(request, "puntoFijo.html", {"error":datos})
  return render(request, "puntoFijo.html")

def pageNewton(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    valorInicial = request.POST["valInicial"]
    tolerancia = request.POST["tolerancia"]
    numIteracciones = request.POST["numIteraciones"]
    tipoDeError = request.POST["tipoDeError"]

    try:
      exp = sympify(funcion, convert_xor=True)
      grafica = plot(exp, show = False)
      grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

      datos = Newton(valorInicial, tolerancia, numIteracciones, funcion, tipoDeError)
    except:
      error = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "newton.html", {"error":error})
    
    if datos:
      if type(datos) is not str:
        #print(datos)
        n = len(datos[0])
        filas = []
        for i in range(n):
          celdas = [datos[0][i],datos[1][i],datos[2][i],datos[3][i]] 
          filas.append(celdas)
        return render(request, "newton.html", {"lista": filas, "msg":datos[-1]})
      else:
        return render(request, "newton.html", {"error":datos})
  return render(request, "newton.html")

def pageRaicesMultiples(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    derivada = request.POST["derivada"]
    derivada2 = request.POST["derivada2"]
    valorInicial = request.POST["valInicial"]
    tolerancia = request.POST["tolerancia"]
    numIteracciones = request.POST["numIteraciones"]
    tipoDeError = request.POST["tipoDeError"]

    try:
      exp = sympify(funcion, convert_xor=True)
      grafica = plot(exp, show = False)
      grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

      datos = RaicesMultiples(valorInicial, tolerancia, numIteracciones, funcion, derivada, derivada2,tipoDeError)
      #print(datos)
    except:
      error = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "raicesMultiples.html", {"error":error})

    if datos:
      if type(datos) is not str:
        n = len(datos[0])
        filas = []
        for i in range(n):
          celdas = [datos[0][i],datos[1][i],datos[2][i],datos[3][i]] 
          filas.append(celdas)
        return render(request, "raicesMultiples.html", {"lista": filas, "msg":datos[-1]})
      else:
        return render(request, "raicesMultiples.html", {"error": datos})

  return render(request, "raicesMultiples.html")
  
def pageReglaFalsa(request):
  datos = ()
  if request.method == 'POST':
    funcion = request.POST["funcion"]
    numeroMenor = request.POST["numeroMenor"]
    numeroMayor = request.POST["numeroMayor"]
    tolerancia = request.POST["tolerancia"]
    numIteracciones = request.POST["numIteraciones"]
    tipoDeError = request.POST["tipoDeError"]

    try:
      exp = sympify(funcion, convert_xor=True)
      grafica = plot(exp, show = False)
      grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

      datos = ReglaFalsa(numeroMenor, numeroMayor, tolerancia, numIteracciones, funcion, tipoDeError)
      #print(datos)
    except:
      error = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "reglaFalsa.html", {"error":error})

    if datos:
      if type(datos) is not str:
        n = len(datos[0])
        filas = []
        for i in range(n):
          celdas = [datos[0][i],datos[1][i],datos[2][i],datos[3][i]] 
          filas.append(celdas)
          return render(request, "reglaFalsa.html", {"lista": filas, "msg": datos[-1]})
      else:
          return render(request, "reglaFalsa.html", {"error": datos})  
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

    try:
      exp = sympify(funcion, convert_xor=True)
      grafica = plot(exp, show = False)
      grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")

      datos = Secante(numeroMenor, numeroMayor, tolerancia, numIteracciones, funcion, tipoDeError)
      #print(datos)
    except:
      error = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "secante.html", {"error":error})

    if datos:
      if type(datos) is not str:   
        n = len(datos[0])
        filas = []
        for i in range(n):
          celdas = [datos[0][i],datos[1][i],datos[2][i],datos[3][i]] 
          filas.append(celdas)
        return render(request, "secante.html", {"lista": filas, "msg":datos[-1]})
      else:
        return render(request, "secante.html", {"error":datos})
  return render(request,"secante.html")

def settingsGauss(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    matrizA = request.POST["matrizA"]
    matrizB = request.POST["matrizB"]
    tamaño = request.POST["tamaño"]
    tipoPivoteo = request.POST["tipoPivoteo"]

    try:
      datos = eng.GaussPiv(matrizA, matrizB, int(tamaño), int(tipoPivoteo))
      print(datos)
    except:
      msg = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "gauss.html", {"msg": msg})
      
  if datos:
      return render(request, "gauss.html", {"data": datos})
  return render(request, "gauss.html")

def pageGauss(request):
  datos = ()
  if request.method == 'POST':
    matrizA = request.POST["matrizA"]
    matrizB = request.POST["matrizB"]
    tipoPivoteo = request.POST["tipoPivoteo"]

    matrizA = ast.literal_eval(matrizA)
    matrizA = [list(x) for x in matrizA]
    matrizB = ast.literal_eval(matrizB)
    matrizB = [list(x) for x in matrizB]
    print(tipoPivoteo)

    try:
      datos = Gauss(matrizA, matrizB, int(tipoPivoteo))
      print(datos)
    except:
      msg = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "gauss.html", {"msg": msg})
    tamaño = 4
  
  if datos:
    return render(request, "gauss.html", {"data": datos,"tamaño": tamaño})
  return render(request, "gauss.html")

def pageFactorizacionLU(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    matrizA = request.POST["matrizA"]
    matrizB = request.POST["matrizB"]
    tamaño = request.POST["tamañoMatrizA"]
    tipoFactorizacion = request.POST["tipoFactorizacion"]
    try:
      datos = eng.LU(matrizA, matrizB, int(tamaño), int(tipoFactorizacion), nargout=3)
      print(datos)
    except:
      msg = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "factorizacionLU.html", {"msg": msg})
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

    if int(numIteraciones) <= 1:
      numIteraciones = 2
    try:
      datos = eng.SOR(matrizX0, matrizA, matrizB, float(tolerancia), int(numIteraciones), float(valorW), nargout=4)
      print(datos)
    except:
      msg = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "sor.html", {"msg": msg})
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
    if int(numIteraciones) <= 1:
      numIteraciones = 2
    try:
      datos = eng.MatJacobiSeid(matrizX0, matrizA, matrizB, float(tolerancia), int(numIteraciones), int(metodo), nargout=4)
      print(datos)
    except:
      msg = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "jacobiGauss.html", {"msg": msg})
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
    try:
      datos = eng.directLU(matrizA, matrizB, int(metodo), nargout=3)
      print(datos)
    except:
      msg = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "croDooCho.html", {"msg": msg})
  if datos:
    return render(request, "croDooCho.html", {"data": datos})
  return render(request, "croDooCho.html")

def pageVandermonde(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    valoresX = request.POST["valoresX"]
    valoresY = request.POST["valoresY"]
    try:
      datos = eng.vandermonde(valoresX, valoresY, nargout=2)
      print(datos)
    except:
      msg = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "vandermonde.html", {"msg": msg})
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
    try:
      datos = eng.Spline(valoresX, valoresY, int(tipoDeSpline))
      print(datos)
    except:
      msg = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "spline.html", {"msg": msg})
  if datos:
    return render(request, "spline.html", {"data": datos})
  return render(request, "spline.html")

def pageLagrange(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    valoresX = request.POST["valoresX"]
    valoresY = request.POST["valoresY"]

    try:
      datos = eng.Lagrange(valoresX, valoresY)
      print(datos)
    except:
      msg = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "lagrange.html", {"msg": msg})
  if datos:
    return render(request, "lagrange.html", {"data": datos})
  return render(request, "lagrange.html")

def pageNewtonint(request):
  datos = ()
  eng = matlab.engine.start_matlab()
  if request.method == 'POST':
    valoresX = request.POST["valoresX"]
    valoresY = request.POST["valoresY"]

    try:
      datos = eng.Newtonint(valoresX, valoresY, nargout=3)
      print(datos)
    except:
      msg = "El método falló inesperadamente, revise los valores de entrada"
      return render(request, "newtonint.html", {"msg": msg})
  if datos:
    tamaño = len(datos[0][0])
    return render(request, "newtonint.html", {"data": datos, "tamaño": tamaño})
  return render(request, "newtonint.html")

def pageGraficas(request):
  if request.method == 'POST':
    funcion = request.POST["funcion"]

    try:
      exp = sympify(funcion, convert_xor=True)
      grafica = plot(exp, show = False)
      grafica.save("calculadora/static/assets/img/GraficaSYM.jpg")
    except:
      msg = "Sucedio un error vuelva a intentar."
      return render(request, 'graficas.html', {"msg": msg})
  return render(request, 'graficas.html') 
