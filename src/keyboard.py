import pygame

class Keyboard():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("assets/keyboard.png")
    self.image = pygame.transform.scale(self.image, (35, 35))