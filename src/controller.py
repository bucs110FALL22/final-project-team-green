import pygame
from src.graphical import Graphical
from src.player import Player

class Controller:
  def __init__(self):
    pygame.init()

  def mainloop(self):
    menu = Graphical("black")
    menu.makeMenu()
    chose_mode = False
    while(chose_mode == False): #Runs until a level is chosen
      search = True #Event loop getting mouse click coordinates
      while(search == True):
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            search = False
      if((x > 75) & (x < 175) & (y > 250) & (y < 300)):
        level = 1
        chose_mode = True

    game_window = Graphical("white")
    game_window.makeMaze(level)
    game_window.drawMaze()

    user = Player(302, 502)
    game_window.window.blit(user.image, (user.x, user.y))
    pygame.display.flip()

    moving = True
    while(moving == True):
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            #Repeated code for functionalitiy purposes
            block = False
            count = 0
            for i in range(len(game_window.xboundaries)):
              if(count % 2 == 1):
                if((user.y <= game_window.yboundaries[i-1]) & (user.y >= game_window.yboundaries[i]) & (user.x >= game_window.xboundaries[i-1]) & (user.x <= game_window.xboundaries[i])):
                  block = True
                  continue
              count += 1
            if(block == False):
              user.moveUp()
            elif(block == True):
              continue
          elif event.key == pygame.K_RIGHT:
            block = False
            count = 0
            for i in range(len(game_window.xboundaries2)):
              if(count % 2 == 1):
                if((user.y <= game_window.yboundaries2[i-1]) & (user.y >= game_window.yboundaries2[i]) & (user.x >= game_window.xboundaries2[i-1]) & (user.x <= game_window.xboundaries2[i])):
                  block = True
                  continue
              count += 1
            if(block == False):
              user.moveRight()
            elif(block == True):
              continue
          elif event.key == pygame.K_DOWN:
            block = False
            count = 0
            for i in range(len(game_window.xboundaries3)):
              if(count % 2 == 1):
                if((user.y <= game_window.yboundaries3[i-1]) & (user.y >= game_window.yboundaries3[i]) & (user.x >= game_window.xboundaries3[i-1]) & (user.x <= game_window.xboundaries3[i])):
                  block = True
                  continue
              count += 1
            if(block == False):
              user.moveDown()
            elif(block == True):
              continue
          elif event.key == pygame.K_LEFT:
            block = False
            count = 0
            for i in range(len(game_window.xboundaries4)):
              if(count % 2 == 1):
                if((user.y <= game_window.yboundaries4[i-1]) & (user.y >= game_window.yboundaries4[i]) & (user.x >= game_window.xboundaries4[i-1]) & (user.x <= game_window.xboundaries4[i])):
                  block = True
                  continue
              count += 1
            if(block == False):
              user.moveLeft()
            elif(block == False):
              continue

          game_window.makeMaze(level)
          game_window.drawMaze()
          game_window.window.blit(user.image, (user.x, user.y))
          pygame.display.flip()