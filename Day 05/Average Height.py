#Average Height DAY 05 {SUMITH SAI KORABOINA}

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum=0
for heigth in student_heights:
    sum=sum+heigth

size=len(student_heights)
average=round(sum/size)
print(average)

#ALL THE BEST FOR EVERYONE
#SUMITH SAI KORABOINA