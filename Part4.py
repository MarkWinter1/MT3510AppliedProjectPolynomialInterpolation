

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