import pygame

grids = 20
white = (255, 255, 255)
black = (0, 0, 0)
select = (255, 0, 0)


images = {}

def loadImages():
    buildings = ['bN','bB','bK','bp','bQ']
    for i in buildings:
        images[i] = pygame.transform.scale(pygame.image.load('buildings/' + i + '.png'),(sqSize,sqSize))

board = [['--'] * 20 for _ in range(20)]
board[1][1] = "bK"



pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_width(), screen.get_height()
sqSize = min(width, height) // grids

# Offset to center the baord
offset_x = (width - grids * sqSize) // 2
offset_y = (height - grids * sqSize) // 2

pygame.display.set_caption("Gamering Time")

exit_button_rect = pygame.Rect(10, 10, 100, 50) #Sizing the button
exit_button_color = (255, 0, 0) #Red color
exit_button_text = pygame.font.Font(None, 36).render("Exit", True, white)

def draw_exit_button():
    pygame.draw.rect(screen, exit_button_color, exit_button_rect)
    screen.blit(exit_button_text, (exit_button_rect.centerx - exit_button_text.get_width() // 2, exit_button_rect.centery - exit_button_text.get_height() // 2))

def drawBuildings(screen, board):
    for row in range(grids):
        for col in range(grids):
            building = board[row][col]
            if building != '--':
                x = offset_x + col * sqSize
                y = offset_y + row * sqSize
                screen.blit(images[building], pygame.Rect(x, y, sqSize, sqSize))

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

def main():
    loadImages()
    selectedSquare = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                col = (mouse_x - offset_x) // sqSize
                row = (mouse_y - offset_y) // sqSize
                selectedSquare = (col, row)
                print(selectedSquare)
                if exit_button_rect.collidepoint(mouse_x, mouse_y):
                    running = False
                else:
                    selectedSquare = (col, row)
                    drawBoard(selectedSquare)

        drawBoard(selectedSquare)

main()
