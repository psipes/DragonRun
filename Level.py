__author__ = 'Patricia'

import pygame, MazeDraw, mapLibrary, StaticItems, MovingObjects, Scoring, GameOver, GameWin
from time import sleep
from threading import Timer

pygame.init()



screen = pygame.display.set_mode((800,600))


background = pygame.image.load ("titleBG.png")
backgroundRect = background.get_rect()
screen.blit (background, backgroundRect)






def stage(lvl, livesLeft, points, mazeMap):
    """PULLS PARAMETERS FROM MAIN"""


    """SCORING AND LIVES"""
    score = Scoring.Score(screen)
    score.score = points
    lives = Scoring.Lives()
    lives.lives = livesLeft
    scoreSprite = pygame.sprite.Group (score)


    """LEVEL SETUP"""
    level = lvl

    mazeLayout = mazeMap.mapLayout
    startX = mazeMap.startx
    startY = mazeMap.starty
    lifeSprite1 = StaticItems.LifeAvatar((900, 140))
    lifeSprite2 = StaticItems.LifeAvatar((900, 140))
    lifeSprite3 = StaticItems.LifeAvatar ((900, 140))
    lifeSprite4 = StaticItems.LifeAvatar ((900,140))

    lifeAvatars = pygame.sprite.Group (lifeSprite1, lifeSprite2, lifeSprite3, lifeSprite4)
    levelMaze = MazeDraw.DrawMaze(mazeLayout, startX, startY)
    mazegroup = levelMaze.mazeCoords()


    """Moving Things"""

    player = (MovingObjects.Player(levelMaze.playerStart()))
    playerSprite = pygame.sprite.Group (player)

    dragon0 = MovingObjects.Dragon(levelMaze.dragonSprites()[0])
    dragon1 = MovingObjects.Dragon(levelMaze.dragonSprites()[1])
    dragon2 = MovingObjects.Dragon(levelMaze.dragonSprites()[2])
    dragon3 = MovingObjects.Dragon(levelMaze.dragonSprites()[3])

    dragonSprites = pygame.sprite.Group (dragon0, dragon1, dragon2, dragon3)

    dragonColor = 0
    for dragon in dragonSprites:
        dragon.colorSet = dragonColor
        dragonColor += 1

    treasure = MovingObjects.Treasure((levelMaze.treasureStart()))
    treasureGroup = pygame.sprite.Group (treasure)


    """CONDITIONAL, PRINCESS SPAWN"""
    if level == 3:
        princess = MovingObjects.Princess(levelMaze.princessStart())

        princessGroup = pygame.sprite.Group (princess)
        #used to signify when princess can start moving
        gemTouch = False


    """Static Things"""
    crumbs = levelMaze.breadcrumbCoords()
    crumbGroup = pygame.sprite.Group (crumbs)
    pelletMax = 0
    for items in crumbGroup:
        pelletMax +=1
    pelletMax -=10

    potions = levelMaze.potionCoords()
    potionGroup = pygame.sprite.Group (potions)
    potionMax = 0
    for items in potionGroup:
        potionMax +=1


    levelText = StaticItems.Text2(screen, lvl)
    textGroup = pygame.sprite.Group (levelText)






    clock = pygame.time.Clock()
    keepGoing = True

    collisionCount = 0




    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                return keepGoing
            player.handle_keys()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                keepGoing = False
                return keepGoing

        """Set princess to invisible until needed"""
        if level == 3:
            if gemTouch ==False:
                princess.image = pygame.image.load ("invisible.png")
                princess.rect.center = levelMaze.princessStart()


        """Gem spawns and level Flips"""
        if score.score >-1 and score.score < 1000*level + 400* (level)+ 500*(level-1):
            treasure.rect.center = ((levelMaze.treasureStart()))
        if score.score > 1000*level + 400* (level)+ 500*(level-1):
            if level == 1:
                treasure.image = pygame.image.load ("treasure1.png")
            if level == 2:
                treasure.image = pygame.image.load ("treasure2.png")
            if level == 3:
                treasure.image = pygame.image.load ("treasure3.png")


        if player.rect.colliderect (treasure.rect) and score.score > 1000*level + 400* (level)+ 500*(level-1): #300*level:
            if level ==1 or level == 2:
                level = level
                dragon0.stopFull()
                dragon1.stopFull()
                dragon2.stopFull()
                dragon3.stopFull()


                sleep (2)

                score.score+=250
                level += 1
                scoreLife = [level, lives.lives, score.score, True]
                return scoreLife
            if level ==3:
                if pygame.sprite.spritecollide (player, treasureGroup, True):
                    gemTouch = True
                    princess.image = pygame.image.load ("princess.png")



        """LIVES"""

        if lives.lives ==-1:
            GameOver.gameOver()
            return False


        if lives.lives ==4:
            lifeSprite1.rect.center = ((772, 155))
            lifeSprite2.rect.center = ((722, 155))
            lifeSprite3.rect.center = ((672, 155))
            lifeSprite4.rect.center = ((622, 155))

        if lives.lives == 3:
            lifeSprite1.rect.center = ((772, 155))
            lifeSprite2.rect.center = ((722, 155))
            lifeSprite3.rect.center = ((672, 155))

        if lives.lives == 2:
            lifeSprite1.rect.center = ((772, 155))
            lifeSprite2.rect.center = ((722, 155))
            lifeSprite3.rect.center = ((900, 155))
        if lives.lives == 1:
            lifeSprite1.rect.center = ((772, 155))
            lifeSprite2.rect.center = ((900, 155))
            lifeSprite3.rect.center = ((900, 155))
        if lives.lives == 0:
            lifeSprite1.rect.center = ((900, 155))
            lifeSprite2.rect.center = ((900, 155))
            lifeSprite3.rect.center = ((900, 155))


        """COLLISION CONTROL"""
        #PLAYER

        #with Maze
        if pygame.sprite.spritecollide (player, mazegroup, False):
            for item in mazegroup:
                if item.rect.colliderect(player.rect):
                    player.handle_collision(item)
        #with crumbs
        if pygame.sprite.spritecollide (player, crumbGroup, True):
            score.score +=10
        #with potions
        if pygame.sprite.spritecollide (player, potionGroup, True):
            score.score +=30
            for dragon in dragonSprites:
                dragon.killState = True
        #with DRAGONS
        #if dragons aren't killable
        if dragon0.killState == False:
            if pygame.sprite.spritecollide (player, dragonSprites, False):
                lives.lives -=1
                player.rect.center = (levelMaze.playerStart())
        #if dragons are killable
        if dragon0.killState == True:
            for dragon in dragonSprites:
                if dragon.rect.colliderect(player.rect):
                    score.score +=100
                    dragon.invisible(mazegroup)

            if pygame.sprite.spritecollide (dragon0, mazegroup, False):
                collisionCount +=1
                if collisionCount == 8:
                    for dragon in dragonSprites:
                        dragon.killState = False
                        collisionCount = 0


        # WALLS WITH
        for item in mazegroup:
            #with DRAGONS
            if item.rect.colliderect (dragon0.rect):
                dragon0.handle_collision(item)
            if item.rect.colliderect (dragon1.rect):
                dragon1.handle_collision(item)
            if item.rect.colliderect (dragon2.rect):
                dragon2.handle_collision(item)
            if item.rect.colliderect (dragon3.rect):
                dragon3.handle_collision(item)

            #with treasure
            if item.rect.colliderect (treasure.rect):
                treasure.handle_collision(item)
        #PRINCESS
        if level == 3:
            for item in mazegroup:
                if item.rect.colliderect (princess.rect):
                    princess.handle_collision (item)
            if gemTouch == True:
                if player.rect.colliderect (princess.rect):
                    GameWin.gameOver()
                    return False





        mazegroup.clear(screen, background)
        crumbGroup.clear (screen, background)
        scoreSprite.clear (screen, background)
        potionGroup.clear (screen, background)
        treasureGroup.clear (screen, background)
        dragonSprites.clear (screen, background)
        playerSprite.clear(screen, background)
        lifeAvatars.clear (screen, background)
        textGroup.clear (screen, background)
        if level ==3:
            princessGroup.clear (screen, background)



        mazegroup.update()
        crumbGroup.update()
        scoreSprite.update()
        potionGroup.update()
        treasureGroup.update()
        dragonSprites.update()
        playerSprite.update()
        lifeAvatars.update()
        textGroup.update()
        if level == 3:
            princessGroup.update()


        mazegroup.draw(screen)
        crumbGroup.draw(screen)
        scoreSprite.draw(screen)
        potionGroup.draw (screen)
        treasureGroup.draw(screen)
        dragonSprites.draw(screen)
        playerSprite.draw(screen)
        lifeAvatars.draw (screen)
        textGroup.draw (screen)
        if level == 3:
            princessGroup.draw(screen)





        pygame.display.flip()


    pygame.quit()

