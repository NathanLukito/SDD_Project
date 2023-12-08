import pygame
import sys
grids = 20
white = (255, 255, 255)
black = (0, 0, 0)
select = (255, 0, 0)


images = {}

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

exit_game_rect = pygame.Rect(10, 10, 100, 50) #Sizing the button
exit_game_color = (255, 0, 0) #Red color
exit_game_text = pygame.font.Font(None, 36).render("Exit", True, white)
def draw_exit_button():
    pygame.draw.rect(screen, exit_game_color, exit_game_rect)
    screen.blit(exit_game_text, (exit_game_rect.centerx - exit_game_text.get_width() // 2, exit_game_rect.centery - exit_game_text.get_height() // 2))

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

def new_game(load = False):
    selectedSquare = None
    global board
    if load:
        try:
            from save_game import game_details
            board = game_details()
            print(board)
        except:
            print("No saved game")
            pass
    while True:
        drawBoard(selectedSquare)
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
                    print(selectedSquare)
                    pass
        drawBoard(selectedSquare)
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
