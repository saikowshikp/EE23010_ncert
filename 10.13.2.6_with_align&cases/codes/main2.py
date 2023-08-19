import random
from collections import Counter

# Set up the possible choices and their corresponding probabilities
choices = [1, 2, 3]
probabilities = [0.25, 0.25, 0.5]

# Generate 1000 random numbers using the specified probabilities
random_numbers = random.choices(choices, probabilities, k=1000)

# Count the occurrences of each number
number_counts = Counter(random_numbers)

# Calculate the observed probabilities
observed_probabilities = [number_counts[num] / len(random_numbers) for num in choices]

# Print the observed probabilities
#for num, observed_prob in zip(choices, observed_probabilities):
#    print(f"p_X({num})={observed_prob}")
print("p_X(1)=",observed_probabilities[0])
print("p_X(2)=",observed_probabilities[1])
print("p_X(3)=",observed_probabilities[2])
