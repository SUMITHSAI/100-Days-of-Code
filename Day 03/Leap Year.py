#Leap Year (SUMITH SAI KORABOINA)

year=int(input("Which year do you want to check? ")
year%4==0:
    print("Leap year.")
else:
    print("Not leap year.")

#OR 
#TRY THIS ENTIRE SOLUTION FOR CLEAR AND PERFECT ANSWER

year = int(input("Enter the year : "))
if year%4==0:
    if year%100:
        if year%400:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")

#All the best from SUMITH SAI KORABOINA :)