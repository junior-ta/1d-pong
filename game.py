import pygame
#events module for detecting windows and inputs stuff ()

pygame.init()

#Game graphics
screen= pygame.display.set_mode((1000, 640))
background_color = (17, 17, 17)


left_player= pygame.image.load('girl.png').convert()
right_player= pygame.image.load('dude.png').convert()
ball= pygame.image.load("ball.png").convert()
ball= pygame.transform.scale(ball, (20, 20))

running= True
ball_position= 504 #place in the middle when game starts


while running:

    screen.fill(background_color)
    screen.blit(left_player, (150, 266))
    screen.blit(right_player, (800, 274))
    screen.blit(ball, (ball_position, 306))


    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
                    running = False


    
    pygame.display.flip()

pygame.quit

