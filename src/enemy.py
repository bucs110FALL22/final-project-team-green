import pygame
import random
import Player from player
import Walls from walls

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.x= x
        self.y= y
        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect()
        self.speed = Random.randrange(1,5)

    def generate(self, x, y):
        '''puts the enemy in a randomly generated position'''
        self.x= Random.randrange(Walls.width)
        self.y= Random.randrange(Walls.height)

    def move(self, x, y):
        '''enemy moves back and forth within the maze (like pacman)'''
        while #pos of enemy is not touching a wall of the maze:
           self.x= self.x-10 #or to wherever a wall is
           self.x= self.x+10 #back to starting
   
    def die(self, x, y):
       '''if enemy and player come into contact, enemy dies, might belong better in the player class so could be changed later'''
        if enemy.x=player.x and enemy.y=player.y:
          self.image= None