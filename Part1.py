import matplotlib.pyplot as plt
import numpy


###############  PART ONE  ################

#The Test Function
f = lambda x: (numpy.e)**x * numpy.cos(10*x)

xValsTest = numpy.linspace(-(numpy.pi), (numpy.pi), 500)
yValsTest = f(xValsTest)

plot = plt.plot(xValsTest,yValsTest)
#plt.savefig("testoutputplot.png")  ##testplot, just graphing the given function 
plt.show()

#returns __a function__ that operates the polynomial. 
#degree is a positive int, knots is a list of coordinate pairs (x, y) 
def piecewiseLagrangePolynomialInterpolation( function, degree, knots ):
	return Null


# this has a wrapper that evaluates the function at the set of inputs
# to perform the specified function

# PWLPI( function, degree, knots )


	