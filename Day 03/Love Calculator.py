#Love Calculator (SUMITH SAI KORABOINA)

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a=str.lower(name1)
b=str.lower(name2)
count=0
count+=a.count('t')
count+=a.count('r')
count+=a.count('u')
count+=a.count('e')
count+=b.count('t')
count+=b.count('r')
count+=b.count('u')
count+=b.count('e')


#love count (dil count) fro both the names i.e a & b
dil_count=0
dil_count+=a.count('l')
dil_count+=a.count('o')
dil_count+=a.count('v')
dil_count+=a.count('e')
#love count(dil count) for name 2 i.e b
dil_count+=b.count('l')
dil_count+=b.count('o')
dil_count+=b.count('v')
dil_count+=b.count('e')

love_score=int(str(count)+str(dil_count))
if love_score<10 or love_score>90:
    print("Your score is "+str(love_score)+", you go together like coke and mentos.")
elif love_score>=40 and love_score<=50:
    print("Your score is "+str(love_score)+", you are alright together.")
else:
    print("Your score is "+str(love_score)+".")

#ALL THE BEST FROM SUMITH SAI KORABOINA :)