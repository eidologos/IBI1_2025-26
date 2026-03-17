heart_rate=[72,76,126,85,90,59,76,131,88,121,64]
patient_number=len(heart_rate)
mean_heart_rate=sum(heart_rate)/patient_number
print("the number of patients is:",patient_number)
print("the mean heart rate is:",mean_heart_rate)
#determine the number of patients into three categories
#low heart rate: <60, normal heart rate: 60-120, high heart rate: >120
low=0
normal=0
high=0
for rate in heart_rate:
    if rate<60:
        low+=1
    elif 60<=rate<=120:
        normal+=1
    else:
        high+=1
print("the number of patients with low heart rate is:",low)
print("the number of patients with normal heart rate is:",normal)
print("the number of patients with high heart rate is:",high)
#identify which category has the most patients
if low>normal and low>high:
    print("the category with the most patients is: low heart rate")
elif normal>low and normal>high:
    print("the category with the most patients is: normal heart rate")
else:
    print("the category with the most patients is: high heart rate")
#create a pie chart to take the initial input and reports the number of patients in each category
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
labels=["Low heart rate","Normal heart rate","High heart rate"]
sizes=[low,normal,high]
colors=["lightblue","lightgreen","lightcoral"]
plt.pie(sizes,labels=labels,colors=colors,autopct="%1.1f%%",startangle=140)
plt.axis("equal")
plt.title("Distribution of Heart Rate Categories")
plt.show()