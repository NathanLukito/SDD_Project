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

Functions:
- loadBuildings(): Loads and scales building piece images.
- draw_exit_button(): Draws the exit button on the screen.
- drawBuildings(screen, board): Draws building pieces on the game board.
- loadBackground(): Loads and scales the background image.
- loadTitle(): Loads the title image and calculates its position.
- drawBoard(selectedSquare): Draws the game board, highlighting the selected square.
- drawMenu(): Draws the main menu with buttons for starting a new game, loading a game, checking high scores, and exiting.
- new_game(load=False): Manages the game loop for starting a new game or loading a saved game.
- show_score(): Placeholder function for displaying high scores.
- main(): The main function that initializes the Pygame environment and manages the main game loop.

Usage:
- Run the script to start the Ngee Ann City game.
- Use the mouse to interact with the menu and game board.
- Click on the exit button to quit the game.
- Able to interact with the main menu of the board

