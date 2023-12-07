import io
from unittest import TestCase
from unittest.mock import patch
from main import play_quiz


class Test(TestCase):
    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_correct_answer_print(self, mock_output, _, __):
        character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                     'Level': "level 1", 'Name': 'Chris'}
        play_quiz(character)
        the_game_printed_this = mock_output.getvalue()
        expected_message = 'You are correct, your KEP was increased by 1\n'
        self.assertIn(expected_message, the_game_printed_this)

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', return_value=1)
    def test_correct_answer_character(self, _, __):
        character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                     'Level': "level 1", 'Name': 'Chris'}
        play_quiz(character)
        expected = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 1,
                    'Level': "level 1", 'Name': 'Chris'}
        self.assertEqual(expected, character)

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', return_value=0)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_wrong_answer_print(self, mock_output, _, __):
        character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                     'Level': "level 1", 'Name': 'Misuzu'}
        play_quiz(character)
        the_game_printed_this = mock_output.getvalue()
        expected_message = 'You are wrong, your HP was decreased by 1\n'
        self.assertIn(expected_message, the_game_printed_this)

    @patch('builtins.input', side_effect=['2'])
    @patch('random.randint', return_value=0)
    def test_wrong_answer_character(self, _, __):
        character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                     'Level': "level 1", 'Name': 'Misuzu'}
        play_quiz(character)
        expected = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 2, 'KEP': 0,
                    'Level': "level 1", 'Name': 'Misuzu'}
        self.assertEqual(expected, character)

    @patch('builtins.input', side_effect=['konnichiwa', '3'])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_first_invalid_answer_second_correct_answer(self, mock_output, _, __):
        character = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                     'Level': "level 1", 'Name': 'Atsuko'}
        play_quiz(character)
        the_game_printed_this = mock_output.getvalue()
        expected_message = ('Something is wrong... Enter your answer again.\n'
                            'You are correct, your KEP was increased by 1\n')
        self.assertIn(expected_message, the_game_printed_this)
