import numpy as np
import random

# Determine if the dart hits within the circle
def is_in_circle(x, y):
    return (x ** 2 + y ** 2) ** 0.5 <= 1

# Simulate the dart throws
def dart_throw_simulation(num_darts):
    hits = 0
    for i in range(num_darts):
        # Generate random x and y within the radius of 1
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if is_in_circle(x, y):
            hits += 1

    # Probability of darts hitting the circle
    prob_hit_circle = hits / num_darts
    return prob_hit_circle

# Number of simulation runs
num_darts = int(input("Enter how many simulations: "))

hitting_the_circle = dart_throw_simulation(num_darts)

estimate_value_pi = 4 * hitting_the_circle

print(f"Estimated value of PI: {estimate_value_pi}")
print(f"The value of PI: {np.pi}")

print(f"The probability of a dart hitting the circle: {hitting_the_circle}")
print(f"Number of simulation runs: {num_darts}")