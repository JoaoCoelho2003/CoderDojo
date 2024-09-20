# Introdução ao Pygame

## O que é o Pygame?

Pygame é uma biblioteca em Python usada para desenvolvimento de jogos. Ela fornece funcionalidades que facilitam a criação de jogos 2D, como manipulação de gráficos, sons e eventos.

## Instalação

Para instalar o Pygame, utilize o seguinte comando:

```bash
pip install pygame
```

## Principais Funcionalidades

### Inicialização

Antes de usar qualquer funcionalidade do Pygame, é necessário inicializar a biblioteca:

```python
import pygame
pygame.init()
```

### Janela do Jogo

Para criar uma janela de jogo, utilize a função `set_mode`:

```python
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu Jogo")
```

### Loop Principal

O loop principal do jogo é onde a lógica do jogo é atualizada e os gráficos são renderizados:

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Preenche a tela com a cor preta
    pygame.display.flip()  # Atualiza a tela

pygame.quit()
```

### Desenhando na Tela

Você pode desenhar formas simples como retângulos e círculos:

```python
pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))  # Desenha um retângulo vermelho
pygame.draw.circle(screen, (0, 255, 0), (400, 300), 50)  # Desenha um círculo verde
```

### Carregando Imagens

Para carregar e exibir imagens:

```python
imagem = pygame.image.load('caminho/para/imagem.png')
screen.blit(imagem, (100, 100))
```

### Sons e Música

Para carregar e reproduzir sons:

```python
pygame.mixer.init()
som = pygame.mixer.Sound('caminho/para/som.wav')
som.play()
```

Para música de fundo:

```python
pygame.mixer.music.load('caminho/para/musica.mp3')
pygame.mixer.music.play(-1)  # -1 para repetir indefinidamente
```

## Conclusão

Pygame é uma ferramenta poderosa para criar jogos 2D em Python. Com suas funcionalidades abrangentes, você pode criar desde jogos simples até projetos mais complexos. Explore a documentação oficial para aprender mais sobre as capacidades do Pygame.

## Eventos

Os eventos são ações que ocorrem durante o jogo, como pressionar uma tecla ou mover o rato. Para capturar eventos, utilize o método `pygame.event.get()` dentro do loop principal:

```python
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False
```

## Movimentação de Personagens

Para mover personagens no ecrã, atualize as suas coordenadas dentro do loop principal:

```python
x, y = 100, 100
velocidade = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocidade
    if keys[pygame.K_RIGHT]:
        x += velocidade
    if keys[pygame.K_UP]:
        y -= velocidade
    if keys[pygame.K_DOWN]:
        y += velocidade

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 50, 50))
    pygame.display.flip()

pygame.quit()
```

## Colisões

Para detectar colisões entre objetos, utilize o método `colliderect`:

```python
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(200, 200, 50, 50)

if rect1.colliderect(rect2):
    print("Colisão detectada!")
```

## Texto na Tela

Para exibir texto na tela, utilize a classe `pygame.font.Font`:

```python
pygame.font.init()
fonte = pygame.font.Font(None, 36)
texto = fonte.render('Olá, Pygame!', True, (255, 255, 255))
screen.blit(texto, (250, 250))
```

## Controlos Avançados

Para criar controlos mais avançados, como menus ou interfaces de utilizador, considere utilizar bibliotecas adicionais como `pygame_gui`:

```python
import pygame_gui

manager = pygame_gui.UIManager((800, 600))
botao = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                     text='Clique-me',
                                     manager=manager)

while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        manager.process_events(event)

    manager.update(time_delta)
    screen.fill((0, 0, 0))
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()
```
