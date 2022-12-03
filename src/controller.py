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


      scorebound1 = 150
      scorebound2 = 450
      scorebound3 = 385
      scorebound4 = 420
      controlbound1 = 185
      controlbound2 = 415
      controlbound3 = 305
      controlbound4 = 340
      menubound1 = 225
      menubound2 = 375
      menubound3 = 225
      menubound4 = 260
      rightborder = 467
      leftborder = 102
      startleft = 300
      startright = 310
      if((x > menubound1) & (x < menubound2) & (y > menubound3) & (y < menubound4)):
        #Initializing scene
        level = 1
        game_window = Graphical("white")
        game_window.makeMaze(level)
        game_window.drawMaze()
        start_time = time.time()
        start_xpos = 302
        start_ypos = 502
        end_xpos = 102
        end_ypos = 442
        user = Player(start_xpos, start_ypos) #Set to 302, 502 for final
        item = Powerup()
        itemx = 160
        itemy = 190
        item.getObj(game_window, itemx, itemy)
        item2 = Powerup()
        item2x = 410
        item2y = 465
        item2.getObj(game_window, item2x, item2y)
        item3 = Powerup()
        item3x = 200
        item3y = 285
        item3.getObj(game_window, item3x, item3y)
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
                if((user.y <= end_xpos) & (user.x <= end_ypos)):
                  continue
                elif((user.y <= end_xpos) & (user.x >= end_ypos)):
                  #Bring up scoreboard, add victory message
                  moving = False
                  wait_time = 3000
                  pygame.time.wait(wait_time)
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
                  scoresize = 40
                  game_window.scorefont = pygame.font.Font("assets/arcade.ttf", scoresize)
                  victory = game_window.scorefont.render("Your time is: " + str(difference) + " seconds", True, game_window.textcolor)
                  scoreposx = 82
                  scoreposy = 485
                  game_window.window.blit(victory, (scoreposx, scoreposy))
                  pygame.display.flip()
                  print(total_points)
                  break
                user.detectItem(game_window, items)      
                last_direction = "Up"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_RIGHT:
                if(user.x >= rightborder):
                  continue
                user.detectItem(game_window, items)
                last_direction = "Right"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_DOWN:
                if((user.y >= rightborder) & ((user.x <= startleft) or (user.x >= startright))):
                  continue
                user.detectItem(game_window, items)
                last_direction = "Down"
                user.movement(block, location, last_direction)
              elif event.key == pygame.K_LEFT:
                if(user.x <= leftborder):
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


      elif((x > controlbound1) & (x < controlbound2) & (y > controlbound3) & (y < controlbound4)):
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
      

      elif((x > scorebound1) & (x < scorebound2) & (y > scorebound3) & (y < scorebound4)):
        score_window = Graphical("white")
        score_window.makeScoreboard()
        pygame.display.flip()
        in_screen = True
        while(in_screen == True):
          for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_ESCAPE:
                in_screen = False
                self.mainloop()
                pygame.display.flip()