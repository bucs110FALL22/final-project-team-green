import pygame
import random
from src.pencil import Pencil

class Enemy():
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (35, 35))

    def moveSide(self, distance):
      '''
      enemy moves side to side going from it's starting point, then to the right a certain distance, and then moves back to its starting spot
       args: (self, distance) self initializes the enemy object, distance is the distance to the right that the enemy moves
       returns : None
      '''
      while self.x != self.x+distance:
        self.x = self.x+1
      if self.x == self.x+distance:
        while self.x != self.x-distance:
          self.x = self.x-1
         
    def die(self, sprite):
      '''
      if player throws an object at the enemy and theycome into contact, enemy dies
       args: (self, x, y) self initializes the enemy object
       returns : None
      '''
      if sprite.x == self.x and sprite.y == self.y:
        self.image= None
          