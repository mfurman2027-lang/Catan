import pygame
from CatanState import CatanState
import tkinter as tk

# only handles display, after every turn display catanstate
def main():
    pygame.init()
    numOfPlayers = int(input("Enter number of players: "))
    if numOfPlayers > 4:
        raise ValueError("The number of players must be a number from 2 to 4")
    state = CatanState(numOfPlayers)

    screen = pygame.display.set_mode((900, 790.5))
    outline = pygame.image.load('CatanPictures\\CatanBoard.png').convert_alpha()
    outline = pygame.transform.scale(outline, (900, 790.5))
    board = state.board
    tileImages = []
    for tile in board.tileList :
        temp = pygame.image.load(tile.image).convert_alpha()
        temp = pygame.transform.scale(temp, (185, 185))
        temp = pygame.transform.rotate(temp, 30)
        tileImages.append(temp)
    running = True
    #difference of 135
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        screen.blit(outline, (0, 0))
        for i in range(0, 3) :
            screen.blit(tileImages[i], (190 + (i * 136), 35))
        for i in range(3, 7) :
            screen.blit(tileImages[i], (120 + ((i - 3) * 136), 155))
        for i in range(7, 12) :
            screen.blit(tileImages[i], (50 + ((i - 7) * 136), 275))
        for i in range(12, 16) :
            screen.blit(tileImages[i], (120 + ((i - 12) * 136), 395))
        for i in range(16, 19) :
            screen.blit(tileImages[i], (190 + ((i - 16) * 136), 515))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()