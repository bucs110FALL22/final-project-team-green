import pygame

class EscKey():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("assets/esc.png")
    self.image = pygame.transform.scale(self.image, (120, 120))