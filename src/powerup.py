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

    

  def getObj(self, window, x, y):
    self.x = x
    self.y = y
    window.window.blit(self.image, (self.x, self.y))
