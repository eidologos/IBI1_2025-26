# 1. Input age, weight, gender, serum creatinine (Cr) as variables
# 2. Check if all inputs are within valid ranges:
#  Age < 100
#  Weight: 20 < w < 80
#  Cr: 0 < cr < 100
#  Gender is "male" or "female"
# 3. If any input is invalid, show error messages
# 4. If all inputs are valid, calculate CrCl using the formula:
# CrCl = ((140 - age) * weight) / (72 * Cr) * gender_factor(Factor: 1 for male, 0.85 for female)
# 5. print the result
age=int(input("Please enter your age(year):"))
while age >= 100:  #check the values of variable
     print("Age must be < 100!!!")
     age=int(input("Please enter your age(year):"))
weight=float(input("Please enter yourweight(kg):"))
while weight <= 20 or weight >= 80:
     print("Weight must be 20-80 kg!!!")
     weight=float(input("Please enter yourweight(kg):"))
gender=input("Please enter your gender(male/female):")
while gender not in ["male", "female"]:
    print("Gender must be male/female!!!")
    gender=input("Please enter your gender(male/female):")
cr=float(input("Please enter serum creatinine(μmol/L):"))
while cr <= 0 or cr >= 100:
    print("Cr must be 0-100 μmol/L!!!")
    cr=float(input("Please enter serum creatinine(μmol/L):"))

#difine gender factor
if gender == "male":
     factor=1.0
else:
     factor=0.85
# Calculate CrCl
crcl = ((140 - age) * weight) / (72 * cr) * factor
# print the result
print("CrCl ="+str(crcl))
