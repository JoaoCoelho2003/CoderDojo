import pygame
import sys
import math
import random
from pygame.locals import QUIT

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shooter Game')

# Load and scale the player image
player_image = pygame.image.load('character.png').convert_alpha()
player_image = pygame.transform.scale(player_image, (40, 50))

player = pygame.Rect((300, 250), (40, 50))
bullets = []
enemies = []
BULLET_SPEED = 5
ENEMY_SPEED = 2
PLAYER_HP = 5
SPAWN_DELAY = 2500  # milliseconds

# Define walls
walls = [
    pygame.Rect((100, 100), (200, 50)),
    pygame.Rect((400, 300), (50, 200)),
    pygame.Rect((600, 100), (150, 150))
]

# Define enemy structure
class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.hp = 3

def get_random_position():
    while True:
        x = random.randint(0, SCREEN_WIDTH - 40)
        y = random.randint(0, SCREEN_HEIGHT - 40)
        new_rect = pygame.Rect(x, y, 40, 40)
        if not new_rect.colliderect(player) and not any(new_rect.colliderect(wall) for wall in walls):
            return x, y

def spawn_enemy():
    x, y = get_random_position()
    enemies.append(Enemy(x, y))

def game_over_menu():
    font = pygame.font.Font(None, 74)
    menu_font = pygame.font.Font(None, 36)
    text = font.render('Game Over', True, (255, 0, 0))
    leave_text = menu_font.render('Press Q to Quit', True, (255, 255, 255))
    restart_text = menu_font.render('Press R to Restart', True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    return True  # Indicate that the game should be restarted

        screen.fill((0, 0, 0))
        screen.blit(text, ((SCREEN_WIDTH - text.get_width()) // 2, SCREEN_HEIGHT // 3))
        screen.blit(restart_text, ((SCREEN_WIDTH - restart_text.get_width()) // 2, SCREEN_HEIGHT // 2))
        screen.blit(leave_text, ((SCREEN_WIDTH - leave_text.get_width()) // 2, SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()

def reset_game():
    global player, bullets, enemies, PLAYER_HP, last_spawn_time
    player = pygame.Rect((300, 250), (40, 50))
    bullets = []
    enemies = []
    PLAYER_HP = 5
    last_spawn_time = pygame.time.get_ticks()

last_spawn_time = pygame.time.get_ticks()
clock = pygame.time.Clock()  # Create a clock object
FPS = 60  # Desired frames per second

run = True

while run:
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time > SPAWN_DELAY:
        spawn_enemy()
        last_spawn_time = current_time

    screen.fill((0, 0, 0))

    # Draw the player image
    screen.blit(player_image, player.topleft)

    # Draw walls
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall)

    # Move the player with collision detection
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-2, 0)
        if any(player.colliderect(wall) for wall in walls):
            player.move_ip(2, 0)
    if key[pygame.K_d]:
        player.move_ip(2, 0)
        if any(player.colliderect(wall) for wall in walls):
            player.move_ip(-2, 0)
    if key[pygame.K_w]:
        player.move_ip(0, -2)
        if any(player.colliderect(wall) for wall in walls):
            player.move_ip(0, 2)
    if key[pygame.K_s]:
        player.move_ip(0, 2)
        if any(player.colliderect(wall) for wall in walls):
            player.move_ip(0, -2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                bullet_x = player.centerx
                bullet_y = player.centery

                # Calculate direction vector
                direction_x = mouse_x - bullet_x
                direction_y = mouse_y - bullet_y
                length = math.hypot(direction_x, direction_y)
                direction_x /= length
                direction_y /= length

                # Create a new bullet
                bullets.append({
                    'rect': pygame.Rect(bullet_x, bullet_y, 5, 5),
                    'dir_x': direction_x,
                    'dir_y': direction_y
                })

    for bullet in bullets[:]:
        bullet['rect'].move_ip(bullet['dir_x'] * BULLET_SPEED, bullet['dir_y'] * BULLET_SPEED)

        # Remove bullets that go off-screen or hit a wall
        if not screen.get_rect().colliderect(bullet['rect']) or any(bullet['rect'].colliderect(wall) for wall in walls):
            bullets.remove(bullet)

    # Move enemies towards the player and check for collision
    for enemy in enemies[:]:
        direction_x = player.centerx - enemy.rect.centerx
        direction_y = player.centery - enemy.rect.centery
        length = math.hypot(direction_x, direction_y)
        direction_x /= length
        direction_y /= length

        # Prevent enemy from moving through walls
        new_rect = enemy.rect.move(direction_x * ENEMY_SPEED, direction_y * ENEMY_SPEED)
        if not any(new_rect.colliderect(wall) for wall in walls):
            enemy.rect.move_ip(direction_x * ENEMY_SPEED, direction_y * ENEMY_SPEED)

        # Check collision with player
        if player.colliderect(enemy.rect):
            PLAYER_HP -= 1
            enemies.remove(enemy)
            if PLAYER_HP <= 0:
                if game_over_menu():
                    reset_game()
                else:
                    run = False

        # Check collision with bullets
        for bullet in bullets[:]:
            if enemy.rect.colliderect(bullet['rect']):
                bullets.remove(bullet)
                enemy.hp -= 1
                if enemy.hp <= 0:
                    enemies.remove(enemy)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy.rect)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, (0, 255, 0), bullet['rect'])

    # Display HP
    font = pygame.font.Font(None, 36)
    hp_text = font.render(f'HP: {PLAYER_HP}', True, (255, 255, 255))
    screen.blit(hp_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)  # Limit the frame rate to the desired FPS

pygame.quit()
