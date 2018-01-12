from Renderer import *
from Snake import *
from Apple import *
from Button import *

pygame.init()
clock = pygame.time.Clock()

def game(gameboard):
    snake = Snake(gameboard)
    putApple(gameboard)
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                snake.setDirection(event.key)
                break

        score = snake.currentScore

        moveResult = snake.move()

        if moveResult == MoveResult.isDead:
            return score

        if moveResult == MoveResult.appleEaten:
            putApple(gameboard)

        screen.fill(WINDOW_COLOR)
        render(gameboard)

        scoreFrame = pygame.Rect(0, WINDOW_HEIGHT-50, WINDOW_WIDTH, 50)
        printText("Score: "+str(score), scoreFrame, screen)

        pygame.display.flip()

        clock.tick(10)


def printText(text, rect, screen):
    font = pygame.font.SysFont("comicsansms", 15)
    text = font.render(text, True, (255, 255, 255))
    horizontalMargin = (rect.width - text.get_width()) // 2
    verticalMargin = (rect.height - text.get_height()) // 2
    screen.blit(text, (rect.x + horizontalMargin, rect.y + verticalMargin))

buttonWidth = WINDOW_WIDTH // 3
buttonHeight = WINDOW_HEIGHT // 15

def showMenu():
    easyButton = Button((WINDOW_WIDTH - buttonWidth) // 2, (WINDOW_HEIGHT - buttonHeight) // 3 + 20, buttonWidth, buttonHeight)
    mediumButton = Button(easyButton.x, easyButton.y + easyButton.height + 10, buttonWidth, buttonHeight)
    hardButton = Button(easyButton.x, easyButton.y + 2*(easyButton.height + 10), buttonWidth, buttonHeight)
    quitButton = Button(easyButton.x, easyButton.y + 3*(easyButton.height + 10), buttonWidth, buttonHeight)

    titleImage = pygame.image.load('snakeTitle.png')

    bestScore = 0
    newScore = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONUP:
                if easyButton.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrix(30)
                    newScore = game(gameboard)

                if mediumButton.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrixLevel1(30)
                    newScore = game(gameboard)

                if hardButton.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrixLevel3(30)
                    newScore = game(gameboard)

                if quitButton.isInside(pygame.mouse.get_pos()):
                    pygame.quit()
                    return

        screen.fill(WINDOW_COLOR)
        screen.blit(titleImage, ((WINDOW_WIDTH-300)//2, 40))
        pygame.display.set_caption('Snake')

        if(newScore > bestScore):
            bestScore = newScore

        bestScoreFrame = pygame.Rect(0, WINDOW_HEIGHT - 100, WINDOW_WIDTH, 50)
        printText("Best score: " + str(bestScore), bestScoreFrame, screen)

        easyButton.draw(screen)
        printText("Easy", easyButton, screen)
        mediumButton.draw(screen)
        printText("Medium", mediumButton, screen)
        hardButton.draw(screen)
        printText("Hard", hardButton, screen)
        quitButton.draw(screen)
        printText("Quit", quitButton, screen)

        pygame.display.flip()


showMenu()
