import pygame

class Player():
  def __init__(self, x, y):
    '''
    initializes the player object
    args: (self, x, y) self used to initialize characteristics of the player, x and y used for positional purposes
    returns: None
    '''
    self.x = x
    self.y = y
    self.speed = 2
    self.image = pygame.image.load("assets/student.png")
    self.image = pygame.transform.scale(self.image, (35, 35))

  #All movement methods will be used in conjunction with KEYDOWN events, so as long as a user holds, the player moves
  def moveRight(self):
    '''
    allows the player to move in the right direction
    args: (self) self allows the player object's x position be updated
    returns: None
    '''
    self.x = self.x + self.speed

  def moveLeft(self):
    '''
    allows the player to move in the left direction
    args: (self) self allows the player object's x position to be updated
    returns: None
    '''
    self.x = self.x - self.speed

  def moveUp(self):
    '''
    allows the player to move upwards
    args: (self) self allows the player object's y position to be updated
    returns: None
    '''
    self.y = self.y - self.speed

  def moveDown(self):
    '''
    allows the player to move downwards
    args: (self) self allows the player object's y position to be updated
    returns: None
    '''
    self.y = self.y + self.speed
