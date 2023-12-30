import pygame
import sys
grids = 20
white = (255, 255, 255)
black = (0, 0, 0)
select = (255, 0, 0)
coins = 16
points = 0

images = {}

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

def loadBuildings():
    buildings = ['bN','bB','bK','bp','bQ']
    for i in buildings:
        images[i] = pygame.transform.scale(pygame.image.load('buildings/' + i + '.png'),(sqSize,sqSize))

board = [['--'] * 20 for _ in range(20)]


start_button = pygame.image.load("buttons/start_button.jpeg")
load_button = pygame.image.load("buttons/load_button.jpeg")
high_scores_button = pygame.image.load("buttons/high_scores_button.jpeg")
exit_button = pygame.image.load("buttons/exit_button.jpeg")

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_width(), screen.get_height()
sqSize = min(width, height) // grids

offset_x = (width - grids * sqSize) // 2
offset_y = (height - grids * sqSize) // 2

exit_game_rect = pygame.Rect(10, 10, 100, 50)
exit_game_color = (255, 0, 0)
exit_game_text = pygame.font.Font(None, 36).render("Exit", True, white)
def draw_exit_button():
    pygame.draw.rect(screen, exit_game_color, exit_game_rect)
    screen.blit(exit_game_text, (exit_game_rect.centerx - exit_game_text.get_width() // 2, exit_game_rect.centery - exit_game_text.get_height() // 2))

def showCoins(player):

    font = pygame.font.Font(None, 36)
    text_content = "Coins:%d" % (player.coins)
    text_surface = font.render(text_content, True, (255, 255, 255))

    screen.blit(text_surface, (exit_game_rect.centerx - exit_game_text.get_width(), (exit_game_rect.centery - exit_game_text.get_height() // 2)+65))

def drawBuildings(screen, board):
    for row in range(grids):
        for col in range(grids):
            building = board[row][col]
            if building != '--':
                x = offset_x + col * sqSize
                y = offset_y + row * sqSize
                screen.blit(images[building], pygame.Rect(x, y, sqSize, sqSize))

def loadBackground():
    background_image = pygame.image.load("background/background.jpeg")
    background_image = pygame.transform.scale(background_image, (width, height))
    return background_image

def loadTitle():
    title_image = pygame.image.load("background/title.png")
    title_rect = title_image.get_rect(topleft=(screen.get_width()//2 - title_image.get_width() // 2, 50))
    return title_image,title_rect

def drawBoard(selectedSquare,player):
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
    showCoins(player)
    pygame.display.flip()

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

def new_game(load = False):
    player = Player("JoonHueay")
    selectedSquare = None
    global board
    global coins
    if load:
        try:
            from save_game import game_details
            board = game_details()
            print(board)
        except:
            print("No saved game")
            pass
    while True:
        drawBoard(selectedSquare,player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = (mouse_x - offset_x) // sqSize
                row = (mouse_y - offset_y) // sqSize
                if exit_game_rect.collidepoint(mouse_x, mouse_y):
                    return
                else:
                    selectedSquare = (col, row)

        drawBoard(selectedSquare,player)
        coins = coins - 1
        calculatePoints()

    return

def show_score():
    return

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
