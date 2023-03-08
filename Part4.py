import matplotlib.pyplot as plt
import numpy as np, numpy
from scipy.interpolate import CubicSpline

def piecewiseLagrangePolynomialInterpolationFunction(x0, y0, xEval, degree = 3):
    Ndeg = degree
    M = len(x0)
    N = len(xEval)
    # First perform the non piecewise interpolation for comparison
    #----------------------------------------------------------------
    A = np.vander(x0)          # construct the Vandermode matrix
    a = np.linalg.solve(A,y0)  # obtain the coefficients by solving the system
    pows = (M-1-np.arange(M)).reshape(M,1)         # these are the exponents required
    xnew = np.reshape(xEval,(1,N))                     # reshape for the broadcast
    ynew = np.sum((xnew**pows)*a.reshape(M,1),axis=0) # multiply by coefficients and sum along the right direction

    # Now do out piecewise polynomial
    #----------------------------------------------------------------

    Ndeg = 3
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

data = np.loadtxt("./wave_data1.txt")
data2 = np.loadtxt("./wave_data1.txt")

yfull = data[1]
xfull = data[0]
store = []


# Loop to find missing x value areas by identifying those with a difference 
# larger than 0.11 (accounting for machine precision)
for i in range(1,len(xfull)):
    diff = xfull[i]-xfull[i-1]
    if diff > 0.11:                                        
        data = [i-1, xfull[i-1], xfull[i], diff]               # Information required to recover missing x values
        store.append(data)
        
missing_store = []
ymiss = []


# Recover all missing x values and print the number of missing points
for i in range(len(store)):
    x_temp = np.arange(store[i][1]+0.1,round(store[i][2],1)-0.001, 0.1)
    for j in range(len(x_temp)):
        missing_store.append(x_temp[j])
q4a = len(missing_store)

print(f'Question 4(a) answer: We have {q4a} missing points.')




# Plot the first 20 seconds of Wave Data
fig, ax = plt.subplots(figsize=(15, 7))
ax.plot(xfull[:201-9],yfull[:201-9], label = 'Wave Data')


# Generate uniformly sampled data on 0.01 sub intervals
x_new = np.linspace(0,20,201)
    
# Perform Piecewise Lagrange Polynomial Interpolation on sampled data
y_new = piecewiseLagrangePolynomialInterpolationFunction(xfull, yfull, xEval = x_new, degree = 3)

# Perform Cubic Spline Interpolation on sampled data
cubic_spline = CubicSpline(data2[0], data2[1],bc_type='natural')


# Plot the results of interpolation methods
ax.plot(x_new,cubic_spline(x_new),'.', label = 'Cubic Spline Interpolated')
ax.plot(x_new, y_new, '.', label = 'Piecwise Polynomial Interpolated')

plt.title('Wave Data with Interpolated Data Using Cubic Spline and Piecewise Polynomial Methods')
plt.legend()
plt.xlabel('Time in Seconds')
plt.ylabel('Elevation of Water in Meters')


# Plot the difference between interpolation methods
fig, ax2 = plt.subplots(figsize=(15, 7))

err = abs(cubic_spline(x_new)-y_new)
ax2.plot(x_new, err)

plt.title('Absolute Difference Between Piecewise Polynomial and Cubic Spline Interpolation on Wave Data')
plt.xlabel('Time in Seconds')
plt.ylabel('| Cubic Spline - Piecewise Polynomial |')

