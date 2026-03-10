# What does this piece of code do?
# Answer:This code generates 11 random numbers between 1 and 9,sums them up and print the final value

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0 #record the sum value of random numbers
progress=0 #control the number of random numbers
while progress<=10: 
	progress+=1 #ensure that 11 random numbers will be generated
	n = randint(1,10) #generate a random number between 1 and 9
	total_rand+=n #add the random number of this round to the total sum

print(total_rand)

