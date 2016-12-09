__author__ = 'Patricia'


import pygame, StaticItems, Level, MovingObjects

pygame.init()



def gameOver():
    clock = pygame.time.Clock()
    keepGoing = True


    screen = pygame.display.set_mode((800,600))



    background = pygame.image.load ("gameWin.png")
    backgroundRect = background.get_rect()
    screen.blit (background, backgroundRect)





    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                return False

        pygame.display.flip()


    pygame.quit()

