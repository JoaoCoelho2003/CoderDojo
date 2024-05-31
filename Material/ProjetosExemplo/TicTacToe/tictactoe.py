import pygame

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Screen setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 60)

# Game variables
player = 1
game_over = False
winner = 0
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def draw_board():
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i * WINDOW_WIDTH // 3, 0), (i * WINDOW_WIDTH // 3, WINDOW_HEIGHT), 10)
        pygame.draw.line(screen, BLACK, (0, i * WINDOW_HEIGHT // 3), (WINDOW_WIDTH, i * WINDOW_HEIGHT // 3), 10)

def draw_x(x, y):
    pygame.draw.line(screen, RED, (x * WINDOW_WIDTH // 3 + 20, y * WINDOW_HEIGHT // 3 + 20), (x * WINDOW_WIDTH // 3 + WINDOW_WIDTH // 3 - 20, y * WINDOW_HEIGHT // 3 + WINDOW_HEIGHT // 3 - 20), 10)
    pygame.draw.line(screen, RED, (x * WINDOW_WIDTH // 3 + WINDOW_WIDTH // 3 - 20, y * WINDOW_HEIGHT // 3 + 20), (x * WINDOW_WIDTH // 3 + 20, y * WINDOW_HEIGHT // 3 + WINDOW_HEIGHT // 3 - 20), 10)

def draw_o(x, y):
    pygame.draw.ellipse(screen, BLUE, (x * WINDOW_WIDTH // 3 + 20, y * WINDOW_HEIGHT // 3 + 20, WINDOW_WIDTH // 3 - 40, WINDOW_HEIGHT // 3 - 40), 10)

def check_winner():
    global winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            winner = board[i][0]
            return True
        if board[0][i] == board[1][i] == board[2][i] != 0:
            winner = board[0][i]
            return True
    if board[0][0] == board[1][1] == board[2][2] != 0:
        winner = board[0][0]
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        winner = board[0][2]
        return True
    return False

def check_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True

def draw_text(text, color, center_x, center_y):
    img = font.render(text, True, color)
    rect = img.get_rect(center=(center_x, center_y))
    screen.blit(img, rect)

def reset_game():
    global player, game_over, winner, board
    player = 1
    game_over = False
    winner = 0
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def draw_game_over():
    screen.fill(WHITE)
    if winner != 0:
        draw_text(f"Player {winner} wins!", BLACK, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
    else:
        draw_text("It's a draw!", BLACK, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
    draw_text("Press R to restart", BLACK, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)

running = True

while running:
    screen.fill(WHITE)
    draw_board()

    for y in range(3):
        for x in range(3):
            if board[y][x] == 1:
                draw_x(x, y)
            elif board[y][x] == 2:
                draw_o(x, y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            x = x // (WINDOW_WIDTH // 3)
            y = y // (WINDOW_HEIGHT // 3)
            if board[y][x] == 0:
                board[y][x] = player
                if check_winner():
                    game_over = True
                elif check_draw():
                    game_over = True
                player = 2 if player == 1 else 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    if game_over:
        draw_game_over()

    pygame.display.flip()

pygame.quit()
