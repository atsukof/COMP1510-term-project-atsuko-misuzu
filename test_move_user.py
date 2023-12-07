from unittest import TestCase
from main import move_user


class Test(TestCase):
    def test_move_to_north(self):
        character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                     'Level': "level 1", 'Name': 'Chris'}
        move_user(character, 1)
        expected = {'X-coordinate': 4, 'Y-coordinate': 8, 'Current HP': 3, 'KEP': 0,
                    'Level': "level 1", 'Name': 'Chris'}
        self.assertEqual(expected, character)

    def test_move_to_east(self):
        character = {'X-coordinate': 4, 'Y-coordinate': 8, 'Current HP': 3, 'KEP': 0,
                     'Level': "level 1", 'Name': 'Atsuko'}
        move_user(character, 2)
        expected = {'X-coordinate': 5, 'Y-coordinate': 8, 'Current HP': 3, 'KEP': 0,
                    'Level': "level 1", 'Name': 'Atsuko'}
        self.assertEqual(expected, character)

    def test_move_to_south(self):
        character = {'X-coordinate': 5, 'Y-coordinate': 8, 'Current HP': 3, 'KEP': 0,
                     'Level': "level 1", 'Name': 'Misuzu'}
        move_user(character, 3)
        expected = {'X-coordinate': 5, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                    'Level': "level 1", 'Name': 'Misuzu'}
        self.assertEqual(expected, character)

    def test_move_to_west(self):
        character = {'X-coordinate': 5, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                     'Level': "level 1", 'Name': 'Chris'}
        move_user(character, 4)
        expected = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                    'Level': "level 1", 'Name': 'Chris'}
        self.assertEqual(expected, character)
