import pygame
pygame.init()
screen = pygame.display.set_mode((1800, 1581))
img = pygame.image.load('CatanPictures\CatanBoard.png').convert_alpha()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(img, (0, 0))
    pygame.display.flip()

pygame.quit()