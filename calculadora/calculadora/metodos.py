from requests import request
import math

def Biseccion(Xi, Xs, Tol, Niter, Fun):
    Xi = int(Xi)
    Xs = int(Xs)
    Tol = float(Tol)
    Niter = int(Niter)

    fm = []
    E = []
    N = []
    x = Xi
    fi = eval(Fun)
    x = Xs
    fs = eval(Fun)
    c = 0
    N.append(c)

    if fi == 0:
      s = Xi
      E = 0
      print(Xi, "es raiz de f(x)")

    elif fs == 0:
      s = Xs
      E = 0
      print(Xs, "es raiz de f(x)")

    elif fs*fi < 0:
      
      Xm = (Xi+Xs)/2
      x = Xm                 
      fe = eval(Fun)
      fm.append(fe)
      E.append(100)

      while E[c] > Tol and fe != 0 and c < Niter:
        if fi*fe < 0:
          Xs = Xm
          x = Xs                 
          fs = eval(Fun)
        else:
          Xi = Xm
          x = Xi
          fs = eval(Fun)
        Xa = Xm
        Xm = (Xi+Xs)/2
        x = Xm 
        fe = eval(Fun)
        fm.append(fe)
        Error = abs(Xm-Xa)
        E.append(Error)
        c = c+1
        N.append(c)
      if fe == 0:
        s = x
        print(s,"es raiz de f(x)")
      elif Error < Tol:
        s = x
        print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
        return N, fm, E
      else:
        s = x
        print("Fracaso en ",Niter, " iteraciones ") 
    else:
      #alerta = "El intervalo es inadecuado"
      #return alerta
      print("El intervalo es inadecuado")

def Newton():
  pass