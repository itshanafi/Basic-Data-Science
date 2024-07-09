# Write a Python program to demonstrate the usage of SciPy's Fourier transform functions, fft and ifft.
# Fourier analysis, a fundamental method in signal processing, is employed to decompose a function into a sum of periodic components
# and retrieve the original signal from those components. Write a program that interacts with the user, prompting them to
# input a sequence of values. Then utilize the fft function to compute the Fourier transform of the input sequence
# and the ifft function to calculate the inverse Fourier transform of the transformed sequence.
# And display the Fourier transform and the inverse Fourier transform of the provided input sequence.
# Input Format:
# The first line of input gets the sequence of values separated by commas.
# Output Format:
# Print the Fourier transform of the input sequence.
# Print the inverse Fourier transform of the transformed sequence.
# Sample Input and Output:
# Enter the sequence (comma-separated values):
# 0,1,2,3
# Fourier Transform of the sequence: [ 6.-0.j -2.+2.j -2.-0.j -2.-2.j]
# Inverse Fourier Transform of the transformed sequence: [0.+0.j 1.+0.j 2.-0.j 3.+0.j]

import numpy as np
from scipy.fftpack import fft, ifft

def main():
    sequence = list(map(float, input("Enter the sequence (comma-separated values): ").split(',')))
    fft_sequence = fft(sequence)
    inverse_fft_sequence = ifft(fft_sequence)
    print("Fourier Transform of the sequence:", fft_sequence)
    print("Inverse Fourier Transform of the transformed sequence:", inverse_fft_sequence)

if __name__ == "__main__":
    main()