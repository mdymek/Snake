"""
 Some unit tests for the class Snake.
"""

import unittest
from src.snake import Snake  # pylint: disable=import-error


class SnakeTest(unittest.TestCase):
    """ Test case tied to the Snake class. """

    def test_create(self):
        """ Test snake creation. """
        snake = Snake()
        self.assertIsInstance(snake, Snake)
        self.assertEqual(len(snake.body), 1)

    def test_eat(self):
        """ Test snake's not hungry if he's eaten. """
        snake = Snake()
        self.assertTrue(snake.hungry)
        snake.eat()
        self.assertFalse(snake.hungry)

    def test_poison(self):
        """ Test poison makes snake shorter. """
        snake = Snake()
        self.assertEqual(len(snake.body), 1)
        snake.poison()
        self.assertEqual(len(snake.body), 0)

    def test_is_dead(self):
        """ Test bodyless snake is dead. """
        snake = Snake()
        snake.body = []
        self.assertTrue(snake.is_dead())

    def test_crash(self):
        """ Test detecting self-crash. """
        snake = Snake()
        snake.body.append(list(snake.body[0]))
        self.assertTrue(snake.crash(list(snake.body[0])))


if __name__ == '__main__':
    unittest.main()
