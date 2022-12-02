import pygame

class Pencil():
  def __init__(self, x, y):
    '''
    intializes the sprite object
    args: (self, choice, x, y) self used to initialize characteristics of the sprite, choice used as a user input to choose which object they want to attack with, x and y used for positional purposes
    returns: None
    '''
    self.speed = 5
    self.x = x
    self.y = y
    self.image = pygame.image.load("assets/pencil.png")
    self.image = pygame.transform.scale(self.image, (35, 35))

  
  def updateDirection(self, direction):
    if(direction == "Up"):
      self.image = pygame.transform.rotate(self.image, -90)
    elif(direction == "Right"):
      self.image = pygame.transform.rotate(self.image, -180)
    elif(direction == "Down"):
      self.image = pygame.transform.rotate(self.image, -270)
  
  
  def updatePos(self, direction):
    if(direction == "Up"):
      self.y -= self.speed
    elif(direction == "Right"):
      self.x += self.speed
    elif(direction == "Down"):
      self.y += self.speed
    elif(direction == "Left"):
      self.x -= self.speed