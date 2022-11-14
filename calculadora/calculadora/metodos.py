import math
from sympy import *
import numpy as np
import sympy as sym
from sympy.abc import x as xmul


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

def PuntoFijo(X0, Tol, Niter, Fun, GFun, tipoDeError): 
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
  ERelativo = []
  X = X0
  #x = X0
  #f = eval(Fun)
  f = exp.subs(x,X)
  c = 0
  Error = 100  
  ErrorRelativo = 100                
  fn.append(f)
  xn.append(X)
  E.append(Error)
  ERelativo.append(ErrorRelativo)
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
    ErrorRelativo = abs((xn[c] - xn[c-1])/xn[c])
    ERelativo.append(ErrorRelativo)

  if fe == 0:
      s = X
      print(s,"es raiz de f(x)")
  elif Error < Tol:
      s = X
      print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
      if tipoDeError == 'Error absoluto':
        return N, xn, fn, E
      else:
        return N, xn, fn, ERelativo 
  else:
      s = X
      print("Fracaso en ",Niter, " iteraciones ") 

def Newton(X0, Tol, Niter, Fun, tipoDeError):
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
  ERelativo = []
  X = X0
  #x = X0
  #f = eval(Fun)
  f = exp.subs(x,X0)
  derivada = DFun.subs(x, X0)
  c = 0
  Error = 100      
  ErrorRelativo = 100            
  fn.append(f)
  xn.append(X0)
  E.append(Error)
  ERelativo.append(ErrorRelativo)
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
      ErrorRelativo = abs((xn[c]-xn[c-1])/xn[c])
      ERelativo.append(ErrorRelativo)
  if f == 0:
      s = X
      print(s,"es raiz de f(x)")

  elif Error < Tol:
      s = X
      print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
      print(tipoDeError)
      if tipoDeError == 'Error absoluto':
        return N, xn ,fn, E
      else: 
        return N, xn ,fn, ERelativo
  else:
      s = X
      print("Fracaso en ",Niter, " iteraciones ")

def ReglaFalsa(X0, X1, Tol, Niter, Fun, tipoDeError):
  x,y = symbols("x y")
  X0 = int(X0)
  X1 = int(X1)
  Tol = float(Tol)
  Niter = int(Niter)
  exp = sympify(Fun, convert_xor=True)

  fm = []
  val2 = []
  E = []
  ERelativo = []
  N = []

  fi = exp.evalf(subs={x:X0})
  fs = exp.evalf(subs={x:X1})

  c = 0
  N.append(c)

  if fi*fs == 0:
    s = X0
    E = 0
    ERelativo = 0
    print(X0, "es raiz de f(x)")

  elif fi*fs <= 0:
    Xm = X1 - (fs*(X0-X1))/(fi-fs)
    val2.append(Xm)
    fe = exp.evalf(subs={x:Xm})
    fm.append(fe)

    E.append(100)
    ERelativo.append(100)
    
    while E[c] > Tol and fe != 0 and c < Niter and fi*fs < 0:
      if fi*fe < 0:
        X1 = Xm
        fs = exp.evalf(subs={x:X1})
      else:
        X0 = Xm
        fi = exp.evalf(subs={x:X0})
      Xa = Xm
      Xm = X1 - (fs*(X0-X1))/(fi-fs)
      val2.append(Xm)
      fe = exp.evalf(subs={x:Xm})
      fm.append(fe)

      Error = abs(Xm-Xa)
      E.append(Error)
      ErrorRelativo = abs((Xm-Xa)/Xm)
      ERelativo.append(ErrorRelativo)

      c = c+1
      N.append(c)

    if fe == 0:
      s = x
      print(s,"es raiz de f(x)")
    elif Error < Tol:
      s = x
      print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
      if tipoDeError == 'Error absoluto':
        return N,val2, fm, E
      else:
        return N, val2, fm, ERelativo
    else:
      s = x
      print("Fracaso en ",Niter, " iteraciones ") 
  else:
    print("El intervalo es inadecuado")

