# SDD_Project
A turn based game where players place down buildings by consuming coins and gain points every turn based on the buildings they have

This program implements a simple City Building game using the Pygame library. The game features a graphical user interface with a 20x20 board, buttons for starting a new game, loading a saved game, checking high scores, and exiting the game.

Modules:
- pygame: Pygame is a set of Python modules designed for writing video games. It provides functionalities for handling events, drawing graphics, and managing the game loop.
- os: The os module provides a way to interact with the operating system. It allows Python programs to perform various operating system-related tasks, such as reading or writing to the file system, manipulating paths, and interacting with the environment variables.
- sys : The sys module provides access to some variables used or maintained by the Python interpreter and functions that interact with the interpreter. It's commonly used for system-specific parameters and functions, including command-line arguments, input and output, and program termination.
- time : The time module provides various time-related functions. It allows you to work with time values, measure time intervals, and format time. Commonly used functions include time(), which returns the current time in seconds since the epoch, and sleep(), which suspends execution for a specified number of seconds.
- threading : The threading module provides a way to create and manage threads in Python. Threads are lightweight processes that run concurrently within a program. The threading module simplifies the creation and synchronization of threads, allowing for parallel execution of tasks.
- random : The random module provides functions for generating pseudorandom numbers. It is commonly used in scenarios where a random element is needed, such as shuffling a sequence, generating random integers, or simulating random events.
- playsound : The playsound module is not a standard Python module. It appears to be a third-party module for playing sound files. This module allows you to play sound files directly from Python scripts without using a more complex audio library. The playsound module simplifies sound playback for simple use cases.

Global Variables:
- grids (int): The number of rows and columns on the game board.
- white, black, select (tuple): RGB color values for white, black, and the selected square.
- images (dict): A dictionary to store and manage building piece images.
- board (list): A 2D list representing the initial state of the game board.
- sqSize (int): The size of each square on the game board.
- offset_x, offset_y (int): Offsets for centering the game board on the screen.
- exit_game_rect (pygame.Rect): Rectangle representing the exit button.
- exit_game_color (tuple): RGB color value for the exit button.
- exit_game_text (pygame.Surface): Rendered text for the exit button.


Functions:

1. loopSound Function
Purpose: Placeholder for playing background sound in a loop.
Details: This function is currently empty and doesn't perform any actions. It seems intended for continuous playback of background music or sound effects during the game.
2. SaveGameButton Class
Purpose: Represents a save game button on the main game screen.
Details:
Attributes:
rect: Rectangle defining the button's position and size.
image: Scaled image of the button.
clicked: Boolean indicating whether the button has been clicked.
Methods:
draw(surface): Draws the button on the given surface and returns True if the button is clicked.
3. loadBuildings Function
Purpose: Loads building images into the images dictionary.
Details: Iterates through the list of building names and loads corresponding images from the 'buildings' directory, scaling them to the desired size.
4. draw_exit_button Function
Purpose: Draws the exit button on the main game screen.
Details: Draws a red rectangle labeled "Exit" on the screen, allowing users to exit the game.
5. showCoins Function
Purpose: Displays the current number of coins on the main game screen.
Details: Renders and displays the number of coins on the screen.
6. drawText Function
Purpose: Draws text on the screen with specified font, color, and position.
Details: Renders text using the provided font, color, and position information, displaying it on the screen.
7. showBuildings Function
Purpose: Displays building options on the main game screen.
Details: Renders and displays images and names of different building types, creating a visual reference for the player.
8. drawBuildings Function
Purpose: Draws buildings on the main game screen based on the board configuration.
Details: Iterates through the game board and draws building images on the screen according to their positions.
9. loadBackground Function
Purpose: Loads and resizes the background image for the main menu screen.
Details: Loads a background image from the 'background' directory, scaling it to match the screen dimensions.
10. loadTitle Function
Purpose: Loads and positions the title image for the main menu screen.
Details: Loads a title image from the 'background' directory and positions it at the top center of the screen.
11. drawBoard Function
Purpose: Draws the game board on the main game screen.
Details: Fills the screen with alternating color tiles to represent the game board and calls drawBuildings to render buildings on the board.
12. drawMenu Function
Purpose: Draws the main menu screen with buttons and background.
Details: Positions and draws buttons and a background image on the main menu screen.
13. calculatePoints Function
Purpose: Calculates points and coins based on the current state of the game board.
Details: Analyzes the configuration of buildings on the board to determine the player's score and earned coins for the current turn.
14. RandomBuilding Function
Purpose: Displays randomly selected building options for the player to choose from.
Details: Renders and displays images and names of two randomly selected buildings, allowing the player to choose one for placement.
Main Game Logic Overview
Loading: Checks whether loading of a saved game is required.
Drawing: Renders and displays various game elements, including the main menu, buildings, coins, and buttons.
Mouse Interaction: Detects mouse clicks for selecting squares, placing buildings, and interacting with buttons (exit and save).
Turn Calculation: Calculates points and coins after every successful building placement, not within the main game loop.
15. new_game Function
Purpose: Initiates a new game or loads a saved game.
Parameters:
load (Boolean): If True, loads a saved game; if False, starts a new game.
Variables:
selectedSquare: Holds the selected grid square for building placement.
coins: Represents the currency available for building placement.
turns: Tracks the number of turns in the game.
board: Represents the game board with building configurations.
margin_size: Sets the margin size for button inflation during mouse click feedback.
16. checkGameFinish Function
Purpose: Checks if the game has finished (either the board is filled or the player runs out of coins).
Returns: True if the game has finished, False otherwise.
17. display_error_message Function
Purpose: Displays an error message on the screen and clears it after a delay.
Parameters:
message: The error message to display.
screen: The Pygame screen object.
18. showEndScreen Function
Purpose: Displays the end game screen with the player's score and prompts for name entry.
Parameters:
score: The player's final score.
19. Save_Game Function
Purpose: Saves the current game state.
Parameters:
gameboard: The current game board.
20. get_user_input Function
Purpose: Displays an input prompt for the user to specify building placement.
Returns: User input if valid, None otherwise.
21. checkBuildingPosition Function
Purpose: Checks if the proposed building position meets orthogonally adjacent requirements.
Parameters:
position: The user-inputted building position.
i: Index representing the selected building from the random options.
Returns: True if the position is valid, False otherwise.
22. loadScoreBackground Function
Purpose: Loads the background image for the end game and high score screens.
Returns: The Pygame surface containing the background image.
23. show_score Function
Purpose: Displays the high scores on the screen.
Note: Handles the display of the leaderboard and supports exiting the screen.
24. main Function
Purpose: Main game loop to handle button clicks in the main menu.
Note: Calls drawMenu to display buttons and waits for user interaction to initiate a new game, load a saved game, view high scores, or exit the game.
25. Threading for Background Music
Purpose: Initiates a separate thread (loopThread) for playing background music in a loop during the game.
Note: Uses the loopSound function, which is currently a placeholder.
Main Code Execution
Note: Calls main() to start the game loop and handle user interactions in the main menu.
Overall
Game Flow: The code manages the game flow, user interactions, saving/loading game states, and displaying relevant screens (main menu, end game, high scores).
Error Handling: Includes error handling for file operations and invalid user inputs.
Modular Design: Functions are structured to handle specific aspects, enhancing code readability and maintainability.
Pygame: Utilizes the Pygame library for GUI and game-related functionalities.

Usage:
- Run the script to start the Ngee Ann City game.
- Use the mouse to interact with the menu and game board.
- Click on the exit button to quit the game.
- Able to interact with the main menu of the board

