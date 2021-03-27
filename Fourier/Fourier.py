#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import Fourier_Utilities


def square_wave_1_Cycle(xPoints):
    '''Generates a single cycle of a square wave for given points.'''

    # Create square wave.
    square = np.zeros(1000)
    square[500:] += 1
    return square


def modulated_sine_wave(xPoints):
    '''Generates modulated sign wave yn = sin(πn/N) sin(20πn/N).'''

    # Modulated sine wave.
    N = len(xPoints)
    modulatedSine = np.sin((np.pi*xPoints)/N)*np.sin((20*np.pi*xPoints)/N)
    return modulatedSine


def sawtooth_wave(xPoints):
    '''Generates 1 cycle of sawtooth wave.'''

    xPoints = xPoints - np.floor(xPoints)
    xPoints = xPoints % 1
    return xPoints


if __name__ == "__main__":

    print("Fourier Graphs")

    # Create 1000 evenly space points.
    N = 1000
    Ns = np.linspace(0, 1, num=N)

    # Plot
    fig, axes = plt.subplots(2, 3)
    fig.canvas.set_window_title("Fourier Graphs")
    axes[0, 0].plot(Ns, square_wave_1_Cycle(Ns))
    axes[0, 0].set_title('Square Wave')
    axes[0, 1].plot(Ns, modulated_sine_wave(Ns))
    axes[0, 1].set_title('Modulated Sine Wave')
    axes[0, 2].plot(Ns, sawtooth_wave(Ns))
    axes[0, 2].set_title('Sawtooth Wave')

    # Perform FFT to calculate coefficients.
    FFT_square_wave = Fourier_Utilities.FFT_for_points(square_wave_1_Cycle(Ns))
    FFT_sine_wave = Fourier_Utilities.FFT_for_points(modulated_sine_wave(Ns))
    FFT_sawtooth_wave = Fourier_Utilities.FFT_for_points(sawtooth_wave(Ns))

    # Plot FFT graphs.
    axes[1, 0].plot(FFT_square_wave)
    axes[1, 1].plot(FFT_sine_wave)
    axes[1, 2].plot(FFT_sawtooth_wave)
    plt.tight_layout()
    plt.show()
