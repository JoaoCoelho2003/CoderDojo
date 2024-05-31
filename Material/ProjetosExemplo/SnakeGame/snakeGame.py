import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
SNAKE_SIZE = 25
SNAKE_SPEED = 10

# Screen setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 60)

# Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction

# Food
food_pos = [random.randrange(1, (WINDOW_WIDTH // 25)) * 25,
            random.randrange(1, (WINDOW_HEIGHT // 25)) * 25]
food_spawn = True

# Game variables
score = 0
clock = pygame.time.Clock()
running = True
game_over_flag = False

def draw_food():
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))

def draw_text(text, color, center_x, center_y):
    img = font.render(text, True, color)
    rect = img.get_rect(center=(center_x, center_y))
    screen.blit(img, rect)

def draw_game_over():
    screen.fill(BLACK)
    draw_text("Game Over", WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
    draw_text("Press R to Restart or Q to Quit", WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)
    pygame.display.update()

def reset_game():
    global snake_pos, snake_body, direction, change_to, food_pos, food_spawn, score, game_over_flag
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    change_to = direction
    food_pos = [random.randrange(1, (WINDOW_WIDTH // 25)) * 25,
                random.randrange(1, (WINDOW_HEIGHT // 25)) * 25]
    food_spawn = True
    score = 0
    game_over_flag = False

while running:
    while game_over_flag:
        draw_game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_over_flag = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                elif event.key == pygame.K_q:
                    running = False
                    game_over_flag = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if direction != 'DOWN':
                    change_to = 'UP'
            elif event.key == pygame.K_s:
                if direction != 'UP':
                    change_to = 'DOWN'
            elif event.key == pygame.K_a:
                if direction != 'RIGHT':
                    change_to = 'LEFT'
            elif event.key == pygame.K_d:
                if direction != 'LEFT':
                    change_to = 'RIGHT'

    if change_to == 'UP':
        snake_pos[1] -= SNAKE_SIZE
    if change_to == 'DOWN':
        snake_pos[1] += SNAKE_SIZE
    if change_to == 'LEFT':
        snake_pos[0] -= SNAKE_SIZE
    if change_to == 'RIGHT':
        snake_pos[0] += SNAKE_SIZE

    direction = change_to
    snake_body.insert(0, list(snake_pos))

    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WINDOW_WIDTH // 25)) * 25,
                    random.randrange(1, (WINDOW_HEIGHT // 25)) * 25]
    food_spawn = True

    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

    draw_food()

    # Check for collisions with boundaries
    if snake_pos[0] < 0 or snake_pos[0] >= WINDOW_WIDTH or snake_pos[1] < 0 or snake_pos[1] >= WINDOW_HEIGHT:
        game_over_flag = True

    # Check for collisions with itself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over_flag = True

    pygame.display.update()
    clock.tick(SNAKE_SPEED)

pygame.quit()
