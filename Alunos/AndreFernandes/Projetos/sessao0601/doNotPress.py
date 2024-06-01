import pygame

pygame.init()

alt = 600
larg = 800

screen = pygame.display.set_mode((larg, alt))
tamanho = 36


fonte = pygame.font.Font(None,tamanho)
fontes = fonte.render("não pressionar",True,(255,255,255))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            tamanho += 1
            fonte = pygame.font.Font(None,tamanho)
            fontes = fonte.render("não pressionar",True,(255,255,255))

    
    screen.fill((0,0,0))
    screen.blit(fontes, (larg//2-fontes.get_width()//2, alt//2-fontes.get_height()//2))

    pygame.display.flip()

pygame.quit()

    
