import pygame
from src.graphical import Graphical
from src.player import Player
from src.enemy import Enemy
from src.pencil import Pencil

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
        #Initializing scene
        level = 1
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

        last_direction = "Up"
        attack = False
        moving = True
        while(moving == True):
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              block, location = user.detectWall(game_window, last_direction)       
              if event.key == pygame.K_UP:
                last_direction = "Up"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_RIGHT:
                last_direction = "Right"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_DOWN:
                last_direction = "Down"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_LEFT:
                last_direction = "Left"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_SPACE:
                sprite = Pencil(user.x, user.y)
                sprite.updateDirection(last_direction)
                attack = True

              #Redrawing scene
              game_window.makeMaze(level)
              game_window.drawMaze()
              game_window.window.blit(user.image, (user.x, user.y))
              game_window.window.blit(enemy1.image, (enemy1.x, enemy1.y))
              game_window.window.blit(enemy2.image, (enemy2.x, enemy2.y))
              game_window.window.blit(enemy3.image, (enemy3.x, enemy3.y))
              while(attack == True):
                sprite.updatePos(last_direction)
                game_window.window.blit(sprite.image, (sprite.x, sprite.y))
            
              pygame.display.flip()

      if((x > 190) & (x < 420) & (y > 330) & (y < 365)):
        controls_window = Graphical("white")
        controls_window.makeControls()
        pygame.display.flip()