from unittest import TestCase
from main import is_alive


class Test(TestCase):
    def test_is_alive_hp_1(self):
        my_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 1, 'KEP': 0, 'Level': 'level 1', 'Name': 'Atsuko'
        }
        self.assertEqual(True, is_alive(my_character))

    def test_is_alive_hp_5(self):
        my_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 5, 'KEP': 0, 'Level': 'level 1', 'Name': 'Atsuko'
        }
        self.assertEqual(True, is_alive(my_character))

    def test_is_alive_hp_0(self):
        my_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 0, 'KEP': 0, 'Level': 'level 1', 'Name': 'Atsuko'
        }
        self.assertEqual(False, is_alive(my_character))

    def test_is_alive_hp_negative_1(self):
        my_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': -1, 'KEP': 0, 'Level': 'level 1', 'Name': 'Atsuko'
        }
        self.assertEqual(False, is_alive(my_character))
