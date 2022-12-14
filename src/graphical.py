import pygame
from src.walls import Walls
from src.keyboard import Keyboard
from src.puzzle import Puzzle
from src.database import Database
from src.esc import EscKey


class Graphical:
  def __init__(self, color):
    self.width = 600
    self.height = 600
    self.window = pygame.display.set_mode((self.width, self.height)) #Blank surface
    self.surface = pygame.display.set_mode((self.width, self.height)) #Maze surface
    self.color = color
    self.mazecolor = (69, 139, 0)
    dungeonsize = 40
    arcadesize = 100
    self.font = pygame.font.Font("assets/dungeon.ttf", dungeonsize)
    self.scorefont = pygame.font.Font("assets/arcade.ttf", arcadesize)
    self.textcolor = "black"

  def makeMenu(self):
    
    #Initialize menu screen + Message
    self.window.fill(self.mazecolor)
    messages = ["Welcome to the maze", "Enter", "Controls", "Scoreboard"]
    starty = 160
    count = 80
    for i in range(len(messages)):
      display_mes = self.font.render(messages[i], True, self.textcolor)
      display_mes_rect = display_mes.get_rect(center = (self.width/2, starty))
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
    keyx = 200
    keyy = 30
    movement_control = Keyboard(keyx, keyy)
    self.window.blit(movement_control.image, (movement_control.x, movement_control.y))
    dungeonsize = 25
    self.font = pygame.font.Font("assets/dungeon.ttf", dungeonsize)
    piecex = 268
    piecey = 310
    piece = Puzzle(piecex, piecey)
    self.window.blit(piece.image, (piece.x, piece.y))
    esckeyx = 240
    esckeyy = 150
    esc_control = EscKey(esckeyx, esckeyy)
    self.window.blit(esc_control.image, (esc_control.x, esc_control.y))
    
    message = "Move up"
    message2 = "Move right"
    message3 = "Move down"
    message4 = "Move left"
    message5 = "Return to previous"

    display_mes = self.font.render(message, True, self.textcolor)
    upx = 237
    upy = 275
    self.window.blit(display_mes, (upx, upy))
    display_mes = self.font.render(message2, True, self.textcolor)
    rightx = 372
    righty = 325
    self.window.blit(display_mes, (rightx, righty))
    display_mes = self.font.render(message3, True, self.textcolor)
    downx = 217
    downy = 375
    self.window.blit(display_mes, (downx, downy))
    display_mes = self.font.render(message4, True, self.textcolor)
    leftx = 72
    lefty = 325
    self.window.blit(display_mes, (leftx, lefty))
    display_mes = self.font.render(message5, True, self.textcolor)
    prevx = 145
    prevy = 425
    self.window.blit(display_mes, (prevx, prevy))


  def makeScoreboard(self):
    self.window.fill(self.mazecolor)
    message = "SCOREBOARD"
    display_mes = self.scorefont.render(message, True, self.textcolor)
    scorey = 100
    display_mes_rect = display_mes.get_rect(center = (self.width/2, scorey))
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

    arcadesize = 40
    self.scorefont = pygame.font.Font("assets/arcade.ttf", arcadesize)
    message = "Rank"
    message2 = "Time"
    rankx = 115
    ranky = 158
    display_mes = self.scorefont.render(message, True, self.textcolor)
    self.window.blit(display_mes, (rankx, ranky))
    timex = 310
    timey = 158
    display_mes = self.scorefont.render(message2, True, self.textcolor)
    self.window.blit(display_mes, (timex, timey))

    numx = 143
    numy = 203
    num = 1
    diff1 = 46
    diff2 = 1
    for i in range(6):
      message = str(num)
      display_mes = self.scorefont.render(message, True, self.textcolor)
      self.window.blit(display_mes, (numx, numy))
      numy += diff1
      num += diff2
    

    highscores = Database()
    bestscores = []
    for key in highscores.db.keys():
      bestscores.append(highscores.db[key])

    bestscores = sorted(bestscores)
    scorex = 230
    scorey = 203
    for i in range(6):
      display_mes = self.scorefont.render(str(bestscores[i]) + " seconds", True, self.textcolor)
      self.window.blit(display_mes, (scorex, scorey))
      scorey += diff1   