# Quadratic equation solver
import math

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return "Invalid equation"
        return f"Linear equation: x = {-c / b}"

    disc = b * b - 4 * a * c
    if disc > 0:
        r1 = (-b + math.sqrt(disc)) / (2 * a)
        r2 = (-b - math.sqrt(disc)) / (2 * a)
        return f"Two real roots: {r1}, {r2}"
    elif disc == 0:
        return f"One real root: {-b / (2 * a)}"
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-disc) / (2 * a)
        return f"Complex roots: {real} ± {abs(imag)}i"

print(solve_quadratic(1, -5, 6))   
print(solve_quadratic(1, 2, 5))    