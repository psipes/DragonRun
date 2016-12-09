__author__ = 'Patricia'
import pygame, StaticItems
pygame.init()

class Score (pygame.sprite.Sprite):
    def __init__ (self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.score = 0
        self.font = pygame.font.Font ("8bitlim.ttf", 35)
    def update (self):
        self.text = "SCORE %d" %(self.score)
        self.image = self.font.render (self.text, 1, (255,255,0))
        self.rect = self.image.get_rect()
        self.rect.y = 140
        self.rect.x = 10



class Lives:
        lives = 3



class LifePics:
    def display (sprite1, sprite2, sprite3, sprite4, lives):
        if lives.lives ==3:
            sprite1.rect.center = ((772, 155))
            sprite2.rect.center = ((722, 155))
            sprite3.rect.center = ((672, 155))
            sprite4.rect.center = ((900, 155))






