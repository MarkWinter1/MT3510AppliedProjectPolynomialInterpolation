

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

def piecewiseLagrangePolynomialInterpolation( function, degree, knots ):
	Ndeg = 3

	N = 101
	x = np.linspace(-1,1,N)

	M = 11
	x0 = np.linspace(-1,1,M)
	y0 = f(x0)

	# Now do out piecewise polynomial
	#----------------------------------------------------------------

	h = x0[2]-x0[1]

	# We have M-deg interpolants to obtain

	Nint = M - Ndeg
	pt1 = np.arange(Ndeg+1)
	pts = pt1 + np.arange(Nint).reshape(Nint,1) # these are the sets of points we require

	a = np.zeros((Ndeg+1,Nint))
	for i in range(Nint):
		A = np.vander(x0[pts[i,:]])
		a[:,i] = np.linalg.solve(A,y0[pts[i,:]])

	pows = (Ndeg-np.arange(Ndeg+1))
	y = np.empty_like(x)

	h = (x0[-1]-x0[0])/(M-1)                  # assumed spacing

	k = np.minimum(M-2,((x-x[0])/h).astype(int)) # making sure we don't overshoot the last subinterval
   
	j = k - Ndeg//2    

	# account for j<0 or j>Nint-1, i.e. at the edge
	j = np.maximum(0,j)
	j = np.minimum(j,Nint-1)

	y = np.sum(a[:,j[:]]*(x[:]**pows.reshape(Ndeg+1,1)),axis=0)

# 	plt.plot(x,(numpy.e)**x * numpy.cos(10*x),label='exact function')
# 	plt.plot(x0,y0,'kx',mew=2,label='data')
# 	plt.plot(x,y,'.',label='poly interpolated')
# 	plt.xlabel('x')
# 	plt.ylabel('y')
# 	plt.legend()
# 	plt.tight_layout()
# 	plt.show()

# 	plt.figure(figsize=(8,5))
# 	plt.plot(x,np.abs(np.sin(x)-y))
# 	plt.xlabel('$x$')
# 	plt.ylabel('$|y-p|$')
# 	plt.title('Error')
# 	plt.tight_layout()
# 	plt.show()

	return y





NN = 100    # Choose how many resolutions to test
a = 0
b = 1/6
M = 11

err_h = np.zeros(NN)    # store error  
h = np.zeros(NN)    #store h

x = np.linspace(a, b, 500)
for i in range(NN):
    x0 = np.linspace(a, b, i+20)
    y0 = (np.e)**x0 * np.cos(10*x0)
    
    f = piecewiseLagrangePolynomialInterpolation(0,0,0)
    
    #y = f(x)
    
    err_h[i] = np.max(np.abs(f - y0))
    h[i] = x0[1] - x0[0]
    
# h is spacing, b is last point and a is first point