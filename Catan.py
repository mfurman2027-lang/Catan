import pygame
import sys
from CatanState import CatanState

WHITE = (255, 255, 255)
DARK_BLUE = (20, 50, 90)
LIGHT_BLUE = (40, 90, 160)
LIGHT_GREY = (211, 211, 211)

class Button:

    def __init__(self, name, x, y, width, height, text):
        self.name = name
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

        self.font = pygame.font.SysFont("Arial", 30)

        self.current_color = DARK_BLUE
        self.is_clicked = False

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.current_color = LIGHT_GREY
        else:
            self.current_color = WHITE

        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=8)

        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return self.on_button_click()
        
        return ""
    
    def on_button_click(self):
        return self.name

# only handles display, after every turn display catanstate
def main():
    pygame.init()
    numOfPlayers = askForPlayers()
    state = CatanState(numOfPlayers)

    screen = pygame.display.set_mode((900, 790.5))
    outline = pygame.image.load('CatanPictures\\CatanBoard.png').convert_alpha()
    outline = pygame.transform.scale(outline, (900, 790.5))
    clock = pygame.time.Clock()
    board = state.board

    tileAndNumberInfo = getTileAndNumberInfo(board)
    tileImages = tileAndNumberInfo[0]
    numberImages = tileAndNumberInfo[1]

    running = True
    #difference of 135
    my_button = Button("bOne", x=240, y=115, width=10, height=10, text="")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if my_button.check_click(event) != "":
                print("clicked")

        pygame.display.flip()
        clock.tick(60)
        
        displayTilesAndNumbers(screen, tileImages, numberImages, outline)
        my_button.draw(screen)
        pygame.display.flip()

    pygame.quit()

def askForPlayers():
    numPlayers = int(input("Enter number of players: "))
    if numPlayers > 4:
        raise ValueError("The number of players must be a number from 2 to 4")

    return numPlayers

def getTileAndNumberInfo(board):
    tileImages = []
    numberImages = []

    for i in range(19) :
        tile = board.tileDict[i]
        temp = pygame.image.load(tile.image).convert_alpha()
        temp = pygame.transform.scale(temp, (185, 185))
        temp = pygame.transform.rotate(temp, 30)
        number = pygame.image.load(f"CatanPictures\\Numbers\\{tile.number}.png").convert_alpha()
        number = pygame.transform.scale(number, (60, 60))
        numberImages.append(number)
        tileImages.append(temp)

    return [tileImages, numberImages]

def displayTilesAndNumbers(screen, tileImages, numberImages, outline):
    screen.fill((255, 255, 255))
    screen.blit(outline, (0, 0))
    for i in range(0, 3) :
        screen.blit(tileImages[i], (190 + (i * 136), 35))
        screen.blit(numberImages[i], (285 + (i * 136), 130))
    for i in range(3, 7) :
        screen.blit(tileImages[i], (120 + ((i - 3) * 136), 155))
        screen.blit(numberImages[i], (215 + ((i - 3) * 136), 250))
    for i in range(7, 12) :
        screen.blit(tileImages[i], (50 + ((i - 7) * 136), 275))
        screen.blit(numberImages[i], (145 + ((i - 7) * 136), 370))
    for i in range(12, 16) :
        screen.blit(tileImages[i], (120 + ((i - 12) * 136), 395))
        screen.blit(numberImages[i], (215 + ((i - 12) * 136), 490))
    for i in range(16, 19) :
        screen.blit(tileImages[i], (190 + ((i - 16) * 136), 515))
        screen.blit(numberImages[i], (285 + ((i - 16) * 136), 610))

if __name__ == "__main__":
    main()