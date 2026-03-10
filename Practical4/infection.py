#Pseudocode:
#1.define viarables
#2.Initialize current infected and day counter
#3.loop:calculate daily infected
#4.stop loop when all students are infected
#5.print the total days


initial_infected=5
growth_rate=0.4
total_students=91
current_infected=initial_infected
daycounter=0

#loop:calculate daily infected
while current_infected<total_students:
    daycounter+=1
    current_infected=current_infected*(1+growth_rate)
    print("Day",daycounter,"Infected students:",current_infected)
print("Total days to infect all students:",daycounter)
