#The HURDLES LOOP CHALLENGE #DAY 06

#SUMITH SAI KORABOINA

#CODE RESOURCES FOR THE CHALLENGE

#RESOURCE 1
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json


#RESOURCE 2

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

#SOLUTION:-

#move()
#turn_left()
#jump()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def loop():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
loop()
loop()
loop()
loop()
loop()
loop()