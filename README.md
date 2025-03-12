# Quadratic equation solver

## Description

This application is designed to solve quadratic equations of the form: ax^2 + bx + c = 0

where a, b, c are real numbers, with a  ≠ 0.

The application supports two modes of operation:

- **Interactive mode** - user enters coefficients manually
- **Non-interactive mode** - coefficients are read from a file

## Instructions

### Preparation

Clone the repository and navigate to its directory:

```sh
git clone https://github.com/ypapish/MTSD_lab1
cd /path/to/MTSD_lab1
```

Ensure that Python is installed:

```sh
python --version
```
### Interactive mode

Run the program without any command-line arguments:

```sh
python main.py
```

Enter the values of coefficients a, b, c, after which the program will display the equation and its roots.

### Non-interactive mode

Run the program with a single argument — the path to the file containing the coefficients:

```sh
python main.py /path/to/example.txt
```

## File format for non-interactive mode

The file must contain three numbers separated by spaces for example:

```
1 2 -3
```

## Revert commit

The repository contains a revert commit ```81b94d8```(reverts the previous changes to the discriminant calculation logic).


