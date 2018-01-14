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
    startButton = Button((WINDOW_WIDTH - buttonWidth) // 2, (WINDOW_HEIGHT - buttonHeight) // 3 + 20, buttonWidth, buttonHeight, "Start Game")
    map1Button = Button(startButton.x, startButton.y + startButton.height + 10, buttonWidth, buttonHeight, "Map 1")
    map2Button = Button(startButton.x, startButton.y + 2*(startButton.height + 10), buttonWidth, buttonHeight, "Map 2")
    map3Button = Button(startButton.x, startButton.y + 3*(startButton.height + 10), buttonWidth, buttonHeight, "Map 3")
    quitButton = Button(startButton.x, startButton.y + 4*(startButton.height + 10), buttonWidth, buttonHeight, "Quit")

    titleImage = pygame.image.load('snakeTitle.png')

    bestScore = getBestScore()
    newScore = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.MOUSEBUTTONUP:
                if startButton.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrix(30)
                    newScore = game(gameboard)

                elif map1Button.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrixLevel1(30)
                    newScore = game(gameboard)

                elif map2Button.isInside(pygame.mouse.get_pos()):
                    gameboard = buildSquareMatrixLevel2(30)
                    newScore = game(gameboard)

                elif map3Button.isInside(pygame.mouse.get_pos()):
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

        startButton.draw(screen)
        map1Button.draw(screen)
        map2Button.draw(screen)
        map3Button.draw(screen)
        quitButton.draw(screen)
        getBestScore()
        pygame.display.flip()


showMenu()
