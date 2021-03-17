#!/usr/bin/env python3
# Exercise 7.4

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import DOW dataset.
dow = pd.read_csv('DOW.txt',names=['Closing_Value'])

# Calculate coefficients using numpy fast fourier transform function.
coefficients = np.fft.rfft(dow.Closing_Value)

# Calculate indexes of 2% and 10%.
index10Percent = int(np.ceil(len(coefficients)*.1))
index2Percent  = int(np.ceil(len(coefficients)*.02))

# Can safely perform inverse without copying if done in order since 10% > 2%.
coefficients[index10Percent:] = 0
inverse10                     = np.fft.irfft(coefficients)
coefficients[index2Percent:]  = 0
inverse2                      = np.fft.irfft(coefficients)

# Plot dow.
plt.figure('DOW')
plt.title('2006-2010')
plt.plot(      dow,c='r',label="Original")
plt.plot(inverse2 ,c='g',label="Inverse of first 10% of FFT.")
plt.plot(inverse10,c='b',label="Inverse of first   2% of FFT.")
plt.xlabel('Trading Day')
plt.ylabel('Closing Value ($)')
plt.legend()
plt.show()