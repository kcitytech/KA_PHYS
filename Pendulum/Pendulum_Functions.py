#!/usr/bin/env python3
# Pendulum Functions

import numpy as np

def pendulum_x_positions_for_angle(angle_degrees_theta, pendulum_arm_length_cm):
    '''x'''
    return pendulum_arm_length_cm * np.cos(np.deg2rad(angle_degrees_theta))

def pendulum_y_positions_for_angle(angle_degrees_theta, pendulum_arm_length_cm):
    '''y'''
    return pendulum_arm_length_cm * np.sin(np.deg2rad(angle_degrees_theta))

def partial_angle_degrees_theta(angular_frequency_omega):
    '''Calculate partial of angle theta with respect to time.'''
    return angular_frequency_omega

def partial_angular_frequency_omega(angle_degrees_theta, pendulum_arm_length_cm, gravity):
    '''Calculate partial of angular velocity omega with respect to time.'''
    return -(gravity/pendulum_arm_length_cm)*np.sin(angle_degrees_theta)

def calculate_theta_and_omega(components, time_step, pendulum_arm_length_cm, gravity): # Time step is not used.
    '''Calculate the partial dervivatives for theta and omega for Runge-Kutta values.'''
    theta = components[0]
    omega = components[1]
    partial_theta = partial_angle_degrees_theta(omega)
    partial_omega = partial_angular_frequency_omega(theta, pendulum_arm_length_cm, gravity)
    
    return np.array([partial_theta, partial_omega])
    
def runge_kutta_theta_omega(time_points, time_step_size, theta_initial, omega_initial, pendulum_arm_length_cm, gravity):
    '''Calculate theta and omega values at each time step.'''
    
    # Convert to radians to fix issue when calculing sin/cos later.
    theta_initial = np.deg2rad(theta_initial)# *= (np.pi/180)
    
    # Create a component array of theta and omega.
    components = np.array([theta_initial, omega_initial])
    
    # Determine the values of theta and omega for every time step.
    theta_values = np.array([])
    omega_values = np.array([])
        
    # Iterate for time steps.
    for time_step in time_points:
        
        # Add points to respective array.
        theta_values = np.append(theta_values, components[0])
        omega_values = np.append(omega_values, components[1])
        
        # Utilize function provided in slides.
        k1 = time_step_size * calculate_theta_and_omega(components, time_step, pendulum_arm_length_cm, gravity)
        k2 = time_step_size * calculate_theta_and_omega(components + 0.5 * k1, time_step + (0.5 * time_step_size), pendulum_arm_length_cm, gravity)
        k3 = time_step_size * calculate_theta_and_omega(components + 0.5 * k2, time_step + (0.5 * time_step_size), pendulum_arm_length_cm, gravity)
        k4 = time_step_size * calculate_theta_and_omega(components + k3, time_step + time_step_size, pendulum_arm_length_cm, gravity)

        # Update value for theta and omega components.
        components += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        
    # Convert back from radians to degrees
    theta_values = np.rad2deg(theta_values)
    theta_values = normalize_theta_points_for_unit_circle(theta_values, theta_initial)
        
    return theta_values, omega_values # Optionally wrap omega_points in np.abs() for absolute.

def normalize_theta_points_for_unit_circle(theta_points, theta_initial):
    '''Normalize values to plot correctly.'''
    
    # Normalize values. NOTE: Issue is occuring for values close to 270° likely due to interval.
    normalized_theta_values = []
    
    # Iterate points to normalize.
    for theta in theta_points:
        
        # Calculate change in value.
        change = (179.0-np.abs(theta))/2.0
        
        # Update value based on new point.
        if theta == 0.0:
            normalized_theta_values.append(270.0)
        elif theta > 0.0:
            normalized_theta_values.append(179.0+change)
        elif theta < 0.0:
            normalized_theta_values.append(361.0-change)

    return np.array(normalized_theta_values)