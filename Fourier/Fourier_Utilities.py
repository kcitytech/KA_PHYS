#!/usr/bin/env python3

import numpy as np


def FFT_for_points(points, ratio=.85):
    '''Perform FFT to get coefficients and save based on ratio.'''

    # Create array of zeros.
    count = points.shape[0]
    length = int(np.ceil(count/2.0))
    format = np.zeros(length, dtype=complex)

    # Perform FFT using numpy and keep arbitrary amount specified by ratio.
    transformed = np.fft.rfft(points)
    split = int(ratio*length)
    format[:split] = transformed[:split]

    # Perform inverse.
    inverse = np.fft.irfft(format)

    return inverse
