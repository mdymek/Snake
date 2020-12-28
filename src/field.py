"""
 Class representing the grassy field where our little python searches for his food,
"""
from enum import Enum
from random import randint
import pygame
import src.constants as consts  # pylint: disable=import-error


class Field:
    """ Field renders obstacles, food and poison for the snake. """

    def __init__(self):
        self.obstacles = [[randint(0, 39), randint(0, 39)] for i in range(10)]
        self.obstacles = [pos for pos in self.obstacles
                          if (pos[0] < 15 or pos[0] > 25) or (pos[1] < 15 or pos[1] > 25)]

        self.poison = []
        self.apple = [randint(0, 39), randint(0, 39)]

    class Event(Enum):
        """ Class representing possible events triggered by snake movement. """
        OBSTACLE_HIT = 1
        POISON = 2
        FOOD = 3

    def check_event(self, position):
        """ Check if snake movement triggered an event. """
        if position[0] not in range(40) or position[1] not in range(40):
            return self.Event.OBSTACLE_HIT

        if position in self.obstacles:
            return self.Event.OBSTACLE_HIT

        if position in self.poison:
            self.poison.remove(position)
            return self.Event.POISON

        if position == self.apple:
            self.apple = [randint(0, 39), randint(0, 39)]
            return self.Event.FOOD

        return None

    def draw(self, screen):
        """ Draw all the objects on the map. """
        screen.fill(consts.GREEN)

        if randint(0, 100) < 2:
            self.add_poison()

        for [pos_x, pos_y] in self.obstacles:
            pygame.draw.rect(screen, consts.BROWN,
                             [pos_x * consts.BLOCK_SIZE, pos_y * consts.BLOCK_SIZE,
                              consts.BLOCK_SIZE, consts.BLOCK_SIZE])

        for [pos_x, pos_y] in self.poison:
            pygame.draw.rect(screen, consts.LIME,
                             [pos_x * consts.BLOCK_SIZE, pos_y * consts.BLOCK_SIZE,
                              consts.BLOCK_SIZE, consts.BLOCK_SIZE])

        pygame.draw.rect(screen, consts.RED,
                         [self.apple[0] * consts.BLOCK_SIZE, self.apple[1] * consts.BLOCK_SIZE,
                          consts.BLOCK_SIZE, consts.BLOCK_SIZE])

    def add_poison(self):
        """ Semi-randombly spawns poisons unless there's already too much of it."""
        if len(self.poison) < 3:
            pos = [randint(0, 39), randint(0, 39)]
            while pos == self.apple or pos in self.obstacles or pos in self.poison:
                pos = [randint(0, 39), randint(0, 39)]
            self.poison.append(pos)
