import matplotlib.pyplot as plt
import numpy

#This file is mostly just for testing junk
#May later be made into a something to call the other files sequentially

f = lambda x: (numpy.e)**x * numpy.cos(10*x)

xVals = numpy.linspace(-(numpy.pi), (numpy.pi), 500)
yVals = f(xVals)

plot = plt.plot(xVals,yVals)
#plt.savefig("testoutputplot.png")  ##testplot, just graphing the given function 
#plt.show()


	



