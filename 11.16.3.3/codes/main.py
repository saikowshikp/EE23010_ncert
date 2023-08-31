import random

# Generate 100000 random numbers between 1 and 1000
length = 100000
random_numbers = [random.randint(1, 1000) for _ in range(length)]

# Count the numbers that are multiples of 2 or 9
multiples_of_2_or_9 = 0
for num in random_numbers:
    if num % 2 == 0 or num % 9 == 0:
        multiples_of_2_or_9 += 1

print("P_X(2 or 9) = ", multiples_of_2_or_9/length)

