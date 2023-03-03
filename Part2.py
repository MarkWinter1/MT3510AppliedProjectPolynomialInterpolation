

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

f = lambda x: (numpy.e)**x * numpy.cos(10*x)

def piecewiseLagrangePolynomialInterpolation( knots, degree = 3 ):

	#put the knots into a dual list form for simplicity reasons
    knotsX = numpy.array([ knot[0] for knot in knots ])
    knotsY = numpy.array([ knot[1] for knot in knots ])

    M = len(knotsX)
    h = knotsX[2]-knotsX[1]
#    print('This is knot length',M)
#    print('This is degree', degree)
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

N = 100
x = np.linspace(-1,1,N)

f = lambda x: (numpy.e)**x * numpy.cos(10*x)

h = np.zeros([10, 25])
error_max = np.zeros([10, 25])

error = np.array([])

for i in range(3, 13):

    for j in range(13, 28):
        
        testknots = [[x, f(x)] for x in np.linspace(-1,1,j)]
    
        y = piecewiseLagrangePolynomialInterpolation(testknots, i)[0]
        
        h[i-3][j-13] = piecewiseLagrangePolynomialInterpolation(testknots, i)[1]
        error_max[i-3][j-13] = np.max(np.abs(y - f(x)))

    # plt.figure(figsize=(8,5))
    # plt.plot(x,np.abs(f(x)-y))
    # plt.xlabel('$x$')
    # plt.ylabel('$|y-p|$')
    # plt.title('Error')
    # plt.tight_layout()
    # plt.show()
    
    # print(np.abs(f(x)-y))

fig = plt.figure(figsize = (8 ,5))
for i in range(0, 10, 4):
    text = 'degree = {:}'.format(i+3)
    plt.loglog(h[i], error_max[i], label = text)
plt.loglog(h[-1], 100*h[-1]**3, linestyle = 'dashed', label = '$h^3$')
plt.loglog(h[-1], 100000*h[-1]**7, linestyle = 'dashed', label = '$h^7$')
plt.loglog(h[-1], 1000000000*h[-1]**11, linestyle = 'dashed', label = '$h^{11}$')

plt.xlim(0.08, 0.16)
plt.legend()
plt.show()
    
# plt.figure(figsize=(8,5))
# plt.plot(x,np.abs(f(x)-y))
# plt.xlabel('$x$')
# plt.ylabel('$|y-p|$')
# plt.title('Error')
# plt.tight_layout()
# plt.show()