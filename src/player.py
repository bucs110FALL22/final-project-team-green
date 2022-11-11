import pygame
from sprite import Sprite

class Player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    '''
    initializes the player object
    args: (self, x, y) self used to initialize characteristics of the player, x and y used for positional purposes
    returns: None
    '''
    super().__init__(self)
    self.health = 100
    self.xpos = x
    self.ypos = y
    self.direction = ""
    self.speed = 3 #Num pixels moving
    self.image = pygame.image.load("assets/Student.png")
    self.rect = self.image.get_rect()

  #All movement methods will be used in conjunction with KEYDOWN events, so as long as a user holds, the player moves
  def moveRight(self):
    '''
    allows the player to move in the right direction
    args: (self) self allows the player object's x position be updated
    returns: None
    '''
    self.xpos = self.xpos + self.speed
    self.direction = "Right"

  def moveLeft(self):
    '''
    allows the player to move in the left direction
    args: (self) self allows the player object's x position to be updated
    returns: None
    '''
    self.xpos = self.xpos - self.speed
    self.direction = "Left"

  def moveUp(self):
    '''
    allows the player to move upwards
    args: (self) self allows the player object's y position to be updated
    returns: None
    '''
    self.ypos = self.ypos - self.speed #In pygame, decreasing speed moves the object upwards
    self.direction = "Up"

  def moveDown(self):
    '''
    allows the player to move downwards
    args: (self) self allows the player object's y position to be updated
    returns: None
    '''
    self.ypos = self.ypos + self.speed
    self.direction = "Down"

  def attack(self, choice):
    '''
    creates the sprite object to be used for "attacks"
    args: (self, choice) self allows the "directoin" charactersitic to be used, and choice dtermines the direction the sprite moves in
    returns: None
    '''
    projectile = Sprite(choice, self.x, self.y)
    if(self.direction == "Right"):
      projectile.moveLeftRight(1)
    elif(self.direction == "Left"):
      projectile.moveLeftRight(2)
    elif(self.direction == "Up"):
      projectile.moveUpDown(1)
    elif(self.direction == "Down"):
      projectile.moveUpDown(2)