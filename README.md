:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# School is a Maze 
## CS 110 Final Project
### Fall, 2022 
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

https://replit.com/join/oiweiazppp-jackhunter9 

<< [link to demo presentation slides](#) >>

### Team: Green 
#### Jack Hunter & Lily Thorne 

***

## Project Description

Navigate your way through a maze as a student as fast as you can and try to avoid or defeat professors blocking your way!

***    

## User Interface Design

- **Initial Concept**
  - << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components. >>
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    *Pygame
      -https://www.pygame.org/
      - Pygame is a module for Python that helps you create games and other multimedia applications

    *
  
* Class Interface Design
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* Classes

1. < Class Player > 
    * __init__
        * < Initializes the player object with characteristics: health xpos ypos direction speed image and rect >
    * moveRight
        * < Allows the player to move in the right direction >
    * moveLeft
        * < Allows the player to move in the left direction >
    * moveUp
        * < Allows the player to move upwards >
    * moveDown
        * < Allows the player to move down >
    * attack
        * < Utilizes the Sprite class to shoot an object in a certain direction   >

2. < Class Sprite >
   * __init__
       * < Initializes the sprite object with characteristics: speed xpos and ypos >
    * moveUpDown
        * < Allows the sprite to move in either the upwards or downwards directions >
    * moveLeftRight
        * < Allows the sprite to move in either the left or right directions >
        
3.  < Class Enemy > 
    * __init__
        * < Initializes the enemy object with characteristics:  xpos ypos speed image and rect >
    * move
        * < Allows the enemy to move back and forth>
    * die
        * < Enemy object leaves the screen if the player comes into contact with it   >

4.  < Class Walls > 
    * __init__
        * < Initializes the Wall object with characteristics:  xpos ypos height width and rect >
    * makeWall
        * < Makes a wall object on the screen>
  

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * controller.py
    * enemy.py
    * graphical.py
    * player.py
    * sprite.py
    * walls.py
* assets
    * class_diagram.jpg
    * enemy.png
    * pencil.png
    * student.png
* etc
    * milestone2.md

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* We would test the program by writing bits of code as testing and debugging as we went

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Navigate to Shell,   |Game window opens to screen that   |
                       |type "python3 main.py"|reads "Welcome to the Maze"        |
                       |and hit enter         |                                   |
|  2                   | click count button   | display changes to count = 1      |

