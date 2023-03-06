

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

import numpy as np, numpy
import matplotlib.pyplot as plt

f = lambda x: (numpy.e)**x * numpy.cos(10*x)    # Define function

def piecewiseLagrangePolynomialInterpolation( knots, degree = 3 ):

	#put the knots into a dual list form for simplicity reasons
    knotsX = numpy.array([ knot[0] for knot in knots ])
    knotsY = numpy.array([ knot[1] for knot in knots ])

    M = len(knotsX)
    h = knotsX[2]-knotsX[1]

	# We have M-deg interpolants to obtain
    Nint = M - degree
    pt1 = np.arange(degree+1)
    pts = pt1 + np.arange(Nint).reshape(Nint,1) # these are the sets of points we require

    a = np.zeros((degree+1,Nint))
    for i in range(Nint):
        A = np.vander(knotsX[pts[i,:]])
        a[:,i] = np.linalg.solve(A,knotsY[pts[i,:]])

    pows = (degree-np.arange(degree+1))
    y = np.empty_like(x)

    h = (knotsX[-1]-knotsX[0])/(M-1)                  # assumed spacing
	
	# making sure we don't overshoot the last subinterval
    k = np.minimum(M-2,((x-x[0])/h).astype(int)) 

    j = k - degree//2    

	# account for j<0 or j>Nint-1, i.e. at the edge
    j = np.maximum(0,j)
    j = np.minimum(j,Nint-1)

    y = np.sum(a[:,j[:]]*(x[:]**pows.reshape(degree+1,1)),axis=0)

    return y, h

N = 101
x = np.linspace(-1,1,500)

f = lambda x: (numpy.e)**x * numpy.cos(10*x)

h = np.zeros([5, N])
error_max = np.zeros([5, N])



for i in range(3, 8):    # Create loop to vary degree

    for j in range(N):    # Create loop to vary number of knots N
        
        testknots = [[x, f(x)] for x in np.linspace(-1,1,j+60)]    # Skip large h
    
        y = piecewiseLagrangePolynomialInterpolation(testknots, i)[0]
        
        h[i-3][j] = piecewiseLagrangePolynomialInterpolation(testknots, i)[1]   # Calculate h within interpolation function and return
        error_max[i-3][j] = np.max(np.abs(y - f(x)))

fig = plt.figure(figsize = (8, 5))    # Plot all degrees tested
for i in range(5):
    text = 'degree = {:}'.format(i+3)
    plt.loglog(h[i], error_max[i], label = text)

plt.xlabel('$h$')
plt.ylabel('$E(h)$')    
plt.legend()
plt.show()


fig1 = plt.figure(figsize = (8 ,5))    # Plot a few degrees and test for trend
for i in range(0, 5, 2):
    text = 'degree = {:}'.format(i+3)
    plt.loglog(h[i], error_max[i], label = text)

plt.loglog(h[-1], 1000*h[-1]**4, linestyle = 'dashed', label = '$h^4$')
plt.loglog(h[-1], 100000*h[-1]**6, linestyle = 'dashed', label = '$h^6$')
plt.loglog(h[-1], 100000*h[-1]**7, linestyle = 'dashed', label = '$h^7$')

plt.xlabel('$h$')
plt.ylabel('$E(h)$')
plt.legend()
plt.show()