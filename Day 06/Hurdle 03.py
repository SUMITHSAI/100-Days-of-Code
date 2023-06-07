#REEBORG'S WORLD

#HURDLE 3

#SUMITH SAI KORABOINA

#move()
#turn_left()
#jump()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def loop():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    if wall_in_front():
        loop()
    else:
        move()