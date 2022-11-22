import math
from sympy import *
import numpy as np
import sympy as sym
from sympy.abc import x as xmul

def busquedasIncrementales(numeroInicial, delta, numIteracciones, funcion):
  x,y = symbols("x y")
  X0 = float(numeroInicial)
  Delta = float(delta)
  Niter = int(numIteracciones)
  Fun = sympify(funcion, convert_xor=True)

  X = X0
  f0 = Fun.evalf(subs={x:X0})

  if f0 == 0:
    s = X
    return f"{X0} es raíz de f(x)"
  else:
    X1 = X0+Delta
    X = X1
    c = 1
    f1 = Fun.evalf(subs={x:X1})

    while f0*f1 > 0 and c < Niter:
      X0 = X1
      f0 = f1
      X1 = X0+Delta
      X = X1                 
      f1 = Fun.evalf(subs={x:X1})
      c = c+1
      if f1 == 0:
          s = X
          return f"{X1} es raíz de f(x)"
      elif f0*f1<0:
          s=X
          return f"Existe una raíz entre [{X0},{X1}]"
      else:
          s=x
          return f"Fracasó en {Niter} iteraciones "
  return f"Fracasó en {Niter} iteraciones "

def Biseccion(Xi, Xs, Tol, Niter, Fun):
    x,y = symbols("x y")
    Xi = float(Xi)
    Xs = float(Xs)
    Tol = float(Tol)
    Niter = int(Niter)
    exp = sympify(Fun, convert_xor=True)

    fm = []
    E = []
    N = []
    fi = exp.evalf(subs={x:Xi})
    fs = exp.evalf(subs={x:Xs})
    print(fi)
    print(fs)
    c = 0
    N.append(c)

    if fi == 0:
      s = Xi
      E = 0
      return f"{Xi} es raíz de f(x)"

    elif fs == 0:
      s = Xs
      E = 0
      return f"{Xs} es raíz de f(x)"

    elif fs*fi < 0:
      
      Xm = (Xi+Xs)/2
      fe = exp.evalf(subs={x:Xm})
      fm.append(fe)
      E.append(100)

      while E[c] > Tol and fe != 0 and c < Niter:
        if fi*fe < 0:
          Xs = Xm
          fs = exp.evalf(subs={x:Xs})
        else:
          Xi = Xm
          fs = exp.evalf(subs={x:Xi})
        Xa = Xm
        Xm = (Xi+Xs)/2
        fe = exp.evalf(subs={x:Xm})
        fm.append(fe)
        Error = abs(Xm-Xa)
        E.append(Error)
        c = c+1
        N.append(c)
      if fe == 0:
        s = x
        return f"{s} es raíz de f(x)"
      elif Error < Tol:
        s = x
        msg = f"{s} es una aproximación de un raíz de f(x) con una tolerancia de {Tol}"
        return N, fm, E, msg
      else:
        s = x
        return f"Fracasó en {Niter} iteraciones"
    else:
      return f"El intervalo es inadecuado"

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
      return f"{s} es raiz de f(x)"
  elif Error < Tol:
      s = X
      msg = f"{s} es una aproximación de una raíz de f(x) con una tolerancia de {Tol}"
      if tipoDeError == 'Error absoluto':
        return N, xn, fn, E, msg
      else:
        return N, xn, fn, ERelativo, msg
  else:
      s = X
      return f"Fracasó en {Niter} iteraciones"

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
  if derivada == 0:
    return f"Alerta: La derivada de la función es igual a cero!"
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
      return f"{s} es raíz de f(x)"

  elif Error < Tol:
      s = X
      msg = f"{s} es una aproximación de un raíz de f(x) con una tolerancia de {Tol}"
      #print(tipoDeError)
      if tipoDeError == 'Error absoluto':
        return N, xn ,fn, E, msg
      else: 
        return N, xn ,fn, ERelativo, msg
  else:
      s = X
      return f"Fracasó en {Niter} iteraciones"

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
    return f"{X0} es raíz de f(x)"

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
      return f"{s} es raíz de f(x)"
    elif Error < Tol:
      s = x
      msg= f"{s} es una aproximación de un raíz de f(x) con una tolerancia de {Tol}"
      if tipoDeError == 'Error absoluto':
        return N,val2, fm, E, msg
      else:
        return N, val2, fm, ERelativo, msg
    else:
      s = x
      return f"Fracasó en {Niter} iteraciones" 
  else:
    return "El intervalo es inadecuado"

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
      return f"{X0} es raiz de f(x)"

  fm = 1
  while (Error > Tol) and (c < Niter) and (fm != 0):    
      f = exp.evalf(subs={x:X0})
      f1 = exp.evalf(subs={x:X1})

      Xn = X1 - ((f1*(X1-X0))/(f1-f))
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
      return f"{s} es raiz de f(x)"

  elif Error < Tol:
      s = X0
      msg = f"{s} es una aproximación de una raíz de f(x) con una tolerancia de {Tol}"
      if tipoDeError == 'Error absoluto':
        return N, xn ,fn, E, msg
      else:
        return N, xn ,fn, ERelativo, msg
  else:
      s = 1
      return f"Fracasó en {Niter} iteraciones"

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
      return f"{s} es raíz de f(x)"
  elif Error < Tol:
      s = X
      msg = f"{s} es una aproximación de una raiz de f(x) con una tolerancia {Tol}"
      if tipoDeError == 'Error absoluto':
        return N, xn ,fn, E, msg
      else:
        return N, xn ,fn, ERelativo, msg
  else:
      s = X
      return f"Fracasó en {Niter} iteraciones"