import pygame
from random import randrange

res = 800
size = 50
x, y = randrange(0, res, size), randrange(0, res, size)
apple = randrange(0, res, size), randrange(0, res, size)
len = 1
snake = [(x, y)]
dx, by = 0, 0
speed = 3
pygame.init()
sc = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('black'))

    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, size, size))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, size, size))

    x += dx * size
    y += by * size
    snake.append((x, y))
    snake = snake[-len:]

    if snake[-1] == apple:
        apple = randrange(0, res, size), randrange(0, res, size)
        len += 1
        if len == 5:
            speed += 1

        pygame.display.flip()
        clock.tick(speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, by = 0, -1
    if key[pygame.K_s]:
        dx, by = 0, 1
    if key[pygame.K_a]:
        dx, by = -1, 0
    if key[pygame.K_d]:
        dx, by = 1, 0

