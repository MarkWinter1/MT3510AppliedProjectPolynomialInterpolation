

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


# Set the knots and evaluation points
knots = np.linspace(-3, 3, 11)
x = np.linspace(-4, 4, 100)

#the test function to use from part 1
f = lambda x: (numpy.e)**x * numpy.cos(10*x)

# Define the function to calculate the Lagrange interpolating polynomial
def lagrange_poly(xk, yk, x):
    n = len(xk)
    p = 0
    for k in range(n):
        L = 1
        for j in range(n):
            if j != k:
                L *= (x - xk[j]) / (xk[k] - xk[j])
        p += yk[k] * L
    return p

# Create the initial plot with the knots and function to be interpolated
fig, ax = plt.subplots()
ax.plot(x, f(x), label='Function to be interpolated')
ax.scatter(knots, f(knots), color='red', label='Knots')

# Define the function to be called when the degree slider is changed
def update(degree):
    # Calculate the Lagrange interpolating polynomial for the current degree
    xk = knots[(len(knots)-degree-1)//2 : (len(knots)+degree+2)//2]
    yk = f(xk)
    p = lagrange_poly(xk, yk, x)
    
    # Update the plot with the new polynomial
    ax.cla()
    ax.plot(x, f(x), label='Function to be interpolated')
    ax.scatter(knots, f(knots), color='red', label='Knots')
    ax.plot(x, p, label=f'Lagrange polynomial of degree {degree}')
    ax.legend()

conda install -c anaconda ipywidgets

# Create the degree slider and set the initial degree to 0
from ipywidgets import interact
interact(update, degree=(0, len(knots)-1, 1))
