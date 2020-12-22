import pygame
from random import randint
import src.constants as constants

"""
 todo doc
  
"""


class Field:
    def __init__(self):
        self.obstacles = [[randint(0, 39), randint(0, 39)] for i in range(10)]
        self.obstacles = [pos for pos in self.obstacles if (pos[0] < 15 or pos[0] > 25) or (pos[1] < 15 or pos[1] > 25)]

        self.poison = []
        self.apple = [randint(0, 39), randint(0, 39)]

    def check_event(self, position):
        if position[0] not in range(40) or position[1] not in range(40):
            return 1
        elif position in self.obstacles:
            return 1
        elif position in self.poison:
            self.poison.remove(position)
            return 2
        elif position == self.apple:
            self.apple = [randint(0, 39), randint(0, 39)]
            return 3

    def draw(self, screen):
        if randint(0, 100) < 2:
            self.add_poison()

        for [x, y] in self.obstacles:
            pygame.draw.rect(screen, constants.BROWN, [x * 20, y * 20, constants.BLOCK_SIZE, constants.BLOCK_SIZE])

        for [x, y] in self.poison:
            pygame.draw.rect(screen, constants.LIME, [x * 20, y * 20, constants.BLOCK_SIZE, constants.BLOCK_SIZE])

        pygame.draw.rect(screen, constants.RED,
                         [self.apple[0] * 20, self.apple[1] * 20, constants.BLOCK_SIZE, constants.BLOCK_SIZE])

    def add_poison(self):
        if len(self.poison) < 3:
            self.poison.append([randint(0, 39), randint(0, 39)])
