from random import randint

import pygame

BROWN = (102, 51, 00)
LIME = (0, 255, 0)
RED = (255, 0, 0)

block_size = 20


class Field:
    def __init__(self):
        self.obstacles = []
        self.poison = []
        self.apple = [randint(0, 39), randint(0, 39)]

    def check_event(self, position):
        if position[0] not in range(40) or position[1] not in range(40):
            return 1
        elif position in self.obstacles:
            return 1
        elif position in self.poison:
            return 2
        elif position == self.apple:
            self.apple = [randint(0, 39), randint(0, 39)]
            return 3

    def draw(self, screen):
        for [x, y] in self.obstacles:
            pygame.draw.rect(screen, BROWN, [x * 20, y * 20, block_size, block_size])

        for [x, y] in self.poison:
            pygame.draw.rect(screen, LIME, [x * 20, y * 20, block_size, block_size])

        pygame.draw.rect(screen, RED, [self.apple[0] * 20, self.apple[1] * 20, block_size, block_size])

    def add_poison(self):
        if len(self.poison) < 3:
            self.poison.append([randint(0, 39), randint(0, 39)])
