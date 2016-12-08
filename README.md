# Sweepster
A minesweeper game created as a final project for GISC 3200 Python Class

###Abstract 
Sweepster was created with the idea of involving a player in an interactive game of Minesweeper through python code. By using a game loop with a coordinate calling system similar to the one used for the game Battleship the game was able to be created. The game exists with great bones to build off of to one day create a more improved interface. 

###What is Minesweeper? 
Minesweeper is a single player videogame with the objective of clearing all spaces of a board without selecting or denoting any bombs/mines. traditionally the game is more sucessful when clues about the number of remaining mines given after each selection. The game utalizes both chance and strategy based off of probabilty and origionated from the 1960. Information about the game was gathered from the game's [Wikipedia page](https://en.wikipedia.org/wiki/Minesweeper_(video_game)). 

###How does Sweepster Work? 
Sweepster works in a way developed after much trial and error. Essentially it runs off of two seperate parts: A game loop and utils page.

####Utils page
the utils page is the utility where all the functions are run and kept in order to keep the game loop more easily managable. 
- The most fundamentally important part of Sweepster is creating a playing board, without it, there would be no point in playing the the game. The functions used for creating the function were:
  * board - which creates a playing board while adjusting the board size as the input
  * flatten - creates a viewer friendly minesweeper
  * show_board - prints the board in the game interface
- The next step in creating Sweepster is to add the bombs here are those functions:
  * bomb - uses the imported random feature to place 10 bombs randomnly on the board
  * bomb_check - checks the choice input with the board to search for bombs
- Since this is a player based game there needs to be functions that check the validity of a point in the game board, here are those functions:
  * check_format - ensures the choice follows the proper '(x,y)' format. It insures that guesses are within the proper parentesis and the are seperated with a comma as well as it strips a space if one is placed in the guess. 
  * extract_coors - seperates the input numbers into a coordinate tuple
  * check_within - takes the coordinates of the guess and the board size as inputs and checks to see if the guess falls within the board
- the final functions run how the board is modified after every guess made by the player:
  * show_bomb - shows how bombs appear in the board within the board once the game has ended
  * show_marked - takes away the '?' symbol in guessed spaces, leaving them blank
  * show_game_over - shows all information about the game board once a bomb has been denoted. 

####Game Loop
The game loop utalizes the utils page remotly while it runs a loop for the game to be played. Here is where the size of the board can be changed as well. As far as how the came loop works, The game is set up to where alive = True and as long as that still applies the user can still submit coordinates to the game in order to keep playing. 
The loop will continue to run even if guesses aren't in the correct formatting and the player continues to guess coordinates that do not contain a bomb. A break to quit the game was installed for when there could potentially be an issue that will not end the game. That break command is ':wq'. 
If a bomb is found, alive = False and the game loop is ended. 


### What Next? 
Sweepster is currently running off of a very basic interactive game model. The game runs great at it's current state however it leads its self to many diffent updates and improvements. Sweepster at its current state cannot be won. It can be played until a bomb is selected and the game is over. If I were to improve this game I would have a way to mark the bombs and once every bomb was marked and every space on the board is cleared then the player wins the game! Additionally I would work on cleaning up the board and improving the playing experiance.
