

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

def piecewiseLagrangePolynomialInterpolationFunction(x0, y0, xEval, degree = 3):
    Ndeg = degree
    M = len(x0)
    N = len(xEval)

    # We have M-deg interpolants to obtain
    Nint = M - Ndeg
    pt1 = np.arange(Ndeg+1)
    pts = pt1 + np.arange(Nint).reshape(Nint,1) # these are the sets of points we require

    #structure a
    a = np.zeros((Ndeg+1,Nint))
    for i in range(Nint):
        A = np.vander(x0[pts[i,:]])
        a[:,i] = np.linalg.solve(A,y0[pts[i,:]])

    y = np.empty_like(xEval)     # set up new data points
    pows = Ndeg-np.arange(Ndeg+1)

    for i in range(N):       # loop over new evaluation points

        if((xEval[i]<x0).all()): # if we're outside of the interval, set k to extrapolate
            k = 0
        elif((xEval[i]>x0).all()):
            k = M-1
        else:                # find k for x_i, accounting for the possibility that x_i=x_k
            k = np.where(((xEval[i]<x0[1:]) & (xEval[i]>=x0[:-1])) | 
                         ((x0[1:]==xEval[i]) & (xEval[i]>x0[:-1])))[0][0]

        # k is the left hand data point of our current subinterval; 
        # we need the polynomial with this point as the *centre*
    
        j = k - Ndeg//2    

        # account for j<0 or j>Nint-1, i.e. at the edge
        j = np.maximum(0,j)
        j = np.minimum(j,Nint-1)

        y[i] = np.sum(a[:,j]*xEval[i]**pows)
    
    return y

f = lambda x: (numpy.e)**x * numpy.cos(10*x)

N = 61
D = 8

h = np.zeros([D, N])
error_max = np.zeros([D, N])

x = np.linspace(0.3,0.6,500)    # Take large number of points over a small subset to ensure that the max error will never be 0

for i in range(1, 1+D):    # Create loop to vary degree

    for j in range(N):    # Create loop to vary number of knots N
    
        x0 = np.linspace(-1, 1, j+60)    # Skip large h
        
        y0 = f(x0)
    
        y = piecewiseLagrangePolynomialInterpolationFunction(x0, y0, x, i) 
        
        h[i-1][j] = x0[1] - x0[0]    # Calculate h within interpolation function and return
        error_max[i-1][j] = np.max(np.abs(y - f(x)))
        

fig = plt.figure(figsize = (8, 5))    # Plot all degrees tested
for i in range(D):
    text = 'degree = {:}'.format(i+1)
    plt.loglog(h[i], error_max[i], label = text)

plt.xlabel('$h$')
plt.ylabel('$E(h)$')    
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
plt.ylabel('$E(h)$')
plt.legend()
plt.show()