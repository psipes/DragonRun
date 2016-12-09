__author__ = 'Patricia'

import pygame, Level, mapLibrary, TitleScreen
from time import sleep
pygame.init()
pygame.key.set_repeat(30,30)






def main():

    actlvl =1
    actlives = 3
    actscore = 0

    keepGoing = True
    while keepGoing:
        donePlaying = TitleScreen.gameOver()
        if donePlaying == True:
            keepGoing = False

        while donePlaying == False:
            Level.background = pygame.image.load ("levelBG.png")
            Level.backgroundRect = Level.background.get_rect()
            Level.screen.blit (Level.background, Level.backgroundRect)
            playlvl =Level.stage(1, 3, 0, mapLibrary.Maze1)
            if playlvl == False:
                donePlaying = True
                break
            else:
                actlvl = playlvl[0]
                actlives = playlvl[1]
                actscore = playlvl[2]
                continuePlay = playlvl[3]

            if actlvl ==2:
                Level.background = pygame.image.load ("levelBG.png")
                Level.backgroundRect = Level.background.get_rect()
                Level.screen.blit (Level.background, Level.backgroundRect)

                playlvl = Level.stage(2, actlives, actscore, mapLibrary.Maze2)
                if playlvl == False:
                    donePlaying = True
                    break
                else:
                    actlvl = playlvl[0]
                    actlives = playlvl[1]
                    actscore = playlvl[2]
                    continuePlay = playlvl[3]
                    if continuePlay == False:
                        donePlaying = True

            if actlvl == 3:
                Level.background = pygame.image.load ("levelBG.png")
                Level.backgroundRect = Level.background.get_rect()
                Level.screen.blit (Level.background, Level.backgroundRect)

                continuePlay = Level.stage(3, actlives, actscore, mapLibrary.Maze3)
                if continuePlay == False:
                    donePlaying = True
                    break



    pygame.quit()
if __name__ == "__main__":
    main()

