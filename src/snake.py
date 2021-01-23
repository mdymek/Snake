"""
 Class representing our little adventurous python.

"""

from collections import deque
import pygame
import src.constants as consts  # pylint: disable=import-error


class Snake:
    """
    The snake can move, eat and be poisoned. It's represented by a deque of body part coordinates
    ranging from 0 to 39.
    """

    def __init__(self):
        self.body = deque([[20, 20]])
        self.direction = None
        self.hungry = True

    def draw(self, screen):
        """ Move the snake and draw all of its body parts. Return the new position of its head. """
        x_change, y_change = 0, 0

        if self.direction == pygame.K_LEFT:  # pylint: disable=no-member
            x_change = -1
        elif self.direction == pygame.K_RIGHT:  # pylint: disable=no-member
            x_change = 1
        elif self.direction == pygame.K_UP:  # pylint: disable=no-member
            y_change = -1
        elif self.direction == pygame.K_DOWN:  # pylint: disable=no-member
            y_change = 1

        head = [x_change, y_change]
        head[0] += self.body[0][0]
        head[1] += self.body[0][1]
        self.body.appendleft(head)

        if self.hungry:
            self.body.pop()
        self.hungry = True

        for [pos_x, pos_y] in self.body:
            pygame.draw.rect(screen, consts.BLACK,
                             [pos_x * consts.BLOCK_SIZE, pos_y * consts.BLOCK_SIZE,
                              consts.BLOCK_SIZE, consts.BLOCK_SIZE])

        return head

    def opposite_direction(self):
        """ Returns direction opposite to the one that snakes going in. """
        opposites = {
            pygame.K_LEFT: pygame.K_RIGHT,  # pylint: disable=no-member
            pygame.K_RIGHT: pygame.K_LEFT,  # pylint: disable=no-member
            pygame.K_UP: pygame.K_DOWN,  # pylint: disable=no-member
            pygame.K_DOWN: pygame.K_UP  # pylint: disable=no-member
        }
        return opposites[self.direction]

    def move(self, direction):
        """ Set snakes' direction based on users' input. """
        if direction in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:  # pylint: disable=no-member
            if not self.direction or direction != self.opposite_direction():
                self.direction = direction

    def eat(self):
        """ When snake eats, its not hungry and elongates by one block when moving. """
        self.hungry = False
        consts.TICKS_PER_MIN += 2

    def poison(self):
        """ Snake shortens by one block when he eats poison. """
        self.body.pop()

    def is_dead(self):
        """ Snake is dead when completely vanished from the poison. Poor him! """
        return len(self.body) == 0

    def crash(self, position):
        """ Checks whether the snake crashed into himself. """
        return self.body.count(position) > 1
