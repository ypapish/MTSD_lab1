import sys
import os
from calculation import calculate_roots


def read_coefficients(filename):
    if not os.path.exists(filename):
        print(f"Error: file {filename} does not exist")
        sys.exit(1)
    with open(filename, 'r') as file:
        line = file.readline().strip()
        coefficients = line.split()
    if len(coefficients) != 3:
        print("Error: invalid file format")
        sys.exit(1)
    try:
        a, b, c = map(float, coefficients)
    except ValueError:
        print("Error: invalid file format")
        sys.exit(1)
    if a == 0:
        print("Error: a cannot be 0")
        sys.exit(1)
    return a, b, c
