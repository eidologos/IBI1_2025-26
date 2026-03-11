#population in 2004(10000 people)
a=508
#population in 2014(10000 people))
b=533
#population in 2024(10000 people))
c=555
#change from 2004-2014
d=b-a
#change from 2014-2024
e=c-b
# Print the population change values
print("Population change 2004-2014: ", d)
print("Population change 2014-2024: ", e)
# Compare d and e, judge the population growth trend
if d > e:
    print("the population growth in Scotland is decelerating")
elif e > d:
    print("the population growth in Scotland is accelerating")
else:
    print("the speed of population growth remains unchanged")

# Conclusion: d=25, e=22 
# d>e, population growth is decelerating


#define boolean variables
X=True
Y=False
W=X or Y
print("W=",W)
#the Truth Table of W:
# X |Y |W
# True |True |True
# True |False|True
# False|True |True
# False|False|False     