def Secante(X0, X1,Tol,Niter ,Fun, tipoDeError):
  x,y = symbols("x y")
  exp = sympify(Fun, convert_xor=True)
  X0 = float(X0)
  X1 = float(X1)
  Tol = float(Tol)
  Niter = int(Niter)
  exp = sympify(Fun, convert_xor=True)

  fn = []
  xn = []
  E = []
  ERelativo = []
  N = []

  f = exp.evalf(subs={x:X0})
  fn.append(f)
  xn.append(X0)

  c = 0
  Error = 100
  ErrorRelativo = 100       
  E.append(Error)
  ERelativo.append(ErrorRelativo)
  N.append(c)

  f1 = exp.evalf(subs={x:X1})
  fn.append(f1)
  xn.append(X1)

  c = c + 1
  Error = 100
  ErrorRelativo = 100   
  E.append(Error)
  ERelativo.append(ErrorRelativo)
  N.append(c)

  if f1 == 0 or f == 0:
      s = X0
      E = 0
      ERelativo = 0
      print(X0, "es raiz de f(x)")

  fm = 1
  while (Error > Tol) and (c < Niter) and (fm != 0):    
      f = exp.evalf(subs={x:X0})
      f1 = exp.evalf(subs={x:X1})

      Xn = X1 - ((f1*(X1-X0))/(f1-f))
      #x = Xn
      fm = exp.evalf(subs={x:Xn})

      fn.append(fm)
      xn.append(Xn)
      c = c+1

      Error = abs(xn[c]-xn[c-1])
      ErrorRelativo = abs((xn[c]-xn[c-1])/xn[c])
      N.append(c)
      E.append(Error)
      ERelativo.append(ErrorRelativo)

      X0 = X1
      X1 = Xn

  if f == 0:
      s = X0
      print(s,"es raiz de f(x)")

  elif Error < Tol:
      s = X0
      print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
      if tipoDeError == 'Error absoluto':
        return N, xn ,fn, E
      else:
        return N, xn ,fn, ERelativo
  else:
      s = 1
      print("Fracaso en ",Niter, " iteraciones ") 

def sustreg(Ab,n):
	x = np.zeros(n)
	x[n-1]=Ab[n-1][n]/Ab[n-1][n-1]
	for i in range(n-2,-1,-1):
		sum=0
		for p in range(i+1,n):
			sum=sum+Ab[i][p]*x[p]
		x[i]=(Ab[i][n]-sum)/Ab[i][i]
	return x

def Gauss(A, b, Piv):
  print(A)
  print(b)
  A = np.array(A, dtype='float64')
  n = len(A)
  b = np.array((b), dtype='float64')
  #Piv = 0
  Ab = np.zeros((3,4))
  Ab = np.concatenate((A, b), axis = 1)
  mark = list(range(n))

  for k in range(0,n-1):
    if Piv == 1:
      print("pivoteo parcial")
    elif Piv > 1:
      print("pivoteo total")
    for i in range(k+1,n):
        M = Ab[i][k]/Ab[k][k]
        for j in range(k,n+1):
                Ab[i][j] = Ab[i][j]-M*Ab[k][j]
  x = sustreg(Ab,n)
  print(x)
  print("mark =", mark)
  print("Ab =", Ab)
  return x, Ab

def RaicesMultiples(X0, Tol, Niter, Fun, DFun, DFun2, tipoDeError):
  x = xmul
  
  X0 = float(X0)
  Tol = float(Tol)
  Niter = int(Niter)

  Fun = sympify(Fun, convert_xor=True)
  DFun = sympify(DFun, convert_xor=True) 
  DFun2 = sympify(DFun2, convert_xor=True)

  fn = []
  xn = []
  E = []
  N = []
  ERelativo = []

  f = Fun.evalf(subs={x:X0})
  derivada = DFun.evalf(subs={x:X0})
  derivada2 = DFun2.evalf(subs={x:X0})

  c = 0
  Error = 100    
  ErrorRelativo = 100           
  fn.append(f)

  xn.append(X0)
  E.append(Error)
  ERelativo.append(ErrorRelativo)
  N.append(c)

  X = X0 - ((f*derivada)/((derivada)**2 - f * derivada2))
  f = Fun.evalf(subs={x:X})
  derivada = DFun.evalf(subs={x:X})
  derivada2 = DFun2.evalf(subs={x:X})

  print(f'Funcion evaluada 2: {f}')

  fn.append(f)
  xn.append(X)
  c = c+1
  Error = abs(xn[c]-xn[c-1])
  ErrorRelativo = abs((xn[c]-xn[c-1])/xn[c])
  E.append(Error)
  ERelativo.append(ErrorRelativo)
  N.append(c)

  while Error>Tol and f!=0 and c<Niter:
      X0 = X
      f = Fun.evalf(subs={x:X0})
      derivada = DFun.evalf(subs={x:X0})
      derivada2 = DFun2.evalf(subs={x:X0})

      X = X0 - ((f*derivada)/(derivada**2 - f * derivada2))
      fn.append(f)
      xn.append(X)

      c = c+1
      Error = abs(xn[c]-xn[c-1])
      ErrorRelativo = abs((xn[c]-xn[c-1])/xn[c])
      N.append(c)
      E.append(Error)
      ERelativo.append(ErrorRelativo)
  if f == 0:
      s = X
      print(s,"es raiz de f(x)")
  elif Error < Tol:
      s = X
      print(s,"es una aproximacion de un raiz de f(x) con una tolerancia", Tol)
      if tipoDeError == 'Error absoluto':
        return N, xn ,fn, E
      else:
        return N, xn ,fn, ERelativo
  else:
      s = X
      print("Fracaso en ",Niter, " iteraciones ")