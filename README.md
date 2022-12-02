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
    * 
        * ![class diagram](assets/class_diagram.jpg) 
* Classes

1. < Class Player > 
    * __init__
        * < Initializes the player object with characteristics: xpos ypos >
    * moveRight
        * < Allows the player to move in the right direction >
    * moveLeft
        * < Allows the player to move in the left direction >
    * moveUp
        * < Allows the player to move upwards >
    * moveDown
        * < Allows the player to move down >
    * detectWall
        * < Checks to see if the Player object collided with a Wall object >
    * movement
        * < Allows the player object to move based on keys >

2. < Class Controller >
   * __init__
       * < Initializes the Controller object>
    * mainloop
        * < Runs the game >

   
        
3.  < Class Powerup > 
    * __init__
        * < Initializes the powerup object >
    * getCoords
        * < Checks the coordinates of the powerup object compared to Walls>
    * getObj
        * < Puts the powerup object on the window   >

4.  < Class Walls > 
    * __init__
        * < Initializes the Wall object with characteristics:  xpos ypos height and width>
    * makeWall
        * < Makes a wall object on the screen>

5. < Class Graphical > 
    * __init__
        * < Initializes the graphical object with characteristic: color >
    * makeMenu
        * <generates the menu screen>
    * makeMaze
        * <creates the maze using Walls>
    * drawMaze
        * <creates the maze on the window>
     * backToMenu
        * <if user presses return key, the game returns to the menu screen>
        
6.  < Class Keyboard > 
    * __init__
        * < Initializes the Keyboard object with characteristics:  xpos ypos >

7. < Class Database >
   * __init__
       * < Initializes the database object >
    * addData
        * < saves data into the repl database >
        
8. < Class puzzle >
   * __init__
        * < Initializes the Puzzle object with characteristics:  xpos ypos >
   

       
## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * controller.py
    * database.py
    * graphical.py
    * keyboard.py
    * player.py
    * powerup.py
    * puzzle.py
    * walls.py
* assets
    * class_diagram.jpg
    * apple.png
    * backpack.png
    * calculator.png
    * pencil.png
    * student.png
    * keyboard.png
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
|                      |type "python3 main.py"|reads "Welcome to the Maze",       |
|                      |and hit enter         |"Enter", "Control", and "Scoreboard"|
|  2                   | click "Control"      | displays control screen with      |  |                      |                      | directions on what keys to press  |  |                      |                      | to move the player                |
|  3                   |press return key on   |window returns to menu screen      |
|                      |  keybord             |                                   |
|  4                   |click "Scoreboard"    |displays scoreboard screen with    |
|                      |                      |  score rankings                   |
|  5                   |press return key on   |window returns to menu screen      |
|                      |  keybord             |                                   |  
|  6                   |click "Enter"         |displays maze screen and user can  |
|                      |                      |  begin playing                    |
|  7                   |press up arrow key    |player moves up 2px                |
|                      | on keyboard          |                                   |
|  8                   |press down arrow key  |player moves down 2 px             |
|                      |   on keyboard        |                                   |
|  9                   |press left arrow key  |player moves left 2 px             |
|                      |   on keyboard        |                                   |
|  10                  |press right arrow key |player moves right 2 px            |
|                      |   on keyboard        |                                   |
|  11                  |using arrow keys,     |when player reaches a powerup, the |
|                      |navigate player to a  |powerup disappears and player gains|
|                      |powerup in the maze   | 5 points                          |
|                      |(backpack, calculator,|                                   |
|                      | or apple)            |                                   |
|  12                  |player is navigated   |scoreboard screen is shown with    |
|                      |to the end of the maze|time ranks and users score is      |
|                      |                      | displayed under the scoreboard.   |
|                      |                      | if user makes it onto the         |
|                      |                      | scoreboard, their score will      |
|                      |                      | appear there as well              |