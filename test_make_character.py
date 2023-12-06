import io
from unittest import TestCase
from unittest.mock import patch
from main import make_character


class Test(TestCase):
    @patch('builtins.input', side_effect=['Chris', 'y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_1_yes_print(self, mock_output, _):
        make_character()
        the_game_print_this = mock_output.getvalue()
        expected_message = 'Hello Chris, let\'s explore Kyoto with us!\n'
        self.assertEqual(expected_message, the_game_print_this)

    @patch('builtins.input', side_effect=['Chris', 'y'])
    def test_input_1_yes_return(self, _):
        expected_return = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                           'Level': "level 1", 'Name': 'Chris'}
        self.assertEqual(expected_return, make_character())

    @patch('builtins.input', side_effect=['Chris', 'n', 'Atsuko', 'y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_1_no_input_2_yes_print(self, mock_output, _):
        make_character()
        the_game_print_this = mock_output.getvalue()
        expected_message = 'Hello Atsuko, let\'s explore Kyoto with us!\n'
        self.assertEqual(expected_message, the_game_print_this)

    @patch('builtins.input', side_effect=['Chris', 'n', 'Atsuko', 'y'])
    def test_input_1_no_input_2_yes_return(self, _):
        expected_return = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                           'Level': "level 1", 'Name': 'Atsuko'}
        self.assertEqual(expected_return, make_character())

    @patch('builtins.input', side_effect=['Chris', 'abc', 'Misuzu', 'y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_1_random_word_input_2_yes_print(self, mock_output, _):
        make_character()
        the_game_print_this = mock_output.getvalue()
        expected_message = ('Your input is not valid, try again.\n'
                            'Hello Misuzu, let\'s explore Kyoto with us!\n')
        self.assertEqual(expected_message, the_game_print_this)

    @patch('builtins.input', side_effect=['Chris', 'abc', 'Misuzu', 'y'])
    def test_input_1_random_word_input_2_yes_return(self, _):
        expected_return = {'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0,
                           'Level': "level 1", 'Name': 'Misuzu'}
        self.assertEqual(expected_return, make_character())
