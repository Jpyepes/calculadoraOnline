import math
from sympy import *
import numpy as np

def Biseccion(Xi, Xs, Tol, Niter, Fun):
    x,y = symbols("x y")
    Xi = int(Xi)
    Xs = int(Xs)
    Tol = float(Tol)
    Niter = int(Niter)
    exp = sympify(Fun, convert_xor=True)

    fm = []
    E = []
    N = []
    #x = Xi
    #fi = eval(Fun)
    fi = exp.subs(x,Xi)
    #x = Xs
    #fs = eval(Fun)
    fs = exp.subs(x, Xs)
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
      fe = exp.subs(x,Xm)
      fm.append(fe)
      E.append(100)

      while E[c] > Tol and fe != 0 and c < Niter:
        if fi*fe < 0:
          Xs = Xm
          fs = exp.subs(x,Xs)
        else:
          Xi = Xm
          fs = exp.subs(x,Xi)
        Xa = Xm
        Xm = (Xi+Xs)/2
        fe = exp.subs(x,Xm)
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

def PuntoFijo(X0, Tol, Niter, Fun, GFun): 
  x,y = symbols("x y") 
  X0 = float(X0)
  Tol = float(Tol)
  Niter = int(Niter)
  exp = sympify(Fun, convert_xor=True)
  Gexp = sympify(GFun, convert_xor=True)

  fn = []
  xn = []
  E = []
  N = []
  X = X0
  #x = X0
  #f = eval(Fun)
  f = exp.subs(x,X)
  c = 0
  Error = 100               
  fn.append(f)
  xn.append(X)
  E.append(Error)
  N.append(c)

  while Error > Tol and f != 0 and c < Niter:
    #x = eval(GFun)
    #fe = eval(Fun)
    X = Gexp.subs(x,X)
    fe = exp.subs(x,X)
    fn.append(fe)
    xn.append(X)

    c = c+1
    Error = abs(xn[c]-xn[c-1])
    N.append(c)
    E.append(Error)	

  if fe == 0:
      s = X
      print(s,"es raiz de f(x)")
  elif Error < Tol:
      s = X
      print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
      return N, xn, fn, E
  else:
      s = X
      print("Fracaso en ",Niter, " iteraciones ") 

def Newton(X0, Tol, Niter, Fun):
  x,y = symbols("x y")
  exp = sympify(Fun, convert_xor=True)
  DFun = diff(exp, x) # poner la derivada
  print(DFun)
  X0 = float(X0)
  Tol = float(Tol)
  Niter = int(Niter)

  fn = []
  xn = []
  E = []
  N = []
  X = X0
  #x = X0
  #f = eval(Fun)
  f = exp.subs(x,X0)
  derivada = DFun.subs(x, X0)
  c = 0
  Error = 100               
  fn.append(f)
  xn.append(X0)
  E.append(Error)
  N.append(c)

  while Error>Tol and f!=0 and derivada!=0  and c<Niter:
      X = X-f/derivada
      derivada = DFun.subs(x, X)
      #f = eval(Fun)
      f = exp.subs(x,X)
      fn.append(f)
      xn.append(X)
      c = c+1
      Error = abs(xn[c]-xn[c-1])
      N.append(c)
      E.append(Error)
  if f == 0:
      s = X
      print(s,"es raiz de f(x)")

  elif Error < Tol:
      s = X
      print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
      return N, xn ,fn, E
  else:
      s = X
      print("Fracaso en ",Niter, " iteraciones ")