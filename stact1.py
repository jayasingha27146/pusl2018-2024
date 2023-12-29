from itertools import product

# Sets to store outcomes
all_outcomes = set()  # To store all unique outcomes of the dice throws
selected_outcomes = set()  # To store unique outcomes that sum up to 32

# Counters for outcomes
count_all = 0  # To count the total number of outcomes
count_selected = 0  # To count the total number of outcomes that add up to 32

# Loop through all possible outcomes of throwing 10 dice
for p in product(range(1, 7), repeat=10):
    count_all += 1  # Counting the number of total outcomes
    sorted_p = tuple(sorted(p))  # Sorting the tuple and converting it back to a tuple
    all_outcomes.add(sorted_p)  # Adding the sorted tuples to the set of all outcomes

    if sum(sorted_p) == 32:  # Checking if the sum of the sorted tuple is 32
        count_selected += 1  # Counting the number of outcomes that sum up to 32
        selected_outcomes.add(sorted_p)  # Adding tuples that sum up to 32 to the set of selected outcomes

# Calculating probabilities
length_all_outcomes = len(all_outcomes)  # Finding the number of tuples in all outcomes
length_selected_outcomes = len(selected_outcomes)  # Finding the number of tuples in selected outcomes
probability = length_selected_outcomes / length_all_outcomes  # Probability of 10 dice summing up to 32

# Displaying the probability and selected outcomes
print(f"Probability of all possible ways of making 32 from 10 dice (without considering order): {probability}")
print("\n")
print("The possible ways of making 32 from 10 dice:")
for i in selected_outcomes:
    print(i)
