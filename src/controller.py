import pygame
import time

from src.graphical import Graphical
from src.player import Player
from src.database import Database
from src.powerup import Powerup

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
        user = Player(302, 502) #Set to 302, 502 for final
        item = Powerup()
        item.getCoords(game_window)
        item.getObj(game_window)
        item2 = Powerup()
        item2.getCoords(game_window)
        item2.getObj(game_window)
        item3 = Powerup()
        item3.getCoords(game_window)
        item3.getObj(game_window)
        items = [item.rect, item2.rect, item3.rect]
        game_window.window.blit(user.image, (user.x, user.y))
        pygame.display.flip()
        last_direction = "Up"
        #attack = False

        total_points = 0
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
                  difference = difference - user.points
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
                  print(total_points)
                  break
                user.detectItem(game_window, items)      
                last_direction = "Up"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_RIGHT:
                if(user.x >= 467):
                  continue
                user.detectItem(game_window, items)
                last_direction = "Right"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_DOWN:
                if((user.y >= 467) & ((user.x <= 300) or (user.x >= 310))):
                  continue
                user.detectItem(game_window, items)
                last_direction = "Down"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_LEFT:
                if(user.x <= 102):
                  continue
                user.detectItem(game_window, items)
                last_direction = "Left"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_ESCAPE:
                self.mainloop()
                pygame.display.flip()
                
              #Redrawing scene
              game_window.makeMaze(level)
              game_window.drawMaze()
              game_window.window.blit(user.image, (user.x, user.y))  
              item.getObj(game_window)
              item2.getObj(game_window)
              item3.getObj(game_window)
              pygame.display.flip()


      elif((x > 185) & (x < 415) & (y > 305) & (y < 340)):
        controls_window = Graphical("white")
        controls_window.makeControls()
        pygame.display.flip()
        in_screen = True
        while(in_screen == True):
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                in_screen = False
                self.mainloop()
                pygame.display.flip()
      

      elif((x > 150) & (x < 450) & (y > 385) & (y < 420)):
        score_window = Graphical("white")
        score_window.makeScoreboard()
        pygame.display.flip()
        in_screen = True
        while(in_screen == True):
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPaE:
                in_screen = False
                self.mainloop()
                pygame.display.flip()