from calculation import calculate_roots


def get_numbers(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print(f"Error: expected a valid real number, got {value} instead")


def interactive_mode():
    a = get_numbers("a = ")
    if a == 0:
        print("Error: a can't be 0")
        return
    b = get_numbers("b = ")
    c = get_numbers("c = ")
    print(f"Equation is: {a}x^2 + {b}x + {c} = 0")
    calculate_roots(a, b, c)
