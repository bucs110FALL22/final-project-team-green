import pygame
from src.walls import Walls
from src.keyboard import Keyboard
from src.puzzle import Puzzle


class Graphical:
  def __init__(self, color):
    self.window = pygame.display.set_mode((600, 600)) #Blank surface
    self.surface = pygame.display.set_mode((600,600)) #Maze surface
    self.color = color
    self.mazecolor = (69, 139, 0)
    self.font = pygame.font.Font("assets/dungeon.ttf", 40)
    self.scorefont = pygame.font.Font("assets/arcade.ttf", 100)
    self.textcolor = "black"

  def makeMenu(self):
    
    #Initialize menu screen + Message
    self.window.fill(self.mazecolor)
    messages = ["Welcome to the maze", "Enter", "Controls", "Scoreboard"]
    starty = 160
    count = 80
    for i in range(len(messages)):
      display_mes = self.font.render(messages[i], True, self.textcolor)
      display_mes_rect = display_mes.get_rect(center = (300, starty))
      self.window.blit(display_mes, display_mes_rect)
      starty += count
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
      sixteen = Walls(138, 142, 20, 80)
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
    self.window.fill(self.mazecolor)
    movement_control = Keyboard(200, 70)
    self.window.blit(movement_control.image, (movement_control.x, movement_control.y))
    self.font = pygame.font.Font("assets/dungeon.ttf", 25)
    piece = Puzzle(275, 310)
    self.window.blit(piece.image, (piece.x, piece.y))
    
    message = "Move up"
    message2 = "Move right"
    message3 = "Move down"
    message4 = "Move left"

    display_mes = self.font.render(message, True, self.textcolor)
    self.window.blit(display_mes, (240, 275))
    display_mes = self.font.render(message2, True, self.textcolor)
    self.window.blit(display_mes, (375, 325))
    display_mes = self.font.render(message3, True, self.textcolor)
    self.window.blit(display_mes, (220, 375))
    display_mes = self.font.render(message4, True, self.textcolor)
    self.window.blit(display_mes, (75, 325))

  def makeScoreboard(self):
    self.window.fill(self.mazecolor)
    message = "SCOREBOARD"
    display_mes = self.scorefont.render(message, True, self.textcolor)
    display_mes_rect = display_mes.get_rect(center = (600/2, 100))
    self.window.blit(display_mes, display_mes_rect)
    outside = Walls(100, 150, 400, 326)
    outside.makeWall(self.window, self.textcolor)
    inside = Walls(104, 154, 392, 318)
    inside.makeWall(self.window, self.mazecolor)
    
    smallchartx = 100
    smallcharty = 150
    smallchartw = 100
    smallcharth = 50
    num_boxes = 7

    largechartx = 196
    largecharty = 150
    largechartw = 304
    largecharth = 50
    
    rect_one = Walls(100, 150, 100, 50)
    rect_one.makeWall(self.window, self.textcolor)
    rect_two = Walls(104, 154, 92, 42)
    rect_two.makeWall(self.window, self.mazecolor)
    rect1 = Walls(100, 196, 100, 50)
    rect1.makeWall(self.window, self.textcolor)
    rect2 = Walls(104, 200, 92, 42)
    rect2.makeWall(self.window, self.mazecolor)
    

    for i in range(num_boxes):
      rect_one = Walls(smallchartx, smallcharty, smallchartw, smallcharth)
      rect_one.makeWall(self.window, self.textcolor)
      rect_two = Walls(smallchartx+4, smallcharty+4, smallchartw-8, smallcharth-8)
      rect_two.makeWall(self.window, self.mazecolor)
      smallcharty += (smallcharth-4)
      rect_three = Walls(largechartx, largecharty, largechartw, largecharth)
      rect_three.makeWall(self.window, self.textcolor)
      rect_four = Walls(largechartx+4, largecharty+4, largechartw-8, largecharth-8)
      rect_four.makeWall(self.window, self.mazecolor)
      largecharty += (largecharth-4)
      