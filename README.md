# SDD_Project
A turn based game where players place down buildings by consuming coins and gain points every turn based on the buildings they have

This program implements a simple City Building game using the Pygame library. The game features a graphical user interface with a 20x20 board, buttons for starting a new game, loading a saved game, checking high scores, and exiting the game.

Modules:
- pygame: Pygame is a set of Python modules designed for writing video games. It provides functionalities for handling events, drawing graphics, and managing the game loop.

Variables:
- grids (int): The number of rows and columns on the game board.
- white, black, select (tuple): RGB color values for white, black, and the selected square.
- images (dict): A dictionary to store and manage building piece images.
- board (list): A 2D list representing the initial state of the game board.
- sqSize (int): The size of each square on the game board.
- offset_x, offset_y (int): Offsets for centering the game board on the screen.
- exit_game_rect (pygame.Rect): Rectangle representing the exit button.
- exit_game_color (tuple): RGB color value for the exit button.
- exit_game_text (pygame.Surface): Rendered text for the exit button.

Classes:
- Building: A building class that contains the building type, cost, and its coordinates on the board.
- Player: A player class that conatins the name of the player, the number of coins the player has and their score.

Functions:

loadBuildings():
Purpose: Loads building images and stores them in the images dictionary.
Parameters: None.
Return: None.

draw_exit_button():
Purpose: Draws and displays the exit button in the main game.
Parameters: None.
Return: None.

showCoins():
Purpose: Draws and displays the number of coins in the main game.
Parameters: None.
Return: None.

showBuildings():
Purpose: Loads, draws, and displays the available buildings on the left side of the main game screen.
Parameters: None.
Return: Rectangles representing the positions of the loaded buildings.

drawBuildings(screen, board):
Purpose: Draws the buildings on the 20x20 grid of the main game.
Parameters:
screen: Pygame screen surface.
board: 2D list representing the current state of the game board.
Return: None.

loadBackground():
Purpose: Loads and scales the background image of the main menu.
Parameters: None.
Return: Loaded background image.

loadTitle():
Purpose: Loads the main menu screen title image.
Parameters: None.
Return: Loaded title image and its rectangle.

drawBoard(selectedSquare):
Purpose: Draws the main game board and elements.
Parameters:
selectedSquare: Tuple representing the selected square on the grid.
Return: Rectangles representing the positions of the buildings on the left side of the main game screen.

drawMenu():
Purpose: Draws the main menu items and buttons.
Parameters: None.
Return: Rectangles representing the positions of the menu buttons.

calculatePoints():
Purpose: Calculates points and updates the global points and coins based on the current state of the game board.
Parameters: None.
Return: None.

initialRandomBuilding():
Purpose: Displays the initial random building options on the main game screen for the first turn.
Parameters: None.
Return: None.

new_game(load=False):
Purpose: Main game logic, handles user input, building placement, and turns.
Parameters:
load: Boolean indicating whether to load a saved game.
Return: None.

checkGameFinish():
Purpose: Checks if the game is finished based on the number of coins and filled squares on the board.
Parameters: None.
Return: Boolean indicating whether the game is finished.

showEndScreen(score):
Purpose: Displays the end screen with the final score and leaderboard status.
Parameters:
score: Player's final score.
Return: None.

get_user_input():
Purpose: Prompts the user to input the position for building placement.
Parameters: None.
Return: String representing the user input position.

Save_Game():
Purpose: Saves the current game state to a Python file.
Parameters: None.
Return: None.

show_score():
Purpose: Displays the leaderboard scores.
Parameters: None.
Return: Leaderboard scores.

main():
Purpose: Main function to run the entire program, handling main menu interactions.
Parameters: None.
Return: None.

Usage:
- Run the script to start the Ngee Ann City game.
- Use the mouse to interact with the menu and game board.
- Click on the exit button to quit the game.
- Able to interact with the main menu of the board

