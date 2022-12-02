import pygame
from src.walls import Walls
from src.keyboard import Keyboard


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
      entrance = Walls(302, 502, 40, 40)
      entrance.makeWall(self.surface, self.color)
      exit = Walls(442, 86, 40, 40)
      exit.makeWall(self.surface, self.color)

      #Establishing hitbox values

      self.wallList = [one.rect, two.rect, three.rect, four.rect, five.rect, six.rect, seven.rect, eight.rect, nine.rect, ten.rect, eleven.rect, twelve.rect, thirteen.rect, fourteen.rect, fifteen.rect, sixteen.rect, seventeen.rect, eighteen.rect, nineteen.rect, twenty.rect, twentyone.rect, twentytwo.rect]


  def drawMaze(self):
    self.window.blit(self.surface, (0,0))

  def makeControls(self):
    self.window.fill("white")
    movement_control = Keyboard(100, 100)
    self.window.blit(movement_control, (movement_control.x, movement_control.y))