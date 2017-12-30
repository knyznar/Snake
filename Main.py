from Renderer import *
from Snake import *
from Apple import *
from Menu import *

pygame.init()

clock = pygame.time.Clock()
buttonWidth = WINDOW_WIDTH // 3
buttonHeight = WINDOW_HEIGHT // 15

def game():
    gameboard = buildSquareMatrix(30)
    snake = Snake(gameboard)
    putApple(gameboard)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    # przechwyć zamknięcie okna
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                snake.setDirection(event.key)
                break

        moveResult = snake.move()


        if moveResult == MoveResult.isDead:
            print("Przegrołeś")
            return

        if moveResult == MoveResult.appleEaten:
            putApple(gameboard)

        screen.fill(WINDOW_COLOR)
        render(gameboard)
        pygame.display.flip()

        clock.tick(10)

def printText(text, x, y, screen):
    font = pygame.font.SysFont("comicsansms", 14)
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (x + 10, y + text.get_height() // 2))


def showMenu():
    newGameButton = Button((WINDOW_WIDTH - buttonWidth) // 2, (WINDOW_HEIGHT - buttonHeight) // 3, buttonWidth, buttonHeight)
    quitButton = Button(newGameButton.x, newGameButton.y + newGameButton.height + 10, buttonWidth, buttonHeight)


    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    # przechwyć zamknięcie okna
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONUP:
                if newGameButton.isInside(pygame.mouse.get_pos()):
                    game()

                if quitButton.isInside(pygame.mouse.get_pos()):
                    pygame.quit()
                    return

        screen.fill(WINDOW_COLOR)

        newGameButton.draw(screen)
        printText("Start Game", newGameButton.x, newGameButton.y, screen)
        quitButton.draw(screen)
        printText("Quit", quitButton.x, quitButton.y, screen)

        pygame.display.flip()


showMenu()