import pygame
from src.graphical import Graphical
from src.player import Player
from src.enemy import Enemy

class Controller:
  def __init__(self):
    pygame.init()

  def mainloop(self):
    menu = Graphical("black")
    menu.makeMenu()
    chose_mode = False
    while(chose_mode == False): #Runs until a level is chosen
      search = True #getting mouse click coordinates
      while(search == True):
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            search = False
      if((x > 230) & (x < 385) & (y > 250) & (y < 285)):
        level = 1
        chose_mode = True

    #Initializing scene
    game_window = Graphical("white")
    game_window.makeMaze(level)
    game_window.drawMaze()
    
    #Add barriers for enemies 
    enemy1 = Enemy(185, 405)
    game_window.window.blit(enemy1.image, (enemy1.x, enemy1.y))
    enemy2 = Enemy(125, 285)
    game_window.window.blit(enemy2.image, (enemy2.x, enemy2.y))
    enemy3 = Enemy(286, 190)
    game_window.window.blit(enemy3.image, (enemy3.x, enemy3.y))
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

          #Redrawing scene
          game_window.makeMaze(level)
          game_window.drawMaze()
          game_window.window.blit(user.image, (user.x, user.y))
          game_window.window.blit(enemy1.image, (enemy1.x, enemy1.y))
          game_window.window.blit(enemy2.image, (enemy2.x, enemy2.y))
          game_window.window.blit(enemy3.image, (enemy3.x, enemy3.y))
          pygame.display.flip()