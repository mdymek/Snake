from collections import deque

import pygame

"""
 todo doc

"""

BLACK = (0, 0, 0)
snake_size = 20


class Snake:

    def __init__(self):
        # 0 - 39
        self.body = deque([[20, 20]])
        self.direction = pygame.K_PAUSE
        self.hungry = True

    def draw(self, screen):
        x_change = 0
        y_change = 0
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
            pygame.draw.rect(screen, BLACK, [x * 20, y * 20, snake_size, snake_size])

        return head

    def move(self, direction):
        if direction in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
            self.direction = direction

        # todo delete
        if direction is pygame.K_SPACE:
            self.eat()

    def eat(self):
        self.hungry = False

    def poison(self):
        self.body.pop()
        return len(self.body) == 0

    def crash(self, position):
        return self.body.count(position) > 1
