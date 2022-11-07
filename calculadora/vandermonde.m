function [A, a] = vandermonde(x, y)
  x = str2num(x);
  y = str2num(y);
  x = x';
  y = y';

  A = [x.^3 x.^2 x ones(4,1)];
  b = y;
  a = inv(A)*b;

  xpol = -2:0.01:3;
  p = a(1)*xpol.^3+a(2)*xpol.^2+a(3)*xpol+a(4);