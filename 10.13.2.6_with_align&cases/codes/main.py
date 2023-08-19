import random
samp_len=1000
# Set up the possible choices and their corresponding probabilities
choices = [1, 2, 3]
probabilities = [0.25, 0.25, 0.5]

# Generate 1000 random numbers using the specified probabilities
random_numbers = random.choices(choices, probabilities, k=samp_len)

# Print the generated random numbers
#print(random_numbers)

count1=0
count2=0
count3=0

for i in range(0,999):
	if random_numbers[i]==1:
		count1= count1+1
	elif random_numbers[i]==2:
		count2=count2+1
	elif random_numbers[i]==3:
		count3=count3+1

prob1=count1/samp_len
prob2=count2/samp_len
prob3=count3/samp_len

#p_X(k)=probability of the arrow to stop in region k

print("p_X(1)=",prob1)
print("p_X(2)=",prob2)
print("p_X(3)=",prob3)
