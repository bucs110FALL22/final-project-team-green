import pygame
import time

from src.graphical import Graphical
from src.player import Player
from src.enemy import Enemy
from src.database import Database
from src.pencil import Pencil

class Controller:
  def __init__(self):
    pygame.init()

  def mainloop(self):
    highscores = Database()
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
      if((x > 225) & (x < 375) & (y > 225) & (y < 260)):
        #Initializing scene
        level = 1
        game_window = Graphical("white")
        game_window.makeMaze(level)
        game_window.drawMaze()
        start_time = time.time()
    
        #Add barriers for enemies 
        enemy1 = Enemy(185, 405)
        game_window.window.blit(enemy1.image, (enemy1.x, enemy1.y))
        enemy2 = Enemy(125, 285)
        game_window.window.blit(enemy2.image, (enemy2.x, enemy2.y))
        enemy3 = Enemy(286, 190)
        game_window.window.blit(enemy3.image, (enemy3.x, enemy3.y))
        user = Player(302, 502) #Set to 302, 502 for final
        game_window.window.blit(user.image, (user.x, user.y))
        pygame.display.flip()

        last_direction = "Up"
        #attack = False
        moving = True
        while(moving == True):
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              block, location = user.detectWall(game_window, last_direction)       
              if event.key == pygame.K_UP:
                if((user.y <= 102) & (user.x <= 442)):
                  continue
                elif((user.y <= 102) & (user.x >= 442)):
                  #Bring up scoreboard, add victory message
                  moving = False
                  pygame.time.wait(3000)
                  end_time = time.time()
                  difference = end_time-start_time
                  difference = round(difference, 4)
                  keylist = []
                  for key in highscores.db.keys():
                    keylist.append(key)
                  iters = len(keylist)
                  greatest = keylist[0]
                  for i in range(0, iters):
                    if(int(keylist[i]) > (int(greatest))):
                      greatest = keylist[i]

                  greatest = int(greatest)
                  highscores.addData((str(greatest+1)), difference)
                  game_window.makeScoreboard()

                  game_window.scorefont = pygame.font.Font("assets/arcade.ttf", 40)
                  victory = game_window.scorefont.render("Your time is: " + str(difference) + " seconds", True, game_window.textcolor)
                  game_window.window.blit(victory, (82, 485))
                  pygame.display.flip()
                  break
                last_direction = "Up"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_RIGHT:
                if(user.x >= 467):
                  continue
                last_direction = "Right"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_DOWN:
                if((user.y >= 467) & ((user.x <= 300) or (user.x >= 310))):
                  continue
                last_direction = "Down"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_LEFT:
                if(user.x <= 102):
                  continue
                last_direction = "Left"
                user.movement(block, location, last_direction)
              #elif event.key == pygame.K_SPACE:
                #sprite = Pencil(user.x, user.y)
                #sprite.updateDirection(last_direction)
                #attack = True

              #Redrawing scene
              game_window.makeMaze(level)
              game_window.drawMaze()
              game_window.window.blit(user.image, (user.x, user.y))
              game_window.window.blit(enemy1.image, (enemy1.x, enemy1.y))
              game_window.window.blit(enemy2.image, (enemy2.x, enemy2.y))
              game_window.window.blit(enemy3.image, (enemy3.x, enemy3.y))
              #while(attack == True):
                #sprite.updatePos(last_direction)
                #game_window.window.blit(sprite.image, (sprite.x, sprite.y))
            
              pygame.display.flip()

      elif((x > 185) & (x < 415) & (y > 305) & (y < 340)):
        controls_window = Graphical("white")
        controls_window.makeControls()
        pygame.display.flip()

      elif((x > 150) & (x < 450) & (y > 385) & (y < 420)):
        score_window = Graphical("white")
        score_window.makeScoreboard()
        pygame.display.flip()