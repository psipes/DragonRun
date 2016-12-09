__author__ = 'Patricia'
import pygame, random, MazeDraw
from threading import Timer



class Player(pygame.sprite.Sprite):
    """This is the player Avatar"""
    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("player.png")
        self.rect = self.image.get_rect()

        self.rect.center = center
        self.dx = 0
        self.dy = 0
        self.x = self.rect.centerx
        self.y = self.rect.centery

        self.collCount = 0

        """This is used to control directional sprite"""
        self.left = False
        self.right = True
        self.up = False
        self.down = False






    def update (self):
        """update controls the call to the directional avatar"""
        if self.left == True:
            self.image = pygame.image.load ("playerLeft.png")

        if self.left == False:
            self.image = pygame.image.load ("playerRight.png")



    def handle_keys(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_DOWN]:
            self.rect.y +=5

        elif key[pygame.K_UP]:
            self.rect.y -=5
            self.right = False
            self.left = False
            self.up = True
            self.down = False

        elif key[pygame.K_RIGHT]:
            self.rect.x +=5
            self.right = True
            self.left = False
            self.up = False
            self.down = False

        elif key[pygame.K_LEFT]:
            self.rect.x -=5
            self.right = False
            self.left = True
            self.up = False
            self.down = False

    def handle_collision(self, item):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:
            self.rect.bottom =item.rect.top

        elif key[pygame.K_UP]:
            self.rect.top = item.rect.bottom

        elif key[pygame.K_RIGHT]:
            self.rect.right = item.rect.left

        elif key[pygame.K_LEFT]:
            self.rect.left = item.rect.right




class Dragon(pygame.sprite.Sprite):
    """This is the enemy sprite"""
    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        self.colorSet = 0
        self.image = pygame.image.load ("dragonGr.png")
        self.rect = self.image.get_rect()
        self.rect.center = center

        """This assigns random start velocity to dragon"""
        a = random.randint (1,4)
        if a==1:
            self.dx = 0
            self.dy = 3
        if a == 2:
            self.dx = 0
            self.dy = -3
        if a == 3:
            self.dx = 3
            self.dy = 0
        if a == 4:
            self.dx = -3
            self.dy = 0

        self.x = self.rect.centerx
        self.y = self.rect.centery
        self.killState = False


    def update (self):
        """assigns colorset"""

        if self.colorSet == 0:
            self.image = pygame.image.load ("dragonGr.png")
        if self.colorSet == 1:
            self.image = pygame.image.load ("dragonPi.png")
        if self.colorSet == 2:
            self.image = pygame.image.load ("dragonBl.png")
        if self.colorSet == 3:
            self.image = pygame.image.load ("dragonRe.png")

        self.rect.centerx += self.dx
        self.rect.centery += self.dy

        if self.killState == True:
            self.image = pygame.image.load ("dragonKillable.png")

        if self.dx == -3:
            self.image = pygame.transform.flip (self.image, True, False)



    def invisible (self, group):
        self.rect.center = ((390, 390))
        coolDown = 0

    def stopFull (self):
        self.dx = 0
        self.dy = 0

    def handle_collision(self, item):
        choice = random.randint(1,2)
        if self.dy ==3:
            self.rect.bottom = item.rect.top-2
            self.dy = 0
            if choice ==1:
                self.dx += 3
            if choice ==2:
                self.dx -= 3


        elif self.dy == -3:
            self.rect.top = item.rect.bottom +2
            self.dy = 0
            if choice ==1:
                self.dx += 3
            if choice == 2:
                self.dx -=3

        elif self.dx == 3:
            self.rect.right = item.rect.left -2
            self.dx =0
            if choice == 1:
                self.dy +=3
            if choice == 2:
                self.dy -=3

        elif self.dx == -3:
            self.rect.left = item.rect.right + 2
            self.dx = 0
            if choice ==1:
                self.dy -=3
            if choice ==2:
                self.dy +=3








