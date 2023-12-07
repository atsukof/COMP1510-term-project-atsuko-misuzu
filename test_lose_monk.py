from unittest import TestCase
from main import lose_monk

class Test(TestCase):
    def test_lose_monk(self):
        my_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0, 'Level': 'level 1', 'Name': 'Atsuko'
        }
        lose_monk(my_character)
        self.assertEqual(1, my_character['Current HP'])
