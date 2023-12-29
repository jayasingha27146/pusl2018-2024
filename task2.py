import random  # Importing the necessary libraries

def dice_throw():
    return [random.randint(1, 6) for i in range(10)]  # Generating 10 random numbers from 1 to 6


def simulate_dice_throw():

    num_of_simulation = 500  # Total number of simulations
    count_of_32 = 0  # Counting simulations that add up to 32

    for i in range(num_of_simulation):
        dice_throw_outcome = dice_throw()
        if sum(dice_throw_outcome) == 32:  # Checking if the sum equals 32
            count_of_32 += 1  # Counting simulations that add up to 32

    probability = count_of_32 / num_of_simulation  # Calculating the probability of getting a sum of 32 in 500 simulations

    print(f"Probability of getting a sum of 32 is: {probability} ")

simulate_dice_throw()

print(f"Random numbers from 10 dice: {dice_throw()}")  # Generating random numbers from 1 to 6 for 10 dice
