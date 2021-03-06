#!/usr/bin/env python3
# Exercise 3.2: Curve plotting

import matplotlib.pyplot as plt
import numpy as np

# Create subplots and specify size.
fig, axes = plt.subplots(1,3)
fig.canvas.set_window_title('Graphs')
fig.set_size_inches(9,3)

# Prevent cutoff subplot titles.
plt.tight_layout(pad=2)

# Create list of points so that values are in range 0 ≤ θ < 2π.
a = np.linspace(0, 2*np.pi, 1000)

# Define equations for x & y.
x = 2*np.cos(a) + np.cos(2*a)
y = 2*np.sin(a) - np.sin(2*a)

# Create plot for deltoid curve using x & y points.
axes[0].set_title('Deltoid Curve')
axes[0].plot(x, y, color='r', linewidth=.5)
axes[0].axis([-4, 4, -4, 4])

# Create list of points so that values are in range 0 ≤ θ < 10π.
theta = np.linspace(0, 10*np.pi, 1000, endpoint=True)
r     = theta**2
x     = r*np.cos(theta)
y     = r*np.sin(theta)

# Plot spiral.
axes[1].set_title('Galilean Spiral')
axes[1].plot(x, y, color='g', linewidth=.5)
axes[1].axis([-1000, 1000, -1000, 1000])

# Create list of points so that values are in range 0 ≤ θ < 10π.
theta = np.linspace(0, 24*np.pi, 100000, endpoint=True)
r     = np.exp(np.cos(theta)) -2 * np.cos(4*theta) + np.sin(theta/12)**5
x     = r*np.cos(theta)
y     = r*np.sin(theta)

# Plot Fey's function
axes[2].set_title('Fey\'s function')
axes[2].plot(x,y,color='b',linewidth=.5)

# Display graph of 3 subplots.
plt.show()