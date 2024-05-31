# Não Pressione O Botão: Um botão com a mensagem a dizer que não o deves pressionar. A cada vez que é pressionado, a mensagem cresce

import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Não Pressione O Botão")

font_size = 36

message_font = pygame.font.Font(None, font_size)
message = message_font.render("Não Pressione O Botão", True, (255, 255, 255))

on = True

while on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            font_size += 1
            message_font = pygame.font.Font(None, font_size)
            message = message_font.render("Não Pressione O Botão", True, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(message, (WINDOW_WIDTH // 2 - message.get_width() // 2, WINDOW_HEIGHT // 2 - message.get_height() // 2))

    pygame.display.flip()

pygame.quit()

