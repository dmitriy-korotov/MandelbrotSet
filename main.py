import pygame

WIDTH = 1024
HEIGHT = 720
TITLE = "MandelbrotSet"

FPS = 60

WHITE = (255, 255, 255)
GREY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(GREY)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

P = 350
scale = P / 2
view = (0, 0)
n_iter = 100

for y in range(-P + view[1], P + view[1]):
    for x in range(-P + view[0], P + view[0]):
        a = x / scale
        b = y / scale
        c = complex(a, b)
        z = complex(0)
        n = 0
        for n in range(n_iter):
            z = z**2 + c
            if abs(z) > 2:
                break

        if n == n_iter - 1:
            r = g = b = 0
        else:
            r = (n % 2) * 32 + 128
            g = (n % 4) * 64
            b = (n % 2) * 16 + 128

        pygame.draw.circle(screen, (r, g, b), (x + P - view[0], y + P - view[1]), 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
