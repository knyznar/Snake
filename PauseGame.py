from Renderer import *

def pauseGame():
    rect1 = pygame.Rect((WINDOW_WIDTH - 50) // 2, (WINDOW_HEIGHT - 50) // 2 - 25, 50, 50)
    rect2 = pygame.Rect((WINDOW_WIDTH - 50) // 2, (WINDOW_HEIGHT - 50) // 2 + 25, 50, 50)
    printText("Game paused", rect1, screen, 50)
    printText("Press any key to continue", rect2, screen, 20)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                return

        pygame.display.update()