class Treasure(pygame.sprite.Sprite):
    """this is set invisible to begin with, becomes visible through level"""
    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("invisible.png")
        self.rect = self.image.get_rect()

        self.dx = 0
        self.dy = 5


        self.rect.center = center


        self.x = self.rect.centerx
        self.y = self.rect.centery



    def update (self):
        #self.rect.center = ((self.rect.centerx, self.rect.centery))
        self.image = self.image
        self.rect.centerx += self.dx
        self.rect.centery += self.dy



    def invisible (self, group):
        self.rect.center = ((390, 390))
        coolDown = 0

    def stopFull (self):
        self.dx = 0
        self.dy = 0


    def handle_collision(self, item):
        choice = random.randint(1,2)
        if self.dy ==5:
            self.rect.bottom = item.rect.top-2
            self.dy = 0
            if choice ==1:
                self.dx += 5
            if choice ==2:
                self.dx -= 5


        elif self.dy == -5:
            self.rect.top = item.rect.bottom +2
            self.dy = 0
            if choice ==1:
                self.dx += 5
            if choice == 2:
                self.dx -= 5

        elif self.dx == 5:
            self.rect.right = item.rect.left -2
            self.dx =0
            if choice == 1:
                self.dy +=5
            if choice == 2:
                self.dy -=5

        elif self.dx == -5:
            self.rect.left = item.rect.right + 2
            self.dx = 0
            if choice ==1:
                self.dy -=5
            if choice ==2:
                self.dy +=5


class Princess (pygame.sprite.Sprite):
    """this is set invisible to begin with, becomes visible through level"""
    def __init__ (self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("princess.png")
        self.rect = self.image.get_rect()

        self.dx = 0
        self.dy = 8


        self.rect.center = center


        self.x = self.rect.centerx
        self.y = self.rect.centery



    def update (self):
        #self.rect.center = ((self.rect.centerx, self.rect.centery))
        self.image = self.image
        self.rect.centerx += self.dx
        self.rect.centery += self.dy



    def invisible (self, group):
        self.rect.center = ((390, 390))
        coolDown = 0

    def stopFull (self):
        self.dx = 0
        self.dy = 0


    def handle_collision(self, item):
        choice = random.randint(1,2)
        if self.dy ==8:
            self.rect.bottom = item.rect.top-2
            self.dy = 0
            if choice ==1:
                self.dx += 8
            if choice ==2:
                self.dx -= 8


        elif self.dy == -8:
            self.rect.top = item.rect.bottom +2
            self.dy = 0
            if choice ==1:
                self.dx += 8
            if choice == 2:
                self.dx -= 8

        elif self.dx == 8:
            self.rect.right = item.rect.left -2
            self.dx =0
            if choice == 1:
                self.dy +=8
            if choice == 2:
                self.dy -=8

        elif self.dx == -8:
            self.rect.left = item.rect.right + 2
            self.dx = 0
            if choice ==1:
                self.dy -=8
            if choice ==2:
                self.dy +=8



class RunText (pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load ("runTxt.png")
        self.rect = self.image.get_rect()
        self.dx = 20
        self.stopCount = False

    def update (self):
        self.rect.centerx += self.dx
        if self.stopCount == True:
            if self.rect.centerx >415:
                self.dx = 0
                self.rect.centerx = 400
        else:
            if self.rect.left >800:
                self.rect.right = 0
                self.stopCount = True







        """t = Timer (3.0, self.canKill)
        t.start()"""















    """def killable (self):
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
        self.image.fill((100,0,0))
        print "HI!"
        return self.last

    def killUpdate (self, last):
        now = pygame.time.get_ticks()
        if now - last >=self.cooldown:
            last = now
            print "OFF"
            self.image.fill ((32, 32, 78))


    def moveAround (self, openSpaces):
        print "Is this working?"

        for element in openSpaces:
            if self.rect.center == element:
                print "yes"
            #print ((element[0]+20, element[1]))
            xCoor=[x for x,_ in element][0]
            yCoor = [x for _,x in element]
            print xCoor
    """






