import pygame
import random
#events module for detecting windows and inputs stuff ()

pygame.init()

#Game graphics
screen= pygame.display.set_mode((1000, 640))
background_color = (17, 17, 17)


left_player= pygame.image.load('girl.png').convert_alpha()
right_player= pygame.image.load('dude.png').convert_alpha()

ball= pygame.image.load("ball.png").convert()
ball= pygame.transform.scale(ball, (20, 20))
ball.set_colorkey((17,17,17))

left_racket= pygame.transform.scale((pygame.image.load("racket.png").convert()), (50,40))
left_racket.set_colorkey((17,17,17))
right_racket= pygame.transform.scale((pygame.image.load("racket.png").convert()), (50,40))
right_racket.set_colorkey((17,17,17))

controls_panel= pygame.image.load("controls.png").convert()
controls_panel.set_colorkey((33,33,33))
# controls_panel= pygame.transform.scale(controls_panel, (600,100))
# print(controls_panel.get_size())

#coordinates
tunnel_leftend= 225
tunnel_rightend= 750


#Game variables
running= True

ball_position= 504 #place in the middle when game starts
current_ball_direction= random.choice(["right","left"])


clock= pygame.time.Clock()
delta_time= 0.1

#scoreboard
font= pygame.font.Font(None, size=60)
left_score=0
right_score=0


#Game loop
while running:

    screen.fill(background_color)
    screen.blit(left_player, (150, 266))
    screen.blit(left_racket, (195, 300))
    screen.blit(right_player, (800, 274))
    screen.blit(right_racket, (750, 300))
    screen.blit(ball, (ball_position, 306))

    #.....ball movement.....
    #check if the ball is at a deadend
    if ball_position<=tunnel_leftend:
        current_ball_direction="right"   
    elif ball_position>=tunnel_rightend:
         current_ball_direction="left"

    #move the ball in a direction     
    if current_ball_direction=="right":
        ball_position+= 75 * delta_time #initial speed is 75px/seconds
    else:
        ball_position-= 75 * delta_time          



    #.....Scoreboard and controls.....
    score= f"{left_score} : {right_score}"
    score= font.render(score, True, (130,130,130))
    screen.blit(score, (450, 50))

    screen.blit(controls_panel, (50,530))
    

    #.....Restart....


    #.....end the game....
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
                    running = False


    
    
    pygame.display.flip()

    #clock.tick() returns the numbers of milliseconds since the second
    delta_time= clock.tick(60)/1000  #gives the time in seconds between each frame with the game capped at 60 frames/second
    delta_time= max(0.001, delta_time) #make sure delta time is never 0

pygame.quit

