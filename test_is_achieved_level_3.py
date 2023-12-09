from unittest import TestCase
from main import is_achieved_level_3


class Test(TestCase):
    def test_level_3(self):
        user_character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 3, 'KEP': 6, 'Name': 'Chris'}
        self.assertEqual(True, is_achieved_level_3(user_character))

    def test_not_level_3(self):
        user_character = {'X-coordinate': 5, 'Y-coordinate': 5, 'Current HP': 4, 'KEP': 5, 'Name': 'Chris'}
        self.assertEqual(False, is_achieved_level_3(user_character))
