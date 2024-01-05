# importing of necessary python libraries needed
try:
    from pip._internal import main as pip
    pip(['install', '--user', 'playsound==1.2.2'])
    pip(['install', '--user', 'pygame==2.5.2'])
    pip(['install', '--user', 'random'])
    pip(['install', '--user', 'time'])
    pip(['install', '--user','threading'])
    from playsound import playsound
    import pygame
    import random
except:
    pass
from importlib import reload
import os
import sys
import time
import threading
#initiating of simple constant game variables

def loopSound():
   # while True:
    #    playsound('background.wav', block=True)
    pass

grids = 20 
white = (255, 255, 255)
black = (0, 0, 0)
select = (255, 0, 0)
coins = 16
points = 0
turns = 0
images = {}
buildings = ["R","I","C","O","Ro"]
building_names = {
    "R": "Residential",
    "I": "Industrial",
    "C": "Commercial",
    "O": "Park",
    "Ro": "Road"
}
alphabet = "abcdefghijklmnopqrstuvwxyz"
board = []
pygame.init()


class SaveGameButton:
    def __init__(self, x_percent, y_percent, image, scale):
        width = image.get_width()
        height = image.get_height()

        # Calculate the x and y coordinates based on percentages
        self.rect = pygame.Rect(0, 0, int(width * scale), int(height * scale))
        self.rect.topright = (
            int((pygame.display.Info().current_w * x_percent / 100) - self.rect.width),
            int((pygame.display.Info().current_h * y_percent / 100)),
        )

        # Scale the image
        self.image = pygame.transform.scale(image, self.rect.size)
        self.clicked = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, self.rect.topleft)

        return action
    
save_game_btn_img = pygame.image.load('buttons/save.png')
save_game_btn = SaveGameButton(75, 10, save_game_btn_img, 0.15)

def loadBuildings():
    for i in buildings:
        images[i] = pygame.transform.scale(pygame.image.load('buildings/' + i + '.png'),(sqSize,sqSize))

# initiating the meanu menu buttons and screen dimensions with background
start_button = pygame.image.load("buttons/start_button.png")
load_button = pygame.image.load("buttons/load_button.png")
high_scores_button = pygame.image.load("buttons/high_scores_button.png")
exit_button = pygame.image.load("buttons/exit_button.png")

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_width(), screen.get_height()
sqSize = min(width, height) // (grids +1)

offset_x = (width - grids * sqSize) // 2
offset_y = (height - grids * sqSize) // 2

exit_game_rect = pygame.Rect(10, 10, 100, 50)
exit_game_color = (255, 0, 0)
exit_game_text = pygame.font.Font(None, 36).render("Exit", True, white)

