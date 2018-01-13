from Renderer import *
from Snake import *
from Apple import *
from Button import *
from PauseGame import *
from BestScore import *

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
            if event.type == pygame.K_p:
                pauseGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pauseGame()
                else:
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

        pauseFrame = pygame.Rect(0, WINDOW_HEIGHT - 50, WINDOW_WIDTH, 50)
        scoreFrame = pygame.Rect(0, WINDOW_HEIGHT-90, WINDOW_WIDTH, 50)
        printText("Score: "+str(score), scoreFrame, screen, 17)
        printText("Press P to pause", pauseFrame, screen, 16)

        pygame.display.flip()

        clock.tick(10)


buttonWidth = WINDOW_WIDTH // 3
buttonHeight = WINDOW_HEIGHT // 15

def showMenu():
    easyButton = Button((WINDOW_WIDTH - buttonWidth) // 2, (WINDOW_HEIGHT - buttonHeight) // 3 + 20, buttonWidth, buttonHeight, "Easy")
    mediumButton = Button(easyButton.x, easyButton.y + easyButton.height + 10, buttonWidth, buttonHeight, "Medium")
    hardButton = Button(easyButton.x, easyButton.y + 2*(easyButton.height + 10), buttonWidth, buttonHeight, "Hard")
    quitButton = Button(easyButton.x, easyButton.y + 3*(easyButton.height + 10), buttonWidth, buttonHeight, "Quit")

    titleImage = pygame.image.load('snakeTitle.png')

    bestScore = getBestScore()
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

                elif mediumButton.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrixLevel1(30)
                    newScore = game(gameboard)

                elif hardButton.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrixLevel3(30)
                    newScore = game(gameboard)

                elif quitButton.isInside(pygame.mouse.get_pos()):
                    pygame.quit()
                    return

                if (newScore > int(bestScore)):
                    bestScore = newScore
                    updateBestScore((bestScore))

        screen.fill(WINDOW_COLOR)
        screen.blit(titleImage, ((WINDOW_WIDTH-300)//2, 40))
        pygame.display.set_caption('Snake')



        bestScoreFrame = pygame.Rect(0, WINDOW_HEIGHT - 100, WINDOW_WIDTH, 50)
        printText("Best score: " + str(bestScore), bestScoreFrame, screen, 17)

        easyButton.draw(screen)
        mediumButton.draw(screen)
        hardButton.draw(screen)
        quitButton.draw(screen)
        getBestScore()
        pygame.display.flip()


showMenu()
