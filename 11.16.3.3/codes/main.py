import random
length=100000
# Generate 100000 random numbers between 1 and 1000
random_numbers = [random.randint(1, 1000) for _ in range(length)]

# Filter numbers that are multiples of 2 or 9 and count them using len()
multiples_of_2_or_9 = filter(lambda num: num % 2 == 0 or num % 9 == 0, random_numbers)
no_of_multiples = len(list(multiples_of_2_or_9))

print("Pr((X=2)+(X=9)) = ",no_of_multiples/length)
