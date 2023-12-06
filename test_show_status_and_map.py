import io
from unittest import TestCase
from unittest.mock import patch

from main import show_status_and_map


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_status_and_map(self, mock_output):
        character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                     'Level': "level 1", 'Name': 'Chris'}
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
        show_status_and_map(character, board)
        the_game_print_this = mock_output.getvalue()
        expected_message = ('\n[Map]\n★★△△△△△△△△△△△△△△△△△△\n△△△△△△△△△△△△△△△△△△△△\n△△△△△△△△△△△△△△##△△△△\n'
                            '△△△△△△##△△△△△△△△△△△△\n△△△△△△△△△△△△△△△△△△△△\n△△△△##△△##△△△△△△△△△△\n△△△△△△##△△△△△△△△##△△\n'
                            '△△△△△△△△△△△△△△△△△△△△\n△△△△△△△△△△△△△△△△△△△△\n△△△△△△△△■■△△△△△△△△△△\n'
                            '\nGoal(Kinkakuji Temple) is ★★.\n\n[Your status]\nName: Chris\nCurrent HP: 3\nKEP: 0\n'
                            'Level: level 1\nLocation:(4, 9) *plotted with ■■\n')
        self.assertEqual(expected_message, the_game_print_this)
