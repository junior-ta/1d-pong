import random
import time

# X-coordinates
tunnel_leftend= 0
tunnel_rightend= 100

ball_starting_coordinate= 50
ball_current_coordinate= ball_starting_coordinate

#Game keys
""" action 1: sending the ball back
    action 2: accelerating the ball"""

left_action1= 'Q'
left_action2=  'A'

right_action1= 'P'
right_action2= 'L'

#Speed
ball_speed= 1

#metadata
game_status="on"
current_ball_direction=""
left_score= 0
right_score= 0



#ball going left
def go_left():
    while ball_current_coordinate!=tunnel_leftend:
        ball_current_coordinate-= ball_speed

#ball going right
def go_right():
    while ball_current_coordinate!=tunnel_rightend:
        ball_current_coordinate+= ball_speed

#making the ball change direction
if ball_current_coordinate==tunnel_leftend and left_action1:
    go_right()
    current_ball_direction="right"

if ball_current_coordinate==tunnel_rightend and right_action1:
    go_left()
    current_ball_direction="left"


#accelerating the ball
    #write logic so that speed goes back to 1 after a speeding action
if left_action2 and current_ball_direction=="left":
    ball_speed+=1

if right_action2 and current_ball_direction=="right":
    ball_speed+=1


#scoring logic
if current_ball_direction=="left" and ball_current_coordinate==tunnel_leftend and not left_action1:
    right_score+= 1

if current_ball_direction=="right" and ball_current_coordinate==tunnel_rightend and not right_action1:
    left_score+= 1

#end of game logic
if right_score==11 or left_score==11:
    game_status= "off"

#restart
if restart:
    left_score=0
    right_score=0

    ball_current_coordinate= ball_starting_coordinate

#track speed
#winners page with restart


"""Game start"""

while game_status=="on":

    #initialize variables
    left_score= 0
    right_score= 0

    ball_current_coordinate= ball_starting_coordinate
    current_ball_direction= random.choice(["right","left"])

    if current_ball_direction=="right":
        go_right()
    else:
        go_left()

    #playing logic



"""Game stop"""