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
            user.moveUp()
          elif event.key == pygame.K_RIGHT:
            user.moveRight()
          elif event.key == pygame.K_DOWN:
            user.moveDown()
          elif event.key == pygame.K_LEFT:
            user.moveLeft()

          game_window.makeMaze(level)
          game_window.drawMaze()
          game_window.window.blit(user.image, (user.x, user.y))
          pygame.display.flip()