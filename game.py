import pygame
import random
#events module for detecting windows and inputs stuff ()

pygame.init()
running= True

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
green_ltimer, green_rtimer= 0, 0
red_ltimer, red_rtimer= 0, 0
yellow_ltimer, yellow_rtimer= 0, 0

controls_panel= pygame.image.load("controls.png").convert()
controls_panel.set_colorkey((33,33,33))

#coordinates
tunnel_leftend, tunnel_rightend= 225, 750
ball_position= 490 #place in the middle when game starts

#Game variables

current_ball_direction= random.choice(["right","left"])

left_action1= False
left_action2=  False

right_action1= False
right_action2= False

racket_sensitivity= 50
ball_speed= 125

clock= pygame.time.Clock()
delta_time= 0.1

#speed control
speedup= 75

#scoreboard
font= pygame.font.Font(None, size=60)
left_score=0
right_score=0

#restart
restart_font= pygame.font.Font(None, size=30)
restart_button = pygame.Rect(15, 15, 90, 30) 
restart_button2= pygame.Rect(455, 352, 90, 30) 

#end of game menu
eog= False
winner=""


def reset_game():
    global left_score, right_score
    global ball_position, current_ball_direction
    global left_action1, left_action2, right_action1, right_action2
    global green_ltimer, green_rtimer
    global yellow_ltimer, yellow_rtimer
    global red_ltimer, red_rtimer
    global eog, winner

    left_score = 0
    right_score = 0

    ball_position = 490
    current_ball_direction = random.choice(["left", "right"])

    green_ltimer = green_rtimer = 0
    yellow_ltimer = yellow_rtimer = 0
    red_ltimer = red_rtimer = 0

    left_action1, left_action2, right_action1, right_action2=False, False, False, False


    winner = ""
    eog = False

#.....................Game loop..........................................
#........................................................................
while running:

    #Check If the game should run or stop
    if left_score >= 4:
        winner= "Left Player"
        eog= True
    elif right_score >= 11:
        winner= "Right Player"
        eog= True


#-------------------------Game going on--------------------------------------------------------
    if eog == False:


    #.....display.....
        screen.fill(background_color)
        
        #1.....Scoreboard and controls.....
        score= f"{left_score} : {right_score}"
        score= font.render(score, True, (130,130,130))
        screen.blit(score, (450, 50))
        screen.blit(controls_panel, (50,530))
 
        #2.....players and rackets......
        screen.blit(left_player, (150, 266))
        screen.blit(ball, (ball_position, 306))
        screen.blit(right_player, (800, 274))

        if green_ltimer>0:
            green_ltimer -= 1
            pygame.draw.rect(screen, (0, 255, 0), (218.5, 300, 5, 40),0)
        elif red_ltimer>0:
            red_ltimer -= 1
            pygame.draw.rect(screen, (255, 0, 0), (218.5, 300, 5, 40),0)
        elif yellow_ltimer>0:
            yellow_ltimer -= 1
            pygame.draw.rect(screen, (255, 255, 0), (218.5, 300, 5, 40),0)    
        else:
            screen.blit(left_racket, (195, 300))

        
        if green_rtimer>0:
            green_rtimer -= 1
            pygame.draw.rect(screen, (0, 255, 0), (773.5, 300, 5, 40),0)
        elif red_rtimer>0:
            red_rtimer -= 1
            pygame.draw.rect(screen, (255, 0, 0), (773.5, 300, 5, 40),0)
        elif yellow_rtimer>0:
            yellow_rtimer -= 1
            pygame.draw.rect(screen, (255, 255, 0), (773.5, 300, 5, 40),0)
        else:
            screen.blit(right_racket, (750, 300))


        #3.....restart button....
        pygame.draw.rect(screen, (220, 220, 220), restart_button, border_radius=4)
        pygame.draw.rect(screen, (0, 0, 0), restart_button, 2, border_radius=4)

        text = restart_font.render("Restart", True, (0, 0, 0))
        text_rect = text.get_rect(center=restart_button.center)
        screen.blit(text, text_rect)

    #....key detection.....
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if restart_button.collidepoint(event.pos):
                        reset_game()


            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_p:
                    right_action1=True
                if event.key== pygame.K_l:
                    right_action2= True
                
                if event.key== pygame.K_q:
                    left_action1= True
                if event.key== pygame.K_a:
                    left_action2= True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    left_action2 = False

                if event.key == pygame.K_l:
                    right_action2 = False           
        
        
    #.....ball movement.....
        #Ball got hit (point saved)
        if ball_position <= (tunnel_leftend + racket_sensitivity) and left_action1 == True:
            current_ball_direction="right"
            green_ltimer=5


        elif ball_position >= (tunnel_rightend - racket_sensitivity) and right_action1 == True:
            current_ball_direction="left"
            green_rtimer=5
            screen.blit(right_racket, (750, 300))
        
        #Ball is at a deadend (point lost)
        if ball_position <= tunnel_leftend:
            right_score += 1
            red_ltimer= 5
            current_ball_direction="right"
            ball_position= tunnel_leftend + 2 #to avoid double counting

        elif ball_position >= tunnel_rightend:
            left_score += 1
            red_rtimer= 5
            ball_position= tunnel_rightend - 2
            current_ball_direction="left"

        #Ball moving freely (no point in play at the moment)    
        if current_ball_direction=="right":
            if left_action2 == True: #check for speeding
                ball_position += (ball_speed + speedup) * delta_time
            else:
                ball_position += ball_speed * delta_time
            
                

            if ball_position < (tunnel_rightend - racket_sensitivity) and ball_position > (tunnel_leftend + racket_sensitivity):
                #dtect if the user is spamming the racket when no pint is in play
                if right_action1 == True:
                    yellow_rtimer= 5
                if left_action1 == True:
                    yellow_ltimer= 5

        else: #ball going left otherwise
            if right_action2 == True: #check for speeding
                ball_position -= (ball_speed + speedup) * delta_time
            else:
                ball_position-= ball_speed * delta_time          
            
            if ball_position < (tunnel_rightend - racket_sensitivity) and ball_position > (tunnel_leftend + racket_sensitivity):
                if right_action1 == True:
                    yellow_rtimer= 5
                if left_action1 == True:
                    yellow_ltimer= 5



    #.....Clock.....
        #clock.tick() returns the numbers of milliseconds since the second
        delta_time= clock.tick(60)/1000  #gives the time in seconds between each frame with the game capped at 60 frames/second
        delta_time= max(0.001, delta_time) #make sure delta time is never 0

    #.....Helper.....   
        #resetting command variables to default so that a winning play must be timed to the millisecond
        left_action1= False
        right_action1= False

    
#-----------------------Game ended------------------------------------------------------
    elif eog == True:
        screen.fill(background_color)
        
        #Congrats message display
        msg= f"{winner} won, CONGRATS (^_^)!"
        text= font.render(msg, True, (255,255,255))
        screen.blit(text, (150, 299))

        #restart button display
        pygame.draw.rect(screen, (220, 220, 220), restart_button2, border_radius=4)
        pygame.draw.rect(screen, (0, 0, 0), restart_button2, 2, border_radius=4)

        text = restart_font.render("Restart", True, (0, 0, 0))
        text_rect = text.get_rect(center=restart_button2.center)
        screen.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    if restart_button2.collidepoint(event.pos):
                        reset_game()

                        #reset clock
                        clock.tick(60)
                        delta_time=0

    pygame.display.flip()
    
pygame.quit

