milestone 2 template
======================================================================

# Final Project Milestone II

*Place this document in your final project repo folder `/etc`. *

***

Come up with interfaces for 3 possible classes you think you may need for your project. Again, brainstorm a little. Nothing is *wrong*.

## Class Interface 1

class Player:
  def __init__ (self, name, major, age):
    self.name= name
    self.major= major
    self.age= age
    self.year= "freshman"
    self.classes= []
  

## Class Interface 2

class Professor:
  def __init__(self, name, subject, x, y)
    self.name = name
    self.subject = subject
    self.xpos = x
    self.ypos = y 
    self.dialogue = ""
    
  def moveRight(self, distance):
    self.xpos = x+distance

  def moveLeft(self, distance):
    self.xpos = x-distance

  def moveUp(self, distance):
    self.ypos = y+distance

  def moveDown(self, distance:
    self.ypos = y-distance
  
  def interact(interaction):
    if(interaction == 1):
      self.dialogue = "Scenario 1" 
    elif(interaction == 2):
      self.dialogue = "Scenario 2"
    elif(interaction == 3):
      self.dialogue = "Scenario 3"

#Scenario text is just a placeholder at the moment, have not decided on what scenarios would actually be yet
#Would also be a system in place that would prevent the scenario variable from being anything other than 1 < Scenario < 3
  
## Class Interface 3

class Projector:
  def __init__(self, color, x, y, h, w):
    self.color = color
    self.xpos = x
    self.ypos = y
    self.height = h
    self.width = w
    self.image = ""

  def getText(self, message, x, y):
    self.text = Text(message, x, y) 
#Would be a different class containing a method that turns a string into printable font on screen (Not made yet)

  def updateSlide(self, slide_num):
    self.image = slide_num 
#Str pathway to different potential images that could be displayed on screen
    