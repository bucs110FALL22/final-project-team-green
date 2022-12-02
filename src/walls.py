import pygame

class Walls():
    def __init__(self, x, y, w, h):
        self.x= x
        self.y= y
        self.width= w
        self.height= h
        self.rect= pygame.Rect(self.x, self.y, self.width, self.height)

    def makeWall(self, display, color):
        pygame.draw.rect(display, color, self.rect)
   