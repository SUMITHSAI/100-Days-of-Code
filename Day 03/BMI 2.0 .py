#  BMI 2.0 (SUMITH SAI KORABOINA)
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
h=float(height)
w=float(weight)
k=float(h*h)
bmi_index=(w/k)
bmi=int(round(w/k))
#bmi=float(float(w)/(float(h)*float(h)))
if bmi_index<18.5:
    #print(f"{weight} ÷ ({height} x {height}) = {bmi}")
    print("Your BMI is {bmi}, you are slightly underweight.")
elif bmi_index>18.5 and bmi<25:
    #print(f"{weight} ÷ ({height} x {height}) = {bmi}")
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi_index>25 and bmi<30:
    #print(f"{weight} ÷ ({height} x {height}) = {bmi}")
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi_index>30 and bmi<35:
    #print(f"{weight} ÷ ({height} x {height}) = {bmi}")
    print(f"Your BMI is {bmi}, you are obese.")
else:
    #print(f"{weight} ÷ ({height} x {height}) = {bmi}")
    print(f"Your BMI is {bmi}, you are clinically obese.")
# All the best :)