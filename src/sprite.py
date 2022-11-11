import pygame

class Sprite(pygame.sprite.Sprite):
  def __init__(self, choice, x, y):
    '''
    intializes the sprite object
    args: (self, choice, x, y) self used to initialize characteristics of the sprite, choice used as a user input to choose which object they want to attack with, x and y used for positional purposes
    returns: None
    '''
    super().__init__(self)
    self.speed = 1
    self.xpos = x
    self.ypos = y
    if(choice == 1):
      self.image = pygame.image.load("assetes/SPRITE1.png")
    elif(choice == 2):
      self.image = pygame.image.load("assets/SPRITE2.png")


  #Movement would start (shooting) when a certain button is pressed, and would continue until hitting an object
  def moveUpDown(self, direction):
    '''
    allows the sprite to move up or down depending on directional paramater
    args: (self, direction) self allows the sprite object to be utilized, direction is assigned depending on if player is facing up/down, correspondingly shoots the sprite in that direction
    returns: (self.ypos) returns the y position of the sprite
    '''
    if(direction == 1): #Shoots up
      self.ypos = self.ypos - self.speed
      return self.ypos
    elif(direction == 2): #Shoots down
      self.ypos = self.ypos + self.speed
      return self.ypos

  def moveLeftRight(self, direction):
    '''
    allows the sprite to move right or left depending on directional paramater
    args: (self, direction) self allows the sprite object to be utilized, direction is assigned depending on if player is facing right/left, correspondingly shoots the sprite in that direction
    returns: (self.xpos) returns the x position of the sprite 
    '''
    if(direction == 1): #Shoots right
      self.xpos = self.xpos + self.speed
      return self.xpos
    elif(direction == 2): #Shoots left
      self.xpos = self.xpos -self.speed
      return self.xpos