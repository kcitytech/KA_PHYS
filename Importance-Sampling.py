 #!/usr/bin/env python3
# Exercise 10.8: Calculate a value for the integral

import numpy as np
import matplotlib.pyplot as plt
import argparse


def g(x):
    ''' f(x) (x**-0.5)/(np.exp(x)+1) divided by weighting for probability distribution  1/(2*np.sqrt(x)).'''
    return 1/(1+np.exp(x))


def plot_histogram(points):
    ''' Show distribution of points used for importance sampling.'''

    # Generate histogram of sampled points.
    plt.figure("Exercise 10.8")
    plt.title(r'Distribution for calculating $\int_{0}^{1} \frac{x^-\frac{1}{2}}{e^x + 1}$')
    plt.hist(points, bins=50)
    plt.xlabel('Value')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    # Create parser to pass in number of samples to use.
    parser = argparse.ArgumentParser(description="Calculate integral using importance sampling.")
    parser.add_argument('--N', type=int, help='Number of samples to use.')
    args = parser.parse_args()

    # Specified number of randomly sampled points.
    N = 1_000_000

    # Use passed in N if specified.
    if args.N is not None:
        N = args.N

    # Perform random sampling from 0-1 for specified N count.
    random_samples = np.random.random(N)
    xs = random_samples**2
    integral = 2*(np.sum(g(xs))/N)

    print("Calculated value: {}".format(integral))
    print("    Actual value: 0.8389329600133814...")

    # Display histogram
    plot_histogram(xs)
