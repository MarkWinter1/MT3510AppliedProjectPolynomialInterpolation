

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