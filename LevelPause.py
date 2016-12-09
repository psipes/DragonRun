__author__ = 'Patricia'

import pygame, MazeDraw, mapLibrary, StaticItems, MovingObjects, Scoring
from time import sleep
from threading import Timer

pygame.init()



def btwnLvl (screen, lvl):
    pygame.init()



    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption ("Work....please?")


    background = pygame.image.load ("bg.png")
    backgroundRect = background.get_rect()
    screen.blit (background, backgroundRect)
    font = pygame.font.Font ("8bitlim.ttf", 35)
    text = "PRESS SPACE TO CONTINUE TO LEVEL %d" %lvl
    text1 = font.render (text, 1, (255, 255, 0))
    screen.blit (text1, (400,150))


    keepDoing = True
    while keepDoing:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_SPACE:
                    keepDoing = False
                    return lvl


    print "I DID IT"

