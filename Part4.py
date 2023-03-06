### PART 1 ###
import matplotlib.pyplot as plt
import numpy as np, numpy
from scipy.interpolate import CubicSpline


def piecewiseLagrangePolynomialInterpolation( knots, degree = 3 ):

	#put the knots into a dual list form for simplicity reasons
	knotsX = np.array([ knot[0] for knot in knots ])
	knotsY = np.array([ knot[1] for knot in knots ])

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

	return y


###############  PART FOUR  ################

#  Load the data file wave_data1.txt (on JupyterHub) using np.loadtxt
#The data file has a row each for data where is time in seconds and is the surface
#elevation of a water column (in metres) at a particular location in a laboratory wave tank (like
#this). Unfortunately there are a few data points missing due to a mishap with the wave
#probe.

#  How many data points appear to be missing?


#  Use your interpolation function from part 1 to obtain a new uniformly sampled data set
#on 0.01s subintervals for the first 20s using piecewise cubic polynomials. Plot the new
#data alongside the equivalent data obtained using
#scipy.interpolate.CubicSpline .


#  Plot the difference between the piecewise cubic interpolation and the cubic spline
#interpolation obtained using scipy.interpolate.CubicSpline



### CHANGE FILE PATHWAY ###
data = np.loadtxt("/Users/benbroughton/Downloads/wave_data1.txt")
data2 = np.loadtxt("/Users/benbroughton/Downloads/wave_data1.txt")
yfull = data[1]
xfull = data[0]
store = []
for i in range(1,len(xfull)):
    diff = xfull[i]-xfull[i-1]
    if diff > 0.11:
        data = [i-1, xfull[i-1], xfull[i], diff]
        store.append(data)
        
missing_store = []
ymiss = []
# loop to find missing x values by identifying those with a difference larger than 0.1 (accounting for machine precision)
# then return them with an array so they may be plotted for visualisation
for i in range(len(store)):
    x_temp = np.arange(store[i][1]+0.1,round(store[i][2],1)-0.001, 0.1)
    coord_pai = []
    for j in range(len(x_temp)):
        coord_pair = [x_temp[j],0]
        missing_store.append(coord_pair)
missing_points = np.transpose(missing_store)
q4a = len(missing_store)
### As seen in q4a we see we have 8 missing points


fig, ax = plt.subplots(figsize=(15, 6))
ax.plot(xfull,yfull)

ax.scatter(missing_points[0], missing_points[1], marker="*", color="r", s=50, zorder=2)
print(q4a)


### q4b - the parts I can currently do ###
x_new = np.linspace(0,20,201)
#interpolated_data = piecewiseLagrangePolynomialInterpolation(np.transpose(data2), degree = 3 )
cubic_spline = CubicSpline(data2[0], data2[1],bc_type='natural')
ax.plot(x_new,cubic_spline(x_new))

