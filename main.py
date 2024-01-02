# importing of necessary python libraries needed
import pygame
import os
import sys
import random

#initiating of simple constant game variables
grids = 20
white = (255, 255, 255)
black = (0, 0, 0)
select = (255, 0, 0)
coins = 16
points = 0
turns = 1
images = {}
buildings = ["R","I","C","O","Ro"]
alphabet = "abcdefghijklmnopqrstuvwxyz"
board = []
pygame.init()

#initiating class for ???
class Building:
    def __init__(self, building_type, row, col, cost = 1):
        self.building_type = building_type
        self.row = row
        self.col = col
        self.cost = cost

class Player:
    def __init__(self, name, coins = 16, score = 0):
        self.name = name
        self.coins = coins
        self.score = score

#Create saved game btn - Liwei
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
save_game_btn = SaveGameButton(90, 10, save_game_btn_img, 0.15)

def loadBuildings():
    for i in buildings:
        images[i] = pygame.transform.scale(pygame.image.load('buildings/' + i + '.png'),(sqSize,sqSize))

# initiating the meanu menu buttons and screen dimensions with background
start_button = pygame.image.load("buttons/start_button.jpeg")
load_button = pygame.image.load("buttons/load_button.jpeg")
high_scores_button = pygame.image.load("buttons/high_scores_button.jpeg")
exit_button = pygame.image.load("buttons/exit_button.jpeg")

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_width(), screen.get_height()
sqSize = min(width, height) // grids

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
    font = pygame.font.Font(None, 36)
    text_content = "Coins:%d" % (coins)
    text_surface = font.render(text_content, True, (255, 255, 255))
    screen.blit(text_surface, (exit_game_rect.centerx - exit_game_text.get_width(), (exit_game_rect.centery - exit_game_text.get_height() // 2)+65))

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
    for row in range(grids):
        for col in range(grids):
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

def drawBoard(selectedSquare):
    screen.fill(black)
    colors = [pygame.Color('white'), pygame.Color('gray')]
    for row in range(grids):
        for col in range(grids):
            x = offset_x + col * sqSize
            y = offset_y + row * sqSize
            rect = pygame.Rect(x, y, sqSize, sqSize)
            if (col, row) == selectedSquare:
                color = select
            else:
                color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, rect)
    drawBuildings(screen, board)
    draw_exit_button()
    if save_game_btn.draw(screen):#Liwei
            print("Game Saved")
    showCoins()
    drawText("Turn:"+str(turns),pygame.font.SysFont(None,26),(255,255,255),150,87) # show the number of turn - liwei
    drawText("Score:"+str(points),pygame.font.SysFont(None,26),(255,255,255),240,87) #show the number of points - Liwei
    residential_rect,industry_rect,commercial_rect,park_rect,road_rect = showBuildings()
    pygame.display.flip()

    return residential_rect,industry_rect,commercial_rect,park_rect,road_rect

#drawing and placing of the main menu items onto the main menu screen
def drawMenu():
    screen.blit(loadBackground(), (0, 0))
    title_image, title_rect = loadTitle()
    screen.blit(title_image, title_rect)
    total_button_height = (start_button.get_height() + load_button.get_height() + high_scores_button.get_height() + exit_button.get_height())

    start_y = (screen.get_height() - total_button_height) // 2
    center_x = screen.get_width() // 2

    start_button_rect = start_button.get_rect(topleft=(center_x - start_button.get_width() // 2, start_y))
    load_button_rect = load_button.get_rect(topleft=(center_x - load_button.get_width() // 2, start_y + start_button.get_height()))
    high_scores_button_rect = high_scores_button.get_rect(topleft=(center_x - high_scores_button.get_width() // 2, start_y + start_button.get_height() + load_button.get_height()))
    exit_button_rect = exit_button.get_rect(topleft=(center_x - exit_button.get_width() // 2, start_y + start_button.get_height() + load_button.get_height() + high_scores_button.get_height()))
    screen.blit(start_button, start_button_rect)
    screen.blit(load_button, load_button_rect)
    screen.blit(high_scores_button, high_scores_button_rect)
    screen.blit(exit_button, exit_button_rect)

    pygame.display.flip()
    return start_button_rect,load_button_rect,high_scores_button_rect,exit_button_rect

# documentation for points calculation here
def calculatePoints():
    turn_points = 0
    turn_coins = 0
    rows = len(board)
    cols = len(board[0])
    def check_position(i, x):
        return 0 <= i < rows and 0 <= x < cols

    def add_points(i, x, building, points):
        if check_position(i, x) and board[i][x] == building:
            nonlocal turn_points
            turn_points += points
        else:
            pass
    def add_coins(i, x, building, coins):
        if check_position(i, x) and board[i][x] == building:
            nonlocal turn_coins
            turn_coins += coins
        else:
            pass

    for i in range(rows):
        for x in range(cols):
            if board[i][x] == 'Re':
                add_points(i, x + 1, 'In', 1)
                add_points(i, x - 1, 'In', 1)
                add_points(i + 1, x, 'In', 1)
                add_points(i - 1, x, 'In', 1)
                add_points(i - 1, x - 1, 'In', 1)
                add_points(i - 1, x + 1, 'In', 1)
                add_points(i + 1, x - 1, 'In', 1)
                add_points(i + 1, x + 1, 'In', 1)
                add_points(i, x + 1, 'Re', 1)
                add_points(i, x - 1, 'Re', 1)
                add_points(i + 1, x, 'Re', 1)
                add_points(i - 1, x, 'Re', 1)
                add_points(i, x + 1, 'Co', 1)
                add_points(i, x - 1, 'Co', 1)
                add_points(i + 1, x, 'Co', 1)
                add_points(i - 1, x, 'Co', 1)
                add_points(i, x + 1, 'Pa', 2)
                add_points(i, x - 1, 'Pa', 2)
                add_points(i + 1, x, 'Pa', 2)
                add_points(i - 1, x, 'Pa', 2)

            if board[i][x] == 'In':
                turn_points += 1
                add_coins(i, x + 1, 'Re', 1)
                add_coins(i, x - 1, 'Re', 1)
                add_coins(i + 1, x, 'Re', 1)
                add_coins(i - 1, x, 'Re', 1)

            if board[i][x] == 'Co':
                add_points(i, x + 1, 'Co', 1)
                add_points(i, x - 1, 'Co', 1)
                add_points(i + 1, x, 'Co', 1)
                add_points(i - 1, x, 'Co', 1)

                add_coins(i, x + 1, 'Re', 1)
                add_coins(i, x - 1, 'Re', 1)
                add_coins(i + 1, x, 'Re', 1)
                add_coins(i - 1, x, 'Re', 1)

            if board[i][x] == 'Pa':
                add_points(i, x + 1, 'Pa', 1)
                add_points(i, x - 1, 'Pa', 1)
                add_points(i + 1, x, 'Pa', 1)
                add_points(i - 1, x, 'Pa', 1)

            if board[i][x] == 'Ro':
                for a in range(cols):
                    add_points(i, x + a, 'Ro', 1)
            else:
                pass
    global points
    global coins

    points += turn_points
    coins += turn_coins
    return

# call upon the building list and remove Road and place onto the main screen to click and place for first turn ONLY
def initialRandomBuilding():
    random_building_names = random.sample(list(images.keys())[:4], 2)
    center_x = screen.get_width() // 2
    center_y = screen.get_height() // 2
    width = 512
    height = 512
    x = center_x - width // 2
    y = center_y - height // 2

    overlay = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    building1_rect = pygame.transform.scale(images[random_building_names[0]], (256, 256)).get_rect(topleft=(x + 50, y + 50))
    building2_rect = pygame.transform.scale(images[random_building_names[1]], (256, 256)).get_rect(topleft=(x + 512, y + 50))
    screen.blit(images[random_building_names[0]], building1_rect.topleft)
    screen.blit(images[random_building_names[1]], building2_rect.topleft)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if building1_rect.collidepoint(mouse_x, mouse_y):
                    position = get_user_input()
                    x = alphabet.index(position[0].lower())
                    y = int(position[1]) - 1
                    board[x][y] = random_building_names[0]
                    running = False
                elif building2_rect.collidepoint(mouse_x, mouse_y):
                    position = get_user_input()
                    x = alphabet.index(position[0].lower())
                    y = int(position[1]) - 1
                    board[x][y] = random_building_names[1]
                    running = False

    return

# main game logic
# checks whether loading of game is needed if not create a new game
# drawing of main game elements and items 
# detection of mouseclicks and board interaction for selecting squares and for placing of buildings, exit and saving of the game
# turn calculation is every successful building placement not the while loop
def new_game(load = False):
    player = Player("JoonHueay")
    selectedSquare = None
    global coins
    global turns
    global board
    global coins
    if load:
        try:
            from save_game import game_details
            board = game_details()
        except:
            print("No saved game")
            pass
    else:
        board = [['--'] * grids for _ in range(20)]
        coins = 16
        points = 0
        turns = 1
    while True:
        residential_rect,industry_rect,commercial_rect,park_rect,road_rect = drawBoard(selectedSquare)
        building_rects = [residential_rect,industry_rect,commercial_rect,park_rect,road_rect]
        if turns == 1:
            initialRandomBuilding()
            turns += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #add one button for game saving @Liwei
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = (mouse_x - offset_x) // sqSize
                row = (mouse_y - offset_y) // sqSize
                if exit_game_rect.collidepoint(mouse_x, mouse_y):
                    return
                for i in range(len(building_rects)):
                    if building_rects[i].collidepoint(mouse_x, mouse_y):
                        print(board)
                        position = get_user_input()
                        if position != None:
                            if coins > 0:
                                if checkBuildingPosition(position,i):
                                    x = alphabet.index(position[0].lower()) 
                                    y = int(position[1]) - 1
                                    board[x][y] = buildings[i]
                                    coins -= 1
                                    turns += 1
                                    
                        
                else:
                    selectedSquare = (col, row)

        calculatePoints()
        if save_game_btn.draw(screen):#Liwei
            print("Game Saved")
        showCoins()
        if (checkGameFinish()):
            score = calculatePoints()
            break
    showEndScreen(score)
    return

# check if the board is filled or if the player runs out of coins
def checkGameFinish():
    if coins > 0:
        for i in range(len(board)):
            for ii in range(len(board[i])):
                if board[i][ii] == "--":
                    return False
    return True

# displaying of end screen with score and whether the player qualifies for the leaderboard
def showEndScreen(score):
    # check qualify for leaderboard anot
    return 

# for building placement whether the building placed meets the orthogonally adjacent requirement ( not for roads )
# if the turn is 1 or board is empty, building can be placed anywhere
def checkBuildingPosition(position,i):
    for j in range(len(board)):
        for jj in range(len(board[j])):
            if board[j][jj] != "--":
                x = alphabet.index(position[0].lower())
                y = int(position[1]) - 1
                if i != 4:
                    if (board[x-1][y] != ("--" or "Ro")) or (board[x+1][y] != ("--" or "Ro")) or (board[x][y-1] != ("--" or "Ro")) or (board[x][y+1] != ("--" or "Ro")):
                        return True
                    else:
                        return False
                else:
                    return True

    return True

# saving of the main game
# gathers the game variables and write them into a new python file for simplicity
def Save_Game():
    try:
        from save_game import game_details
        board,leaderboard,variables = game_details()
        with open("save_game.py","w") as file:
            file.write("def game_details():\n")
            file.write("    "+"board = "+str(board)+"\n")
            file.write("    "+"leaderboard = "+str(leaderboard)+"\n")
            file.write("    variables = {turn: " + str(turns) + ", points: " + str(points) + ", coins: " + str(coins) + "}\n")
            file.write("    "+"return board,leaderboard,variables")
            file.close()
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

    if turns != 1:
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
                if turns != 1:
                    if confirm_button.collidepoint(event.pos):
                        if len(text) == 2 and text[0].isalpha() and text[1].isdigit():
                            return text
                        else:
                            print("Invalid input. Please enter a letter followed by a number.")
                    elif cancel_button.collidepoint(event.pos):
                        return None
                else:
                    if confirm_button.collidepoint(event.pos):
                        if len(text) == 2 and text[0].isalpha() and text[1].isdigit():
                            return text
                        else:
                            print("Invalid input. Please enter a letter followed by a number.")
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        if len(text) == 2 and text[0].isalpha() and text[1].isdigit():
                            return text
                        else:
                            print("Invalid input. Please enter a letter followed by a number.")
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    elif len(text) < 2:
                        text += event.unicode

        pygame.draw.rect(screen, (255, 255, 255), input_box)
        pygame.draw.rect(screen, color, input_box, 2)
        title_surface = title_font.render("Enter Position", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(width // 2, input_box.top - 30))
        screen.blit(title_surface, title_rect)
        txt_surface = input_font.render(text, True, (0, 0, 0))
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

        pygame.draw.rect(screen, confirm_color, confirm_button)
        screen.blit(confirm_text, confirm_rect)

        if turns != 1:
            pygame.draw.rect(screen, cancel_color, cancel_button)
            screen.blit(cancel_text, cancel_rect)

        pygame.display.flip()
        pygame.time.wait(30)

# display the leaderboard score
def show_score():
    try:
        from save_game import game_details
        board,leaderboard,variables = game_details()
        return leaderboard
    except:
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

main()
