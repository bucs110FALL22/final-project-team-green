import pygame
import random
from src.sprtie import Player
from src.walls import Walls
from src.graphical import Graphical

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.x= x
        self.y= y
        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect()
        self.speed = random.randrange(1,5)

    def generate(self, x, y):
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
      if enemy and player come into contact, enemy dies
       args: (self, x, y) self initializes the enemy object, x is the x position on screen, y is the y position on screen
       returns : None
      '''
      if self.x in Player.x and self.y in Player.y:
        self.image= None
          