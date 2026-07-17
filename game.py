import pygame
#events module for detecting windows and inputs stuff ()

pygame.init()

#Game graphics
screen= pygame.display.set_mode((640, 640))
background_color = (17, 17, 17)


left_player= pygame.image.load('girl.png').convert()
right_player= pygame.image.load('dude.png').convert()

running= True

while running:

    screen.fill(background_color)
    screen.blit(left_player, (50, 10))
    screen.blit(right_player, (590, 400))


    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
                    running = False


    
    pygame.display.flip()

pygame.quit

