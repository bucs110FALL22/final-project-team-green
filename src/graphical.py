import pygame
from src.walls import Walls

class Graphical:
  def __init__(self, color):
    self.window = pygame.display.set_mode((600, 600)) #Blank surface
    self.surface = pygame.display.set_mode((600,600)) #Maze surface
    self.color = color
    self.font = pygame.font.Font(None, 50)

  def makeMenu(self):
    
    #Initialize menu screen + Message
    self.window.fill(self.color)
    message = "Welcome to THE MAZE"
    display_mes = self.font.render(message, True, "white")
    self.window.blit(display_mes, (120, 120))

    #Create boxes (1, 2, 3) with difficulty options
    offset = 175
    outside_color = "white"
    outsidex = 75
    outsidey = 250
    outsidew = 100
    outsideh = 50
    inside_color = "black"
    insidex = 77
    insidey = 252
    insidew = 96
    insideh = 46
    
    for i in range(3):
      outside = Walls(outsidex, outsidey, outsidew, outsideh)
      outside.makeWall(self.window, outside_color)
      inside = Walls(insidex, insidey, insidew, insideh)
      inside.makeWall(self.window, inside_color)
      outsidex += offset
      insidex += offset

    font_change = 117
    level_choice = 1
    for i in range(3):
      message = str(level_choice)
      display_mes = self.font.render(message, True, "white")
      self.window.blit(display_mes, (font_change, 260))
      font_change += 175
      level_choice += 1
    pygame.display.flip()

  def makeMaze(self, level):
    self.window.fill(self.color)
    pygame.display.flip()

    wallcolor = (69, 139, 0)
    outsidex = 100
    outsidey = 100
    outsidew = 404
    outsideh = 404
    perimeter_o = Walls(outsidex, outsidey, outsidew, outsideh)
    perimeter_o.makeWall(self.surface, wallcolor)
    insidex = 102
    insidey = 102
    insidew = 400
    insideh = 400
    perimeter_i = Walls(insidex, insidey, insidew, insideh)
    perimeter_i.makeWall(self.surface, "white")

    #Level 1 Design

    if(level == 1):
      one = Walls(342, 442, 20, 60)
      one.makeWall(self.surface, wallcolor)
      two = Walls(402, 442, 100, 20)
      two.makeWall(self.surface, wallcolor)
      three = Walls(402, 382, 20, 80)
      three.makeWall(self.surface, wallcolor)
      four = Walls(282, 442, 20, 60)
      four.makeWall(self.surface, wallcolor)
      five = Walls(220, 442, 80, 20)
      five.makeWall(self.surface, wallcolor)
      six = Walls(220, 382, 200, 20)
      six.makeWall(self.surface, wallcolor)
      seven = Walls(162, 322, 20, 180)
      seven.makeWall(self.surface, wallcolor)
      eight = Walls(162, 322, 260, 20)
      eight.makeWall(self.surface, wallcolor)
      nine = Walls(462, 262, 20, 200)
      nine.makeWall(self.surface, wallcolor)
      ten = Walls(322, 262, 144, 20)
      ten.makeWall(self.surface, wallcolor)
      eleven = Walls(102, 262, 20, 240)
      eleven.makeWall(self.surface, wallcolor)
      twelve = Walls(102, 262, 180, 20)
      twelve.makeWall(self.surface, wallcolor)
      thirteen = Walls(322, 229, 20, 52)
      thirteen.makeWall(self.surface, wallcolor)
      fourteen = Walls(262, 229, 20, 52)
      fourteen.makeWall(self.surface, wallcolor)
      fifteen = Walls(102, 189, 56, 20)
      fifteen.makeWall(self.surface, wallcolor)
      sixteen = Walls(138, 142, 20, 88)
      sixteen.makeWall(self.surface, wallcolor)
      seventeen = Walls(198, 102, 244, 20)
      seventeen.makeWall(self.surface, wallcolor)
      eighteen = Walls(198, 102, 20, 88)
      eighteen.makeWall(self.surface, wallcolor)
      nineteen = Walls(198, 170, 208, 20)
      nineteen.makeWall(self.surface, wallcolor)
      twenty = Walls(422, 102, 20, 28)
      twenty.makeWall(self.surface, wallcolor)
      twentyone = Walls(482, 102, 20, 88)
      twentyone.makeWall(self.surface, wallcolor)
      twentytwo = Walls(446, 170, 56, 20)
      twentytwo.makeWall(self.surface, wallcolor)

  def drawMaze(self):
    self.window.blit(self.surface, (0,0))