from collections import deque

import src.constants as constants

import pygame

"""
 todo doc

"""


class Snake:

    def __init__(self):
        # 0 - 39
        self.body = deque([[20, 20]])
        self.direction = None
        self.hungry = True

    def draw(self, screen):
        x_change, y_change = 0, 0

        if self.direction == pygame.K_LEFT:
            x_change = -1
        elif self.direction == pygame.K_RIGHT:
            x_change = 1
        elif self.direction == pygame.K_UP:
            y_change = -1
        elif self.direction == pygame.K_DOWN:
            y_change = 1

        head = [x_change, y_change]
        head[0] += self.body[0][0]
        head[1] += self.body[0][1]
        self.body.appendleft(head)

        if self.hungry:
            self.body.pop()
        self.hungry = True

        for [x, y] in self.body:
            pygame.draw.rect(screen, constants.BLACK, [x * 20, y * 20, constants.BLOCK_SIZE, constants.BLOCK_SIZE])

        return head

    def opposite_direction(self):
        opposites = {
            pygame.K_LEFT: pygame.K_RIGHT,
            pygame.K_RIGHT: pygame.K_LEFT,
            pygame.K_UP: pygame.K_DOWN,
            pygame.K_DOWN: pygame.K_UP
        }
        return opposites[self.direction]

    def move(self, direction):
        if direction in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
            if not self.direction or direction != self.opposite_direction():
                self.direction = direction

    def eat(self):
        self.hungry = False

    def poison(self):
        self.body.pop()
        return len(self.body) == 0

    def crash(self, position):
        return self.body.count(position) > 1
