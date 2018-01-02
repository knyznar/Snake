from Renderer import *
from Snake import *
from Apple import *
from Button import *

pygame.init()
clock = pygame.time.Clock()

def game(gameboard):
    # gameboard = buildSquareMatrixLevel2(30)
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

        score = snake.currentScore

        moveResult = snake.move()

        if moveResult == MoveResult.isDead:
            return

        if moveResult == MoveResult.appleEaten:
            putApple(gameboard)

        screen.fill(WINDOW_COLOR)
        render(gameboard)

        scoreFrame = pygame.Rect(0, WINDOW_HEIGHT-50, WINDOW_WIDTH, 50)
        printText("Score: "+str(score), scoreFrame, screen)

        pygame.display.flip()

        clock.tick(10)


def printText(text, rect, screen):
    font = pygame.font.SysFont("comicsansms", 14)
    text = font.render(text, True, (255, 255, 255))
    horizontalMargin = (rect.width - text.get_width()) // 2
    verticalMargin = (rect.height - text.get_height()) // 2
    screen.blit(text, (rect.x + horizontalMargin, rect.y + verticalMargin))

buttonWidth = WINDOW_WIDTH // 3
buttonHeight = WINDOW_HEIGHT // 15

def showMenu():
    newGameButton = Button((WINDOW_WIDTH - buttonWidth) // 2, (WINDOW_HEIGHT - buttonHeight) // 3, buttonWidth, buttonHeight)
    mediumButton = Button(newGameButton.x, newGameButton.y + newGameButton.height + 10, buttonWidth, buttonHeight)
    hardButton = Button(newGameButton.x, newGameButton.y + 2*(newGameButton.height + 10), buttonWidth, buttonHeight)
    quitButton = Button(newGameButton.x, newGameButton.y + 3*(newGameButton.height + 10), buttonWidth, buttonHeight)


    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:    # przechwyć zamknięcie okna
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONUP:
                if newGameButton.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrix(30)
                    game(gameboard)

                if mediumButton.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrixLevel1(30)
                    game(gameboard)

                if hardButton.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrixLevel2(30)
                    game(gameboard)

                if quitButton.isInside(pygame.mouse.get_pos()):
                    pygame.quit()
                    return

        screen.fill(WINDOW_COLOR)
        pygame.display.set_caption('Snake')

        newGameButton.draw(screen)
        printText("Start game", newGameButton, screen)
        mediumButton.draw(screen)
        printText("Level Medium", mediumButton, screen)
        hardButton.draw(screen)
        printText("Level Hard", hardButton, screen)
        quitButton.draw(screen)
        printText("Quit", quitButton, screen)

        pygame.display.flip()


showMenu()
