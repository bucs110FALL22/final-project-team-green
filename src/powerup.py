import pygame
import random

class Powerup():
  def __init__(self):
    self.obj = random.randrange(1,4)
    if(self.obj == 1):
      self.image = pygame.image.load("assets/backpack.png")
      self.image = pygame.transform.scale(self.image, (30, 30))
    elif(self.obj == 2):
      self.image = pygame.image.load("assets/calculator.png")
      self.image = pygame.transform.scale(self.image, (30, 30))
    elif(self.obj == 3):
      self.image = pygame.image.load("assets/apple.png")
      self.image = pygame.transform.scale(self.image, (30, 30))

  def getCoords(self, window):
    possible = False
    while(possible == False):
      self.rect = self.image.get_rect()
      self.rect.x = random.randrange(102, 472)
      self.rect.y = random.randrange(102, 472)
      self.x = self.rect.x
      self.y = self.rect.y
      for i in range(len(window.wallList)):
        spot = self.rect.colliderect(window.wallList[i])
        if(spot == True):
          continue
        else:
          possible  = True

  def getObj(self, window):
    window.window.blit(self.image, (self.rect.x, self.rect.y))
