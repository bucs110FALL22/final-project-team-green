import pygame
import random
from src.walls import Walls

class Enemy():
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.image = pygame.image.load("assets/enemy.png")
        self.image = pygame.transform.scale(self.image, (35, 35))

    def generate(self):
        '''
        puts the enemy in a randomly generated position
        args: (self, x, y) self initializes the enemy object, x is the x position on screen, y is the y position on screen
        returns: None
        '''
        self.x= random.randrange(Walls.width)
        self.y= random.randrange(Walls.height)

    def move(self, x, y):
        '''
        enemy moves back and forth within the maze (like in pacman)
        args: (self, x, y) self initializes the enemy object, x is the x position on screen, y is the y position on screen
        returns: None
        '''
        while Walls.insidex != self.x and Walls.insidey != self.y:
          #pos of enemy is not touching a wall of the maze:
           self.x= self.x-10 #or to wherever a wall is
           self.x= self.x+10 #back to starting
   
    def die(self, x, y):
      '''
      if player throws an object at the enemy and theycome into contact, enemy dies
       args: (self, x, y) self initializes the enemy object, x is the x position on screen, y is the y position on screen
       returns : None
      '''
      if self.x in Sprite.x and self.y in Sprite.y:
        self.image= None
          