# drawing and displaying of the exit button in the main game
def draw_exit_button():
    pygame.draw.rect(screen, exit_game_color, exit_game_rect)
    screen.blit(exit_game_text, (exit_game_rect.centerx - exit_game_text.get_width() // 2, exit_game_rect.centery - exit_game_text.get_height() // 2))

def showCoins():
    font = pygame.font.Font(None, 20)

    coins_text = "Coins:%d" % coins
    turn_text = "Turn: %d" % turns
    score_text = "Score: %d" % points

    coins_surface = font.render(coins_text, True, (255, 255, 255))
    turn_surface = font.render(turn_text, True, (255, 255, 255))
    score_surface = font.render(score_text, True, (255, 255, 255))

    # Adjust the Y-coordinate for each line to create a stacked effect
    y_offset = 40
    screen.blit(coins_surface, (exit_game_rect.centerx - coins_surface.get_width(), (exit_game_rect.centery - coins_surface.get_height() // 2) + y_offset))
    y_offset += 30  # Increase Y-offset for the next line
    screen.blit(turn_surface, (exit_game_rect.centerx - turn_surface.get_width(), (exit_game_rect.centery - turn_surface.get_height() // 2) + y_offset))
    y_offset += 30  # Increase Y-offset for the next line
    screen.blit(score_surface, (exit_game_rect.centerx - score_surface.get_width(), (exit_game_rect.centery - score_surface.get_height() // 2) + y_offset))

def drawText(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

# loading drawing and displaying the buildings that are available on the left side of the screen of the main game
def showBuildings():

    #residential
    font = pygame.font.Font(None,36)
    residential_building = pygame.image.load("buildings/R.png").convert_alpha()
    residential_building = pygame.transform.scale(residential_building, (60, 60))
    residential_rect = residential_building.get_rect()
    residential_rect.topleft = (20,150)
    pygame.draw.rect(screen, (255,255,255), residential_rect)
    screen.blit(residential_building, residential_rect)
    residential_text = "Residential"
    residential_text_surface = font.render(residential_text, True, (255,255,255))
    screen.blit(residential_text_surface, (10,215))

    #industrial
    industry_building = pygame.image.load("buildings/I.png")
    industry_building = pygame.transform.scale(industry_building, (60, 60))
    industry_rect = industry_building.get_rect()
    industry_rect.topleft = (20,170+residential_rect.top-40)
    pygame.draw.rect(screen, (255,255,255), industry_rect)
    screen.blit(industry_building, industry_rect)
    industry_text = "Industrial"
    industry_text_surface = font.render(industry_text, True, (255,255,255))
    screen.blit(industry_text_surface, (10,industry_rect.top+65))

    #commercial
    commercial_building = pygame.image.load("buildings/C.png")
    commercial_building = pygame.transform.scale(commercial_building, (60, 60))
    commercial_rect = commercial_building.get_rect()
    commercial_rect.topleft = (20,190+residential_rect.top*2-40)
    pygame.draw.rect(screen, (255,255,255), commercial_rect)
    screen.blit(commercial_building, commercial_rect)
    commercial_text = "Commercial"
    commercial_text_surface = font.render(commercial_text, True, (255,255,255))
    screen.blit(commercial_text_surface, (10,commercial_rect.top+65))

    #park
    park_building = pygame.image.load("buildings/O.png")
    park_building = pygame.transform.scale(park_building, (60, 60))
    park_rect = park_building.get_rect()
    park_rect.topleft = (20,210+residential_rect.top*3-40)
    pygame.draw.rect(screen, (255,255,255), park_rect)
    screen.blit(park_building, park_rect)
    park_text = "Park"
    park_text_surface = font.render(park_text, True, (255,255,255))
    screen.blit(park_text_surface, (10,park_rect.top+65))

    #road (not a building)
    road_building = pygame.image.load("buildings/Ro.png")
    road_building = pygame.transform.scale(road_building, (60, 60))
    road_rect = road_building.get_rect()
    road_rect.topleft = (20,230+residential_rect.top*4-40)
    pygame.draw.rect(screen, (255,255,255), road_rect)
    screen.blit(road_building, road_rect)
    road_text = "Road"
    road_text_surface = font.render(road_text, True, (255,255,255))
    screen.blit(road_text_surface, (10,road_rect.top+65))

    return residential_rect,industry_rect,commercial_rect,park_rect,road_rect

# drawing the buildings into the 20x20 grid of the game after every turn 
def drawBuildings(screen, board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            building = board[row][col]
            if building != '--':
                x = offset_x + col * sqSize
                y = offset_y + row * sqSize
                screen.blit(images[building], pygame.Rect(x, y, sqSize, sqSize))

# loading and drawing of the background image of the main menu screen
def loadBackground():
    background_image = pygame.image.load("background/background.jpeg")
    background_image = pygame.transform.scale(background_image, (width, height))
    return background_image

# loading and drawing of the main menu screen title 
def loadTitle():
    title_image = pygame.image.load("background/title.png")
    title_rect = title_image.get_rect(topleft=(screen.get_width()//2 - title_image.get_width() // 2, 50))
    return title_image,title_rect

# add board positions to the board e.g. alphabets and numbers
def draw_board_labels(screen, grids, sqSize, offset_x, offset_y):
    font = pygame.font.SysFont(None, 24) 

    for col in range(grids):
        x = offset_x + col * sqSize + sqSize // 2 - 5
        y = offset_y - 30
        label = font.render(chr(ord('A') + col), True, (255, 255, 255))
        screen.blit(label, (x, y))

    for row in range(grids):
        x = offset_x - 30
        y = offset_y + row * sqSize + sqSize // 2 - 10
        label = font.render(str(row + 1), True, (255, 255, 255))
        screen.blit(label, (x, y))

# draws the board on the screen, adds board labels and any buildings placed
def drawBoard(selectedSquare):
    screen.fill(black)
    colors = [pygame.Color('white'), pygame.Color('gray')]
    for row in range(grids):
        for col in range(grids):
            x = offset_x + col * sqSize
            y = offset_y + row * sqSize
            rect = pygame.Rect(x, y, sqSize, sqSize)
            color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, rect)
    draw_board_labels(screen, grids, sqSize, offset_x, offset_y)
    drawBuildings(screen, board)
    draw_exit_button()
    if save_game_btn.draw(screen):#Liwei
        Save_Game()

    showCoins()
    pygame.display.flip()

    return 

#drawing and placing of the main menu items onto the main menu screen
def drawMenu():
    screen.blit(loadBackground(), (0, 0))
    title_image, title_rect = loadTitle()
    screen.blit(title_image, title_rect)
    total_button_height = (start_button.get_height() + load_button.get_height() + high_scores_button.get_height() + exit_button.get_height())

    padding = 40
    start_y = (screen.get_height() - total_button_height + padding) // 2
    center_x = screen.get_width() // 2

    start_button_rect = start_button.get_rect(topleft=(center_x - start_button.get_width() // 2, start_y))
    load_button_rect = load_button.get_rect(topleft=(center_x - load_button.get_width() // 2, start_y + start_button.get_height() + padding))
    high_scores_button_rect = high_scores_button.get_rect(topleft=(center_x - high_scores_button.get_width() // 2, start_y + start_button.get_height() + load_button.get_height() + padding * 2))
    exit_button_rect = exit_button.get_rect(topleft=(center_x - exit_button.get_width() // 2, start_y + start_button.get_height() + load_button.get_height() + high_scores_button.get_height() + padding * 3))

    screen.blit(start_button, start_button_rect)
    screen.blit(load_button, load_button_rect)
    screen.blit(high_scores_button, high_scores_button_rect)
    screen.blit(exit_button, exit_button_rect)

    pygame.display.flip()
    return start_button_rect,load_button_rect,high_scores_button_rect,exit_button_rect


# Calculates the number of points and coins earned in the current turn
# Loop through each position in the board, if the position is a building
# Check for other buildings around the position referencing the game scope building mechanics
# Ff the buildings are placed in a position to generate points or coins, the turn_points and turn_coins are updated
def calculatePoints():
    turn_points = 0
    turn_coins = 0
    rows = len(board)
    cols = len(board[0])
    #Check if the position is out of the board
    def check_position(i, x):
        return 0 <= i < rows and 0 <= x < cols

    #If the position has the specified building, add points 
    def add_points(i, x, building, points):
        if check_position(i, x) and board[i][x] == building:
            nonlocal turn_points
            turn_points += points
        else:
            pass
    #If the position has the specified building, add coins
    def add_coins(i, x, building, coins):
        if check_position(i, x) and board[i][x] == building:
            nonlocal turn_coins
            turn_coins += coins
        else:
            pass
    
    for i in range(len(board)):
        for x in range(len(board[i])):
            if board[i][x] == 'R':
                add_points(i, x + 1, 'I', 1)
                add_points(i, x - 1, 'I', 1)
                add_points(i + 1, x, 'I', 1)
                add_points(i - 1, x, 'I', 1)
                add_points(i - 1, x - 1, 'I', 1)
                add_points(i - 1, x + 1, 'I', 1)
                add_points(i + 1, x - 1, 'I', 1)
                add_points(i + 1, x + 1, 'I', 1)
                add_points(i, x + 1, 'R', 1)
                add_points(i, x - 1, 'R', 1)
                add_points(i + 1, x, 'R', 1)
                add_points(i - 1, x, 'R', 1)
                add_points(i, x + 1, 'C', 1)
                add_points(i, x - 1, 'C', 1)
                add_points(i + 1, x, 'C', 1)
                add_points(i - 1, x, 'C', 1)
                add_points(i, x + 1, 'O', 2)
                add_points(i, x - 1, 'O', 2)
                add_points(i + 1, x, 'O', 2)
                add_points(i - 1, x, 'O', 2)

            if board[i][x] == 'I':
                turn_points += 1
                add_coins(i, x + 1, 'R', 1)
                add_coins(i, x - 1, 'R', 1)
                add_coins(i + 1, x, 'R', 1)
                add_coins(i - 1, x, 'R', 1)

            if board[i][x] == 'C':
                add_points(i, x + 1, 'C', 1)
                add_points(i, x - 1, 'C', 1)
                add_points(i + 1, x, 'C', 1)
                add_points(i - 1, x, 'C', 1)

                add_coins(i, x + 1, 'R', 1)
                add_coins(i, x - 1, 'R', 1)
                add_coins(i + 1, x, 'R', 1)
                add_coins(i - 1, x, 'R', 1)

            if board[i][x] == 'O':
                add_points(i, x + 1, 'O', 1)
                add_points(i, x - 1, 'O', 1)
                add_points(i + 1, x, 'O', 1)
                add_points(i - 1, x, 'O', 1)

            if board[i][x] == 'Ro':
                for a in range(cols):
                    add_points(i, x + a, 'Ro', 1)
            else:
                pass


    return turn_points, turn_coins

# call upon the building list and remove Road and place onto the main screen to click and place for first turn ONLY
def RandomBuilding(randombuildings = None):

    font = pygame.font.Font(None,36)

    if randombuildings != None:
       random_building_names = randombuildings
    else:
        random_building_names = random.sample(list(images.keys()), 2)
    building1 = pygame.transform.scale(images[random_building_names[0]], (60, 60))
    building2 = pygame.transform.scale(images[random_building_names[1]], (60,60))
    building1_rect = building1.get_rect()
    building2_rect = building2.get_rect()
    building1_rect.topleft = (20, 150)
    pygame.draw.rect(screen, (255,255,255), building1_rect)
    screen.blit(building1, building1_rect)
    building1_name = building_names[random_building_names[0]]
    building1_name_surface = font.render(building1_name, True, (255,255,255))
    screen.blit(building1_name_surface, (10,215))

    building2_rect.topleft = (20, 170 + building1_rect.top - 40)
    pygame.draw.rect(screen, (255,255,255), building2_rect)
    screen.blit(building2, building2_rect)
    building2_name = building_names[random_building_names[1]]
    building2_name_surface = font.render(building2_name, True, (255,255,255))
    screen.blit(building2_name_surface, (10, building2_rect.top + 65))
    pygame.display.flip()
    return building1_rect, building2_rect, random_building_names

# main game logic
# checks whether loading of game is needed if not create a new game
# drawing of main game elements and items 
# detection of mouseclicks and board interaction for selecting squares and for placing of buildings, exit and saving of the game
# turn calculation is every successful building placement not the while loop
def new_game(load = False):
    selectedSquare = None
    global coins
    global turns
    global board
    margin_size = 5
    if load:
        try:
            import save_game
            reload(save_game)
            from save_game import game_details
            board,leaderboard,variables = game_details()
            turns = variables["turn"]
            coins = variables["coins"]
            points = variables["points"]
            print(board)

        except IOError:
            print("No saved game")
            pass
    else:
        board = [['--'] * grids for _ in range(20)]
        coins = 16
        points = 0
        turns = 1
    drawBoard(selectedSquare)
    building1_rect, building2_rect, random_buildings = RandomBuilding()
    building_rects = building1_rect, building2_rect
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = (mouse_x - offset_x) // sqSize
                row = (mouse_y - offset_y) // sqSize
                if exit_game_rect.collidepoint(mouse_x, mouse_y):
                    return
                for i in range(len(building_rects)):
                    if building_rects[i].collidepoint(mouse_x, mouse_y):
                        pygame.draw.rect(screen, (34,139,34), building_rects[i].inflate(margin_size * 2, margin_size * 2), 2)
                        position = get_user_input()

                        if position != None:
                            if coins > 0:
                                if checkBuildingPosition(position, i):
                                    x = alphabet.index(position[0].lower()) 
                                    y = int(position[1:]) - 1

                                    board[x][y] = random_buildings[i]
                                    coins -= 1
                                    turns += 1
                                    turn_points,turn_coins = calculatePoints()
                                    points += turn_points
                                    coins += turn_coins
                                    drawBoard(selectedSquare)
                                    building_rects[i].width = 0
                                    building1_rect, building2_rect, random_buildings = RandomBuilding()
                                    building_rects = building1_rect, building2_rect
                                    calculatePoints()
                                else:
                                    drawBoard(selectedSquare)
                                    building1_rect, building2_rect, random_buildings = RandomBuilding(random_buildings)
                        else:
                            drawBoard(selectedSquare)
                            building1_rect, building2_rect, random_buildings = RandomBuilding(random_buildings)


        if save_game_btn.draw(screen):
            Save_Game(board)
            return
        showCoins()
        if (checkGameFinish()):
            break
    showEndScreen(points)
    return

# check if the board is filled or if the player runs out of coins
def checkGameFinish():
    if coins > 0:
        for i in range(len(board)):
            for ii in range(len(board[i])):
                if board[i][ii] == "--":
                    return False
    
    return True

def display_error_message(message, screen):
    error_font = pygame.font.Font(None, 36)
    error_surface = error_font.render(message, True, (255, 0, 0))
    error_rect = error_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
    screen.blit(error_surface, error_rect)
    pygame.display.flip()
    pygame.time.delay(3000)
    screen.fill((0, 0, 0))
    pygame.display.flip()

# displaying of end screen with score and whether the player qualifies for the leaderboard
def showEndScreen(score):
    # Set up the fonts
    big_title_font = pygame.font.Font(None, 60)
    title_font = pygame.font.Font(None, 72)

    # Initialize variables for text input
    input_text = ""
    input_rect = pygame.Rect((screen.get_width() - 300) // 2, 250, 300, 40)
    input_active = False
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    font = pygame.font.Font(None, 32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    input_active = not input_active
                else:
                    input_active = False
                color = color_active if input_active else color_inactive
                
                # Check if the mouse click is within the region of the exit button
                if exit_button_rect.collidepoint(event.pos):
                  return
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        try:
                            import save_game
                            reload(save_game)
                            from save_game import game_details
                            b,leaderboard,v = game_details()
                            min_key = min(leaderboard, key=leaderboard.get)

                            del leaderboard[min_key]

                            leaderboard[input_text] = score
                            with open("save_game.py","w") as file:
                                file.write("def game_details():\n")
                                file.write("    "+"board = "+str(b)+"\n")
                                file.write("    "+"leaderboard = " + str(leaderboard) + "\n")
                                file.write("    variables = "+str(v)+"\n")
                                file.write("    "+"return board,leaderboard,variables")
                                file.close()
                        except IOError:
                            print("Error in save game")
                        return 
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        screen.fill(black)
        screen.blit(loadScoreBackground(), (0, 0))
        red = (255,0,0)
        # Draw the exit button at the top-left of the screen
        exit_button_rect = pygame.Rect(10, 10, 40, 40)
        pygame.draw.rect(screen, red, exit_button_rect)
        exit_text = big_title_font.render("X", True, white)
        screen.blit(exit_text, (15, 15))

        # Center the text on the screen
        header_text = title_font.render("Game Over", True, white)
        header_x = (screen.get_width() - header_text.get_width()) // 2
        screen.blit(header_text, (header_x, 20))  # Adjust the vertical position

        subheader_text = title_font.render(f"Your Score: {score}", True, white)
        subheader_x = (screen.get_width() - subheader_text.get_width()) // 2
        screen.blit(subheader_text, (subheader_x, 70))  # Adjust the vertical position

        # Check if the score is greater than 10 to display the input text field
        try:
            import save_game
            reload(save_game)
            from save_game import game_details
            x,leaderboard,y = game_details()
            if score >= min(leaderboard.values()):
                input_label = big_title_font.render("You made it on the leaderboard! Enter your name:", True, white)
                input_x = (screen.get_width() - input_label.get_width()) // 2
                screen.blit(input_label, (input_x, 150))

                # Draw the input text field
                pygame.draw.rect(screen, color, input_rect, 2)
                text_surface = font.render(input_text, True, white)
                width = max(200, text_surface.get_width())
                input_rect.w = width
                screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        except IOError:
            print("Error in endgame function")
        pygame.display.flip()


# for building placement whether the building placed meets the orthogonally adjacent requirement ( not for roads )
# if the turn is 1 or board is empty, building can be placed anywhere
def checkBuildingPosition(position, i):
    x = alphabet.index(position[0].lower())
    y = int(position[1:]) - 1
    if y >= 20:
        display_error_message("Please select a position in the board",screen)
        return False
    for j in range(len(board)):
        for jj in range(len(board[j])):
            if board[j][jj] != "--":
              
                if board[x][y] == "--":
                    if (board[x-1][y] != ("--" or "Ro")) or (board[x+1][y] != ("--" or "Ro")) or (board[x][y-1] != ("--" or "Ro")) or (board[x][y+1] != ("--" or "Ro")):
                        return True
                    else:
                        display_error_message("Invalid position, buildings must be orthogonally adjacent",screen)

                        return False
                else:
                    display_error_message("There is already a building on the selected square",screen)

                    return False
    return True

# saving of the main game
# gathers the game variables and write them into a new python file for simplicity
def Save_Game(gameboard):
    try:
        import save_game
        reload(save_game)
        from save_game import game_details
        board,leaderboard,variables = game_details()
        with open("save_game.py","w") as file:
            file.write("def game_details():\n")
            file.write("    "+"board = "+str(gameboard)+"\n")
            file.write("    "+"leaderboard = "+str(leaderboard)+"\n")
            file.write("    variables = {'turn': " + str(turns) + ", 'points': " + str(points) + ", 'coins': " + str(coins) + "}\n")
            file.write("    "+"return board,leaderboard,variables")

    except:
        print("Error in save game")
    return



# input prompt to ask the user for positioning placement of the buildings 
# turns ends only if valid building and position is inputted
# validation shown at the top of the screen for a few seconds
def get_user_input():
    input_box = pygame.Rect(0, 0, 200, 32)
    width, height = screen.get_width(), screen.get_height()
    input_box.center = (width // 2, height // 2)

    title_font = pygame.font.Font(None, 36)
    input_font = pygame.font.Font(None, 32)

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = True
    text = ''
    
    confirm_button = pygame.Rect(input_box.left, input_box.bottom + 10, 80, 32)
    confirm_color = pygame.Color('forestgreen')
    confirm_text = pygame.font.Font(None, 28).render('Confirm', True, (255, 255, 255))
    confirm_rect = confirm_text.get_rect(center=confirm_button.center)


    cancel_button = pygame.Rect(input_box.right - 80, input_box.bottom + 10, 80, 32)
    cancel_color = pygame.Color('firebrick')
    cancel_text = pygame.font.Font(None, 28).render('Cancel', True, (255, 255, 255))
    cancel_rect = cancel_text.get_rect(center=cancel_button.center)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

                if confirm_button.collidepoint(event.pos):
                    if (len(text) >=2 and len(text) <= 3) and text[0].isalpha() and text[1:].isdigit():
                        return text
                    else:
                        display_error_message("Invalid input. Please enter a letter followed by a number.",screen)
                        return None
                elif cancel_button.collidepoint(event.pos):
                    return None

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if (len(text) >=2 and len(text) <= 3) and text[0].isalpha() and text[1:].isdigit():
                            return text
                        else:
                            display_error_message("Invalid input. Please enter a letter followed by a number.",screen)
                            return None
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif len(text) < 3:
                        text += event.unicode

        pygame.draw.rect(screen, (255, 255, 255), input_box)
        pygame.draw.rect(screen, color, input_box, 2)
        title_surface = title_font.render("Enter Position", True, (34,139,34))
        title_rect = title_surface.get_rect(center=(width // 2, input_box.top - 30))
        screen.blit(title_surface, title_rect)
        txt_surface = input_font.render(text, True, (0, 0, 0))
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        pygame.draw.rect(screen, confirm_color, confirm_button)
        screen.blit(confirm_text, confirm_rect)

        pygame.draw.rect(screen, cancel_color, cancel_button)
        screen.blit(cancel_text, cancel_rect)

        pygame.display.flip()

def loadScoreBackground():
    background_image = pygame.image.load("background/background.jpeg")
    background_image = pygame.transform.scale(background_image, (width, height))
    return background_image


# display the leaderboard score
def show_score():
    try:
        import save_game
        reload(save_game)
        from save_game import game_details
        board, leaderboard, variables = game_details()
        # Assuming leaderboard is a dictionary
        leaderboard_items_list = list(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))

        big_title_font = pygame.font.Font(None, 60) 
        title_font = pygame.font.Font(None, 72)  

        red = (255, 0, 0)  

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_button_rect.collidepoint(event.pos):
                       return
            screen.fill(black)
            screen.blit(loadScoreBackground(), (0, 0))

            # Exit button
            exit_button_rect = pygame.Rect(10, 10, 40, 40)
            pygame.draw.rect(screen, red, exit_button_rect)
            exit_text = big_title_font.render("X", True, white)
            screen.blit(exit_text, (15, 15))

            # Center the text on the screen
            header_text = title_font.render("Ngee Ann City", True, white)
            header_x = (screen.get_width() - header_text.get_width()) // 2
            screen.blit(header_text, (header_x, 20))  # Adjust the vertical position

            subheader_text = title_font.render("High Scores", True, white)
            subheader_x = (screen.get_width() - subheader_text.get_width()) // 2
            screen.blit(subheader_text, (subheader_x, 70))  # Adjust the vertical position

            # Center the main text on the screen
            text_y = (screen.get_height() - big_title_font.get_height()) // 4

            rank = 1

            for key, value in leaderboard_items_list:
                score_text = big_title_font.render(f"{rank}: {key} {value}PTS", True, white)

                # Center the text horizontally
                text_x = (screen.get_width() - score_text.get_width()) // 2

                screen.blit(score_text, (text_x, text_y))
                text_y += 60  # Adjust the vertical spacing between scores
                rank += 1

            pygame.display.flip()

    except IOError:
        print("Leaderboard scores  not found")




# main code for the whole program to detect button clicks in the main menu
def main():
    loadBuildings()
    running = True
    while running:
        start_button_rect,load_button_rect,high_score_button_rect,exit_button_rect = drawMenu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = (mouse_x - offset_x) // sqSize
                row = (mouse_y - offset_y) // sqSize
                if start_button_rect.collidepoint(mouse_x,mouse_y):
                    new_game(False)
                elif load_button_rect.collidepoint(mouse_x, mouse_y):
                    new_game(True)
                elif high_score_button_rect.collidepoint(mouse_x,mouse_y):
                    show_score()
                elif exit_button_rect.collidepoint(mouse_x,mouse_y):
                    running = False
                    pygame.quit()
try:
    loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
    loopThread.daemon = True # shut down music thread when the rest of the program exits
    loopThread.start()
    pass
except:
    pass
main()
