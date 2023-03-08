

###############  PART TWO  ################

#Investigate the convergence of your interpolation by using evenly spaced data and 
#varying the number of points N, or spacing h, to obtain a plot of error-vs-h, 
#where h = b  - aN - 1 is the usual knot spacing. The error should be defined by choosing
#the maximum error over a set of evaluation points on a subinterval of the 
#original data array x1, taking care that evaluation
#points will never be coincident with the data points as 
#N or h is varied. Note that you may need to tune the choice of evaluation points, or
#interval, to obtain a robust trend. Your plot should have a different curve for each
#degree of polynomial tested, and you should attempt to check the rate of convergence
#from the error data (i.e. the trend ).

import matplotlib.pyplot as plt
import numpy as np, numpy

f = lambda x: (numpy.e)**x * numpy.cos(10*x)

N = 61
D = 8

h = np.zeros([D, N])
error_max = np.zeros([D, N])

x = np.linspace(0.3,0.6,500)    # Take large number of points over a small subset to ensure that the max error will never be 0

for i in range(1, 1+D):    # Create loop to vary degree

    for j in range(N):    # Create loop to vary number of knots N
    
        x0 = np.linspace(-1, 1, j+60)    # Focus on small h
        
        y0 = f(x0)
    
        y = piecewiseLagrangePolynomialInterpolationFunction(x0, y0, x, i) 
        
        h[i-1][j] = x0[1] - x0[0]    # Calculate h as space between points. Evenly spaced so can just use two points from x0
        error_max[i-1][j] = np.max(np.abs(y - f(x)))    # Calculate error as maximum absolute value between actual function and interpolant
        

fig = plt.figure(figsize = (8, 5))    # Plot all degrees tested
for i in range(D):
    text = 'degree = {:}'.format(i+1)
    plt.loglog(h[i], error_max[i], label = text)

plt.xlabel('$h$')
plt.ylabel('$Error(h)$')    
plt.legend()
plt.show()


fig1 = plt.figure(figsize = (8 ,5))    # Plot a few degrees and test for trend
for i in range(1, D, 2):
    text = 'degree = {:}'.format(i+1)
    plt.loglog(h[i], error_max[i], label = text)

plt.loglog(h[-1], 100*h[-1]**3, linestyle = 'dashed', label = '$h^3$')
plt.loglog(h[-1], 1000*h[-1]**5, linestyle = 'dashed', label = '$h^5$')
plt.loglog(h[-1], 10000*h[-1]**7, linestyle = 'dashed', label = '$h^7$')
plt.loglog(h[-1], 100000*h[-1]**9, linestyle = 'dashed', label = '$h^9$')

plt.xlabel('$h$')
plt.ylabel('$Error(h)$')
plt.legend()
plt.show()