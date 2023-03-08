

###############  PART THREE  ################

#  Create an interactive plot which allows the user to vary the degree of a Lagrange
# interpolating polynomial (not piecewise) for a certain set of knots and evaluation points.
# The plot should show the interpolating function and the knots (like this). For
# demonstration purposes use the function from part 1, i.e. but now
# plot the interval choose a modest number of knots and centre your
# interpolant (i.e. as the degree increases and more knots are required work from the
# centre out, as seen in the video)


import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact,interactive,fixed #imported all i need to get this scale changing thing
def f(x):
    return np.exp(x)*np.cos(10*x)

N=100
x= np.linspace(1,2,N)

def lagrange_polynomial_degree(a,b,M,N):
    midpoint = (a+b)/2
    x0 = np.array([midpoint])
    y0 = f(x0)
    pows = np.array([[0]])
    # Adding points by increasing degree for slider usage
    for i in range(2, M+1): 
        # If degree is odd
        if i % 2 == 1:
            # Index k of next points relative to the centre with 1/2 added for symmetricity between 
            # points at previous interpolation level
            k = i//2 + 1/2
            # Identify next right with index k multiplied by distance between adjacent points
            x_right = midpoint + k*(b-midpoint)/M
            x0 = np.concatenate((x0,[x_right]))
        else:
            # Identify next left with index only half of degree because degree is even
            x_left = midpoint - (i/2)*(midpoint-a)/M
            x0 = np.concatenate((x0,[x_left]))
        # Implement x0 value into f for the y0 array
        y0 = np.concatenate((y0, [f(x0[-1])]))
        pows = np.concatenate((pows, [[i]]))
    #y0 = f(x0)
    A = np.vander(x0)       
    a = np.linalg.solve(A,y0) 
    pows = (M-1-np.arange(M)).reshape(M,1)         
    xnew = np.reshape(x,(1,N))                     
    ynew = np.sum((xnew**pows)*a.reshape(M,1),axis=0) 
    return ynew

#3 - set up a plot which updates as it slides 

def polynomial_plot(a=1,b=2,degree=1):
    N = 100
    x = np.linspace(1, 2, N)
    x0 = np.linspace(a,b,10)
    y0 = f(x0)
    plt.figure(figsize=(8,5))
    plt.plot(x0,y0,label='data')
    plt.plot(x,lagrange_polynomial_degree(a,b,degree+1, N),label=f'poly interpolated data of degree {degree}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Varying the Degree in fitting the Lagrange Interpolating Polynomial to f(x) = exp(x)cos(10x)')
    plt.ylim(-7,8)
    plt.legend()
    plt.show() 

# Set knots from (1,12) so that interactive graph looks as required in video 
interactive(polynomial_plot,a=fixed(1),b=fixed(2), degree = (1,12))
