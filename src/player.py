pimport pygame

class Player():
  def __init__(self, x, y):
    '''
    initializes the player object
    args: (self, x, y) self used to initialize characteristics of the player, x and y used for positional purposes
    returns: None
    '''
    self.x = x
    self.y = y
    self.speed = 2
    self.image = pygame.image.load("assets/student.png")
    self.image = pygame.transform.scale(self.image, (35, 35))
    self.rect = self.image.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y
    self.points = 0

  #All movement methods will be used in conjunction with KEYDOWN events, so as long as a user pressesp, the player moves
  def moveRight(self):
    '''
    allows the player to move in the right direction
    args: (self) self allows the player object's x position be updated
    returns: None
    '''
    self.x += self.speed
    self.rect.x += self.speed

  def moveLeft(self):
    '''
    allows the player to move in the left direction
    args: (self) self allows the player object's x position to be updated
    returns: None
    '''
    self.x -= self.speed
    self.rect.x -= self.speed

  def moveUp(self):
    '''
    allows the player to move upwards
    args: (self) self allows the player object's y position to be updated
    returns: None
    '''
    self.y -= self.speed
    self.rect.y -= self.speed

  def moveDown(self):
    '''
    allows the player to move downwards
    args: (self) self allows the player object's y position to be updated
    returns: None
    '''
    self.y += self.speed
    self.rect.y -= self.speed

  def detectWall(self, window, direction):
    self.rect.x = self.x
    self.rect.y = self.y
    for i in range(len(window.wallList)):
      collide = self.rect.colliderect(window.wallList[i])
      if(collide == True):
        break
    return collide, direction

  def movement(self, block, location, direction):
    if(block == True):
      if(direction == location):
        pass
      else:
        if(direction == "Up"):
          self.moveUp()
        elif(direction == "Right"):
          self.moveRight()
        elif(direction == "Down"):
          self.moveDown()
        elif(direction == "Left"):
          self.moveLeft()
    else:
      if(direction == "Up"):
        self.moveUp()
      elif(direction == "Right"):
        self.moveRight()
      elif(direction == "Down"):
        self.moveDown()
      elif(direction == "Left"):
        self.moveLeft()

  def detectItem(self, window, items):
    for i in range(len(items)):
      hit_item = self.rect.colliderect(items[i])
      if(hit_item == True):
        cover = pygame.Rect(items[i].x, items[i].y, 30, 30)
        items[i].x = -40
        items[i].y = -40
        self.points += 5
        