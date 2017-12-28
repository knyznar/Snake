from MatrixBuilder import MapState
import pygame

class Point:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Snake:
    def __init__(self, matrix):
        centerRow = len(matrix) // 2
        centerColumn = len(matrix[centerRow]) // 2

        matrix[centerRow][centerColumn] = MapState.SNAKE
        self.head = Point(centerRow, centerColumn)
        self.matrix = matrix
        self.lastDirection = pygame.K_LEFT

    def setDirection(self, key):
        if key != pygame.K_LEFT and key != pygame.K_RIGHT and key != pygame.K_UP and key != pygame.K_DOWN:
            return
        else:
            self.lastDirection = key

    def move(self):
        if self.lastDirection == pygame.K_LEFT:
            self.head.column -= 1
            self.matrix[self.head.row][self.head.column] = MapState.SNAKE
        elif self.lastDirection == pygame.K_RIGHT:
            self.head.column += 1
            self.matrix[self.head.row][self.head.column] = MapState.SNAKE
        elif self.lastDirection == pygame.K_UP:
            self.head.row -= 1
            self.matrix[self.head.row][self.head.column] = MapState.SNAKE
        elif self.lastDirection == pygame.K_DOWN:
            self.head.row += 1
            self.matrix[self.head.row][self.head.column] = MapState.SNAKE

