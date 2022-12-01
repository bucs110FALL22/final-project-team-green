import pygame
from src.walls import Walls

class Graphical:
  def __init__(self, color):
    self.window = pygame.display.set_mode((600, 600)) #Blank surface
    self.surface = pygame.display.set_mode((600,600)) #Maze surface
    self.color = color
    self.mazecolor = (69, 139, 0)
    self.font = pygame.font.Font("assets/dungeon.ttf", 40)

  def makeMenu(self):
    
    #Initialize menu screen + Message
    text_color = "black"
    self.window.fill(self.mazecolor)
    message1 = "Welcome to THE MAZE"
    message2 = "Enter"
    message3 = "Controls"
    message4 = "Scoreboard"

    display_mes = self.font.render(message1, True, text_color)
    self.window.blit(display_mes, (35, 160))
    display_mes = self.font.render(message2, True, text_color)
    self.window.blit(display_mes, (230, 240))
    display_mes = self.font.render(message3, True, text_color)
    self.window.blit(display_mes, (190, 320))
    display_mes = self.font.render(message4, True, text_color)
    self.window.blit(display_mes, (160, 400))
    pygame.display.flip()

  def makeMaze(self, level):
    self.window.fill(self.color)
    pygame.display.flip()

    outsidex = 100
    outsidey = 100
    outsidew = 404
    outsideh = 404
    perimeter_o = Walls(outsidex, outsidey, outsidew, outsideh)
    perimeter_o.makeWall(self.surface, self.mazecolor)
    insidex = 102
    insidey = 102
    insidew = 400
    insideh = 400
    perimeter_i = Walls(insidex, insidey, insidew, insideh)
    perimeter_i.makeWall(self.surface, "white")

    #Level 1 Design

    if(level == 1):
      one = Walls(342, 442, 20, 60)
      one.makeWall(self.surface, self.mazecolor)
      two = Walls(402, 442, 100, 20)
      two.makeWall(self.surface, self.mazecolor)
      three = Walls(402, 382, 20, 80)
      three.makeWall(self.surface, self.mazecolor)
      four = Walls(282, 442, 20, 60)
      four.makeWall(self.surface, self.mazecolor)
      five = Walls(220, 442, 80, 20)
      five.makeWall(self.surface, self.mazecolor)
      six = Walls(220, 382, 200, 20)
      six.makeWall(self.surface, self.mazecolor)
      seven = Walls(162, 322, 20, 180)
      seven.makeWall(self.surface, self.mazecolor)
      eight = Walls(162, 322, 260, 20)
      eight.makeWall(self.surface, self.mazecolor)
      nine = Walls(462, 262, 20, 200)
      nine.makeWall(self.surface, self.mazecolor)
      ten = Walls(322, 262, 144, 20)
      ten.makeWall(self.surface, self.mazecolor)
      eleven = Walls(102, 262, 20, 240)
      eleven.makeWall(self.surface, self.mazecolor)
      twelve = Walls(102, 262, 180, 20)
      twelve.makeWall(self.surface, self.mazecolor)
      thirteen = Walls(322, 229, 20, 52)
      thirteen.makeWall(self.surface, self.mazecolor)
      fourteen = Walls(262, 229, 20, 52)
      fourteen.makeWall(self.surface, self.mazecolor)
      fifteen = Walls(102, 189, 56, 20)
      fifteen.makeWall(self.surface, self.mazecolor)
      sixteen = Walls(138, 142, 20, 88)
      sixteen.makeWall(self.surface, self.mazecolor)
      seventeen = Walls(198, 102, 244, 20)
      seventeen.makeWall(self.surface, self.mazecolor)
      eighteen = Walls(198, 102, 20, 88)
      eighteen.makeWall(self.surface, self.mazecolor)
      nineteen = Walls(198, 170, 208, 20)
      nineteen.makeWall(self.surface, self.mazecolor)
      twenty = Walls(422, 102, 20, 28)
      twenty.makeWall(self.surface, self.mazecolor)
      twentyone = Walls(482, 102, 20, 88)
      twentyone.makeWall(self.surface, self.mazecolor)
      twentytwo = Walls(446, 170, 56, 20)
      twentytwo.makeWall(self.surface, self.mazecolor)

      #Establishing hitbox values

      #For UP arrow key (get rid of magic values)
      self.xboundaries = [147, 416, 189, 416, 189, 267, 371, 502, 291, 466, 102, 278, 165, 402, 413, 502, 105, 154, 67, 123, 196, 406]
      self.yboundaries = [342, 322, 402, 382, 462, 442, 462, 442, 282, 262, 282, 262, 190, 170, 190, 170,222, 202, 209, 189, 122, 102]

      #For RIGHT arrow keys (get rid of magic values)
      self.xboundaries2 = [307, 327, 367, 387, 185, 205, 247, 267, 185, 205, 427, 447, 287, 307, 227, 247, 103, 123, 103, 123, 163, 183, 411, 431, 447, 467]
      self.yboundaries2 = [600, 407, 460, 382, 460, 407, 502, 438, 400, 347, 458, 262, 281, 196, 281, 196, 220, 174, 174, 107, 188, 102, 188, 135, 102, 190]

    #For DOWN arrow keys (get rid of magic values)
    self.xboundaries3 = [307, 358, 187, 298, 187, 418, 127, 418, 402, 439, 322, 502, 98, 270, 229, 278, 289, 338, 98, 138, 106, 154, 208, 402, 414, 482]
    self.yboundaries3 = [427, 405, 427, 405, 357, 345, 305, 285, 427, 405, 252, 225, 252, 225, 219, 192, 219, 192, 189, 154, 138, 105, 170, 133, 170, 133]

    #For LEFT arrow keys (get rid of magic values)
    self.xboundaries4 = [282, 300, 351, 359, 172, 180, 414, 420, 414, 420, 116, 120, 276, 280, 336, 340, 152, 156, 212, 216, 400, 404, 436, 440]
    self.yboundaries4 = [600, 407, 502, 407, 502, 322, 442, 348, 340, 288, 502, 262, 281, 195, 261, 195, 220, 108, 170, 122, 188, 136, 128, 102]
      

  def drawMaze(self):
    self.window.blit(self.surface, (0,0))