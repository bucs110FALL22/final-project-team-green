import pygame

class Puzzle():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = pygame.image.load("assets/puzzle.png")
    self.image = pygame.transform.scale(self.image, (60,60))