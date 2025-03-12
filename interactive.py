from calculation import calculate_roots


def get_numbers(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print(f"Error: expected a valid real number, got {value} instead")

