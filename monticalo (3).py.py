import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

# Checking whether the dart hits within the circle
def is_hit(x, y):
    return (x**2 + y**2)**0.5 <= 1

# Simulating the dart throws
def simulate_dart_throw(num_darts):
    hits = 0
    for i in range(num_darts):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if is_hit(x, y):
            hits += 1
    prob_hit_circle = hits / num_darts
    return prob_hit_circle

# Accepting multiple values of N for dart throw simulations
n_values = [int(n) for n in input("Enter multiple values of N separated by commas: ").split(',')]

# Running the dart throw simulation for each value of N
results = []

for num_darts in n_values:
    prob_hit_circle = simulate_dart_throw(num_darts)
    estimate_value_pi = 4 * prob_hit_circle
    results.append({'N': num_darts, 'Pi Estimate': estimate_value_pi, 'True Pi': np.pi})

# Creating a DataFrame from the results
df = pd.DataFrame(results)

# Sorting the DataFrame by 'N' for plotting
df = df.sort_values(by='N')

# Saving the DataFrame to an Excel file with the name 'monti.xlsx'
df.to_excel('monti.xlsx', index=False)

# Displaying the Excel file content in the terminal
print("Excel Sheet Content:")
excel_df = pd.read_excel('monti.xlsx')
print(excel_df)

# Creating a line plot of N values against the estimated Pi values
plt.figure(figsize=(10, 6))
plt.plot(df['N'], df['Pi Estimate'], marker='o', linestyle='-', color='b')
plt.xlabel('N')  # Label for x-axis
plt.ylabel('Estimated Pi Value')  # Label for y-axis
plt.title('Estimated Pi Value vs. N')  # Title for the plot

# Saving the plot as an image file
plt.savefig('pi_estimation_vs_N_line_plot.png')

# Displaying the confirmation message
print("Results have been saved to 'monti.xlsx' and 'pi_estimation_vs_N_line_plot.png'")
