from MatrixBuilder import MapState
import pygame
from enum import Enum

class Point:
    def __init__(self, row, column):
        self.row = row
        self.column = column

class Snake:
    def __init__(self, matrix):
        centerRow = len(matrix) // 2
        centerColumn = len(matrix[centerRow]) // 2

        matrix[centerRow][centerColumn] = MapState.SNAKE
        matrix[centerRow][centerColumn+1] = MapState.SNAKE
        head = Point(centerRow, centerColumn)
        tail = Point(centerRow, centerColumn+1)
        self.matrix = matrix
        self.currentDirection = pygame.K_LEFT
        self.body = [head, tail]
        self.currentScore = 0


    def setDirection(self, key):
        if key != pygame.K_LEFT and key != pygame.K_RIGHT and key != pygame.K_UP and key != pygame.K_DOWN:
            return
        elif key == pygame.K_UP and self.currentDirection == pygame.K_DOWN:
            return
        elif key == pygame.K_DOWN and self.currentDirection == pygame.K_UP:
            return
        elif key == pygame.K_LEFT and self.currentDirection == pygame.K_RIGHT:
            return
        elif key == pygame.K_RIGHT and self.currentDirection == pygame.K_LEFT:
            return
        else:
            self.currentDirection = key

    def move(self):
        if self.currentDirection == pygame.K_LEFT:
            self.body.insert(0, Point(self.body[0].row, self.body[0].column-1))

        elif self.currentDirection == pygame.K_RIGHT:
            self.body.insert(0, Point(self.body[0].row, self.body[0].column + 1))

        elif self.currentDirection == pygame.K_UP:
            self.body.insert(0, Point(self.body[0].row-1, self.body[0].column))

        elif self.currentDirection == pygame.K_DOWN:
            self.body.insert(0, Point(self.body[0].row+1, self.body[0].column))

        if self.matrix[self.body[0].row][self.body[0].column] == MapState.WALL or self.matrix[self.body[0].row][self.body[0].column] == MapState.SNAKE:
            return MoveResult.isDead


        if self.matrix[self.body[0].row][self.body[0].column] != MapState.APPLE:
            self.matrix[self.body[0].row][self.body[0].column] = MapState.SNAKE
            self.matrix[self.body[-1].row][self.body[-1].column] = MapState.EMPTY
            del self.body[-1]

        else:
            self.matrix[self.body[0].row][self.body[0].column] = MapState.SNAKE
            self.currentScore += 1
            return MoveResult.appleEaten



class MoveResult(Enum):
    appleEaten = 1
    isDead = 3