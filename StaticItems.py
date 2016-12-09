__author__ = 'Patricia'
import pygame, random, MovingObjects

class MazeWall(pygame.sprite.Sprite):
    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        wallChoice = random.randint(1,9)
        rotationChoice = random.randint (1,4)
        flipChoice = random.randint (1,4)
        if wallChoice == 1:
            self.image = pygame.image.load ("wall1.png")
        if wallChoice == 2:
            self.image = pygame.image.load ("wall2.png")
        if wallChoice ==3:
            self.image = pygame.image.load ("wall3.png")
        if wallChoice ==4:
            self.image = pygame.image.load ("vWall1.png")
        if wallChoice ==5:
            self.image = pygame.image.load ("vWall2.png")
        if wallChoice ==6:
            self.image = pygame.image.load ("vWall3.png")
        if wallChoice ==7:
            self.image = pygame.image.load ("vWall4.png")
        if wallChoice == 8:
            self.image = pygame.image.load ("wall4.png")
        if wallChoice == 9:
            self.image = pygame.image.load ("wall5.png")

        if rotationChoice ==1:
            self.image = pygame.transform.rotate (self.image, 90)
        if rotationChoice ==2:
            self.image = pygame.transform.rotate (self.image, 180)
        if rotationChoice == 3:
            self.image = pygame.transform.rotate (self.image, 270)

        if flipChoice ==1:
            self.image = pygame.transform.flip (self.image, True, True)
        if flipChoice == 2:
            self.image = pygame.transform.flip (self.image, True, False)
        if flipChoice ==3:
            self.image = pygame.transform.flip (self.image, False, True)

        self.rect = self.image.get_rect()


        self.rect.center = center


    def update (self):
        pass





class Breadcrumb(pygame.sprite.Sprite):
    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        choice = random.randint (1,3)
        rotationchoice = random.randint (1,4)
        flipchoice = random.randint (1,4)
        if choice==1:
            self.image = pygame.image.load ("breadcrumb.png")
        if choice ==2:
            self.image = pygame.image.load ("breadcrumb3.png")
        if choice == 3:
            self.image = pygame.image.load ("breadcrumb2.png")
        self.rect = self.image.get_rect()

        if rotationchoice ==1:
            self.image = pygame.transform.rotate (self.image, 90)
        if rotationchoice ==2:
            self.image = pygame.transform.rotate (self.image, 180)
        if rotationchoice ==3:
            self.image = pygame.transform.rotate (self.image, 270)

        if flipchoice == 1:
            self.image = pygame.transform.flip (self.image, True, True)
        if flipchoice ==2:
            self.image = pygame.transform.flip (self.image, True, False)
        if flipchoice ==3:
            self.image = pygame.transform.flip (self.image, False, True)



        self.rect.center = center




    def update (self):
        pass


class Potion (pygame.sprite.Sprite):
    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("potion.png")
        self.rect = self.image.get_rect()

        self.rect.center = center




    def update (self):
        pass

class LifeAvatar (pygame.sprite.Sprite):
    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("playerLeft.png")
        self.rect = self.image.get_rect()

        self.rect.center = center

    def update (self):
        self.rect.center = self.rect.center


class Text2 (pygame.sprite.Sprite):
    def __init__ (self, screen, lvl):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.font = pygame.font.Font ("8bitlim.ttf", 25)
        if lvl ==1:
            self.text = "Level One"
        if lvl ==2:
            self.text = "Level Two"
        if lvl ==3:
            self.text = "Level Three"
        self.image = self.font.render (self.text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = ((400,375))

    def update (self):

        self.rect.y = self.rect.y
        self.rect.x = self.rect.x


class Blackout (pygame.sprite.Sprite):
    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((800,600))
        self.image.fill ((32, 32, 78))
        self.rect = self.image.get_rect()




        self.rect.center = center



    def update (self):
        pass

class Blackout2 (pygame.sprite.Sprite):
    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("titleBG.png")
        self.rect = self.image.get_rect()




        self.rect.center = center
    def update(self):
        pass


class dragonBG (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("dragonScroll.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = self.rect.center

class dragonTxt (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("dragonTxt.png")
        self.rect = self.image.get_rect()
    def update (self):
        pass