#!/usr/bin/env python3
# Exercise 8.4

import numpy as np
import matplotlib.pyplot as plt
import Pendulum_Functions as PK
import matplotlib.animation as animation

# Specifications for pendulum.
pendulum_arm_length_cm = 10.0
pendulum_degrees_theta_initial = 179.0 # Assuming on unit circle.
pendulum_angular_frequency_omega_initial = 0.0

# Environmental specifications.
gravity = 9.81

# Time parameters pendulum will be simulated for.
time_seconds_start = 0
time_seconds_stop = 330
time_steps = 1000
time_step_size = (time_seconds_stop-time_seconds_start)/time_steps
time_points = np.arange(time_seconds_start, time_seconds_stop, time_step_size)

# Create theta and omega points.
pendulum_degrees_theta_for_time_points, pendulum_angular_frequency_omega_for_time_points = PK.runge_kutta_theta_omega(time_points, time_step_size, pendulum_degrees_theta_initial, pendulum_angular_frequency_omega_initial, pendulum_arm_length_cm, gravity)

# Calculate the x & y positions of the pendulum bob based on the angle theta for each time step.
pendulum_x_positions_for_time_points = PK.pendulum_x_positions_for_angle(pendulum_degrees_theta_for_time_points, pendulum_arm_length_cm)
pendulum_y_positions_for_time_points = PK.pendulum_y_positions_for_angle(pendulum_degrees_theta_for_time_points, pendulum_arm_length_cm)

# Plot the relationship between the angle theta and angular freqeuncy.
plt.figure("Pendulum Lab")
plt.plot(pendulum_degrees_theta_for_time_points, np.abs(pendulum_angular_frequency_omega_for_time_points))
plt.xlabel("angle - theta - degrees")
plt.ylabel("angular frequency omega")
plt.show()

# Create a figure for animation.
fig = plt.figure("Pendulum Lab", figsize=(6,6))
ax  = fig.add_subplot(1, 1, 1)
ax.set_xlim(-15,15)
ax.set_ylim(-15,2)
ax.axis('equal')

# Create list of objects to add to animation.
artists = []

# Iterate for each position to create animation.
for i in range(500):
        
    # Access corresponding x,y position as well as angular frequency.
    x = pendulum_x_positions_for_time_points[i]
    y = pendulum_y_positions_for_time_points[i]
    angular_frequency_color = (np.abs(pendulum_angular_frequency_omega_for_time_points[i]) % 1)+ 0.001
    
    # Create the pendulum line from the origin to the x,y coordinate.
    pendulum_line, = ax.plot([0, x], [0, y], color='k', lw=2)
    
    # Create the pendulum bob and change color to indicate angular frequency.
    circle = plt.Circle((x, y), 0.5, color = [1, 0.5, angular_frequency_color])
    pendulum_bob = ax.add_patch(circle)
    
    # Add the pendulum line and bob.
    artists.append([pendulum_line, pendulum_bob])
    
# Create the animation.
pendulum_animation = animation.ArtistAnimation(fig, artists, interval=50)

# Display animation.
plt.show()