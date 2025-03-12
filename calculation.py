def calculate_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("Discriminant < 0. There are no real roots")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"Discriminant = 0. There is one root: x = {x}")
    else:
        x1 = (-b - discriminant**0.5) / (2 * a)
        x2 = (-b + discriminant**0.5) / (2 * a)
        print(f"Discriminant > 0. There are two roots: x1 = {x1}, x2 = {x2}")
