from unittest import TestCase
from main import is_kinkakuji


class Test(TestCase):
    def test_character_is_kinkakuji(self):
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 4, 'KEP': 7,
                     'Level': "level 3", 'Name': 'Chris'}
        board = {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street',
                 (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street',
                 (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street',
                 (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street',
                 (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street',
                 (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street',
                 (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street',
                 (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street',
                 (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace',
                 (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market',
                 (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street',
                 (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street',
                 (4, 5): 'Ueshima Coffee', (4, 6): 'Random Street', (4, 7): 'Random Street',
                 (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street',
                 (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street',
                 (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street',
                 (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street',
                 (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street',
                 (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street',
                 (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street',
                 (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street',
                 (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street',
                 (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street',
                 (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street',
                 (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street',
                 (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street',
                 (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
        expected = True
        self.assertEqual(expected, is_kinkakuji(character, board))

    def test_character_is_not_kinkakuji(self):
        character = {'X-coordinate': 4, 'Y-coordinate': 5, 'Current HP': 3, 'KEP': 5,
                     'Level': "level 2", 'Name': 'Chris'}
        board = {(0, 0): 'Kinkakuji Temple', (0, 1): 'Random Street', (0, 2): 'Random Street',
                 (0, 3): 'Random Street', (0, 4): 'Random Street', (0, 5): 'Random Street', (0, 6): 'Random Street',
                 (0, 7): 'Random Street', (0, 8): 'Random Street', (0, 9): 'Random Street', (1, 0): 'Random Street',
                 (1, 1): 'Random Street', (1, 2): 'Random Street', (1, 3): 'Random Street', (1, 4): 'Random Street',
                 (1, 5): 'Random Street', (1, 6): 'Random Street', (1, 7): 'Random Street', (1, 8): 'Random Street',
                 (1, 9): 'Random Street', (2, 0): 'Random Street', (2, 1): 'Random Street', (2, 2): 'Random Street',
                 (2, 3): 'Random Street', (2, 4): 'Random Street', (2, 5): 'Nijojo Castle', (2, 6): 'Random Street',
                 (2, 7): 'Random Street', (2, 8): 'Random Street', (2, 9): 'Random Street', (3, 0): 'Random Street',
                 (3, 1): 'Random Street', (3, 2): 'Random Street', (3, 3): 'Kyoto Imperial Palace',
                 (3, 4): 'Random Street', (3, 5): 'Random Street', (3, 6): 'Nishiki Market',
                 (3, 7): 'Random Street', (3, 8): 'Random Street', (3, 9): 'Random Street', (4, 0): 'Random Street',
                 (4, 1): 'Random Street', (4, 2): 'Random Street', (4, 3): 'Random Street', (4, 4): 'Random Street',
                 (4, 5): 'Ueshima Coffee', (4, 6): 'Random Street', (4, 7): 'Random Street',
                 (4, 8): 'Random Street', (4, 9): 'Kyoto Station', (5, 0): 'Random Street', (5, 1): 'Random Street',
                 (5, 2): 'Random Street', (5, 3): 'Random Street', (5, 4): 'Random Street', (5, 5): 'Random Street',
                 (5, 6): 'Random Street', (5, 7): 'Random Street', (5, 8): 'Random Street', (5, 9): 'Random Street',
                 (6, 0): 'Random Street', (6, 1): 'Random Street', (6, 2): 'Random Street', (6, 3): 'Random Street',
                 (6, 4): 'Random Street', (6, 5): 'Random Street', (6, 6): 'Random Street', (6, 7): 'Random Street',
                 (6, 8): 'Random Street', (6, 9): 'Random Street', (7, 0): 'Random Street', (7, 1): 'Random Street',
                 (7, 2): 'Kyoto University', (7, 3): 'Random Street', (7, 4): 'Random Street',
                 (7, 5): 'Random Street', (7, 6): 'Random Street', (7, 7): 'Random Street', (7, 8): 'Random Street',
                 (7, 9): 'Random Street', (8, 0): 'Random Street', (8, 1): 'Random Street', (8, 2): 'Random Street',
                 (8, 3): 'Random Street', (8, 4): 'Random Street', (8, 5): 'Random Street',
                 (8, 6): 'Kiyomizudera Temple', (8, 7): 'Random Street', (8, 8): 'Random Street',
                 (8, 9): 'Random Street', (9, 0): 'Random Street', (9, 1): 'Random Street', (9, 2): 'Random Street',
                 (9, 3): 'Random Street', (9, 4): 'Random Street', (9, 5): 'Random Street', (9, 6): 'Random Street',
                 (9, 7): 'Random Street', (9, 8): 'Random Street', (9, 9): 'Random Street'}
        expected = False
        self.assertEqual(expected, is_kinkakuji(character, board))
