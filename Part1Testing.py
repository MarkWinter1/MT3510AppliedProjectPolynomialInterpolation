import matplotlib.pyplot as plt
import numpy as np, numpy

import Part1

f = lambda x: (numpy.e)**x * numpy.cos(10*x)

N = 101
x = np.linspace(-2,5,N)

M = 11
x0 = np.linspace(-1,1,M)
y0 = f(x0)

y = Part1.piecewiseLagrangePolynomialInterpolationFunction(x0, y0, x)

#y = piecewiseLagrangePolynomialInterpolationFunction(testknots, 3)

plt.figure(figsize=(8,5))
plt.plot(x,f(x),label='exact function')
plt.plot(x0,y0,'kx',mew=2,label='data')
plt.plot(x,y,'.',label='polynomial interpolated')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
plt.plot(x,np.abs(f(x)-y),label='polynomial interpolated')
plt.xlabel('$x$')
plt.ylabel('$|y-p|$')
plt.title('Error')
plt.legend()
plt.tight_layout()
plt.show()
