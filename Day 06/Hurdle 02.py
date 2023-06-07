#REEBORG'S WORLD

#HURDLE 2

#SUMITH SAI KORABOINA

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
while not at_goal():
    loop()