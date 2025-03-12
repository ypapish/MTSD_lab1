def calculate_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("Discriminant < 0. There are no real roots")
    else:
        x1 = (-b - discriminant**0.5) / (2 * a)
        x2 = (-b + discriminant**0.5) / (2 * a)
        if discriminant == 0:
            print(f"Discriminant = 0. There is one root: x = {x1}")
        else:
            print(f"Discriminant > 0. There are two roots: x1 = {x1}, x2 = {x2}")
