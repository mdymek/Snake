"""
 Some unit tests for the Field class.
"""

import unittest
from src.field import Field  # pylint: disable=import-error


class FieldTest(unittest.TestCase):
    """ Test case connected to the Field class. """

    def test_create(self):
        """ Test field creation. """
        field = Field()
        self.assertIsInstance(field, Field)

    def test_check_event(self):
        """ Test event detection - obstacle hits, poisoning and eating."""
        field = Field()

        # out of borders
        self.assertEqual(field.check_event([-1, 1]), Field.Event.OBSTACLE_HIT)
        self.assertEqual(field.check_event([40, 1]), Field.Event.OBSTACLE_HIT)
        self.assertEqual(field.check_event([1, -1]), Field.Event.OBSTACLE_HIT)
        self.assertEqual(field.check_event([1, 40]), Field.Event.OBSTACLE_HIT)

        obj_pos = [1, 1]
        field.obstacles.append(obj_pos)
        self.assertEqual(field.check_event(obj_pos), Field.Event.OBSTACLE_HIT)
        field.obstacles.pop()

        field.poison.append(obj_pos)
        self.assertEqual(field.check_event(obj_pos), Field.Event.POISON)

        field.apple = obj_pos
        self.assertEqual(field.check_event(obj_pos), Field.Event.FOOD)

    def test_add_poison(self):
        """ Test adding poison to the field. """
        field = Field()

        self.assertEqual(len(field.poison), 0)

        field.add_poison()
        self.assertEqual(len(field.poison), 1)

        field.add_poison()
        self.assertEqual(len(field.poison), 2)

        field.add_poison()
        self.assertEqual(len(field.poison), 3)

        field.add_poison()
        self.assertEqual(len(field.poison), 3)


if __name__ == '__main__':
    unittest.main()
