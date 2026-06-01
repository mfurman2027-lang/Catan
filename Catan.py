import pygame

# only handles display, after every turn display catanstate
def main():
    pygame.init()
    
    screen = pygame.display.set_mode((900, 790.5))
    img = pygame.image.load('CatanPictures\CatanBoard.png').convert_alpha()
    img = pygame.transform.scale(img, (900, 790.5))
    running = True
    CatanState()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        screen.blit(img, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()