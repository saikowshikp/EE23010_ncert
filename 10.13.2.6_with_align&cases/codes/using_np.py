import numpy as np

# Set up the options and probabilities
options = [1, 2, 3]
probabilities = [0.25, 0.25, 0.5]
# Generate 1000 random numbers
random_numbers = np.random.choice(options, size=1000, p=probabilities)

# Count the occurrences of each number
counts = np.bincount(random_numbers)

#Printing the observed probabilites
print("Observed p_X(1) = ", counts[1]/len(random_numbers))
print("Observed p_X(2) = ", counts[2]/len(random_numbers))
print("Observed p_X(3) = ", counts[3]/len(random_numbers))
