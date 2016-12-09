__author__ = 'Patricia'

__author__ = 'Patricia'


import pygame, StaticItems, Level, MovingObjects

pygame.init()
pygame.display.update()



def instruction():
    clock = pygame.time.Clock()
    keepGoing = True

    screen = pygame.display.set_mode((800,600))



    background = pygame.image.load ("instructions.png")
    backgroundRect = background.get_rect()
    screen.blit (background, backgroundRect)








    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                donePlaying = False
                keepGoing = False
            elif key[pygame.K_ESCAPE]:
                donePlaying = True
                keepGoing = False



        pygame.display.flip()
    return donePlaying



