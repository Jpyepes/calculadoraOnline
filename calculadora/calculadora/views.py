from django.shortcuts import render
from calculadora.metodos import Biseccion, PuntoFijo, Newton

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
    return render(request,"reglaFalsa.html")

def pageMetodoSecante(request):
    return render(request,"secante.html")
