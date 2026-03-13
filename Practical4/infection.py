#Pseudocode:
#1.define variables and input values
#2.Initialize current infected and day counter
#3.loop:calculate daily infected
#4.stop loop when all students are infected
#5.print the total days


initial_infected=int(input("Please enter the initial infected number:"))
growth_rate=float(input("Please enter the daily growth rate:"))
total_students=91
current_infected=initial_infected
day_counter=0

#loop:calculate daily infected
while current_infected<total_students:
    day_counter+=1
    current_infected=current_infected*(1+growth_rate)
    print("Day",day_counter,"Infected students:",current_infected)
print("Total days to infect all students:",day_counter)
