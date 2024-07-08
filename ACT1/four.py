import math
import numpy as np
import matplotlib.pyplot as plt

with open('multiple.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    a, b, c = map(float, line.strip().split())
    discriminant = b**2 - 4 * a * c

    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        roots = [root1, root2]
    else:
        roots = []

    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    for root in roots:
        plt.plot(root, 0, 'ro')

    plt.ylim(-50, 50)
    plt.title('Quadratic Function and its Roots')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.legend()
    plt.grid(True)
    plt.show()
