__author__ = 'Patricia'



import pygame, StaticItems, Level, MovingObjects, Instructions

pygame.init()



def gameOver():
    clock = pygame.time.Clock()
    keepGoing = True

    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption ("Dragon? RUN!!!")


    background = pygame.image.load ("titleBG.png")
    backgroundRect = background.get_rect()
    screen.blit (background, backgroundRect)

    dragoTest = StaticItems.Blackout2 ((1200, 300))



    dragonstext = StaticItems.dragonTxt ()
    dragonstext.rect.center = ((400,200))

    runText = MovingObjects.RunText()
    runText.rect.center = ((-200, 310))

    dragonScroll = StaticItems.dragonBG()
    dragonScroll.rect.center = ((-500, 400))

    blackout = StaticItems.Blackout2((1200, 300))



    blackoutgroup = pygame.sprite.Group (blackout)
    rungroup = pygame.sprite.Group (runText)
    dragoGroup = pygame.sprite.OrderedUpdates (dragoTest, dragonstext)
    scrollGroup = pygame.sprite.Group (dragonScroll)


    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True

            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                blackout.rect.centerx = 400
                donePlaying = Instructions.instruction()

                keepGoing =False

            elif key[pygame.K_ESCAPE]:
                donePlaying =True
                keepGoing = False

        if runText.rect.centerx >400 and runText.stopCount == True:
            dragonScroll.rect.center = ((400, 300))











        dragoGroup.clear (screen, background)
        scrollGroup.clear (screen, background)
        rungroup.clear (screen, background)
        blackoutgroup.clear (screen, background)

        dragoGroup.update ()
        scrollGroup.update()
        rungroup.update()
        blackoutgroup.update()

        dragoGroup.draw (screen)
        scrollGroup.draw (screen)
        rungroup.draw (screen)
        blackoutgroup.draw(screen)

        pygame.display.flip()

    return donePlaying

