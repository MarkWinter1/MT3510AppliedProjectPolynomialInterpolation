

###############  PART THREE  ################

#  Create an interactive plot which allows the user to vary the degree of a Lagrange
# interpolating polynomial (not piecewise) for a certain set of knots and evaluation points.
# The plot should show the interpolating function and the knots (like this). For
# demonstration purposes use the function from part 1, i.e. but now
# plot the interval choose a modest number of knots and centre your
# interpolant (i.e. as the degree increases and more knots are required work from the
# centre out, as seen in the video)

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact,interactive,fixed #imported all i need to get this scale changing thing 

#1 - set up our function and our x0 and y0 

def f(x):
    return np.exp(x)*np.cos(10*x)

N=100
x = np.linspace(1,2,N)

#2 - make a function performing a lagrange polynomial of degree M based on the input of M.

def lagrange_polynomial_degree(a,b,M):
    x0 = np.linspace(a,b,M)
    y0 = f(x0)
    A = np.vander(x0)         
    a = np.linalg.solve(A,y0)
    pows = (M-1-np.arange(M)).reshape(M,1)         # these are the exponents required
    xnew = np.reshape(x,(1,N))                     # reshape for the broadcast
    ynew = np.sum((xnew**pows)*a.reshape(M,1),axis=0)
    return ynew

#3 - set up a plot which updates as it slides 

def polynomial_plot(a=1,b=2,degree=(1,10)):
    plt.figure(figsize=(8,5))
    plt.plot(x,f(x),label='exact function')
    plt.plot(x0,y0,'kx',mew=2,label='data')
    plt.plot(x,lagrange_polynomial_degree(a,b,degree),'.',label=f'poly interpolated data of degree {M}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    
interactive(polynomial_plot,M=1, a=fixed(1),b=fixed(2))
