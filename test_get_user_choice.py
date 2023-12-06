import io
from unittest import TestCase
from unittest.mock import patch
from main import get_user_choice


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_input_1_valid_return(self, _):
        self.assertEqual(1, get_user_choice())

    @patch('builtins.input', side_effect=['BCIT', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_1_invalid_input_2_valid_print(self, mock_output, _):
        get_user_choice()
        the_game_print_this = mock_output.getvalue()
        expected_message = 'You need to choose from the list!\n'
        self.assertEqual(expected_message, the_game_print_this)

    @patch('builtins.input', side_effect=['BCIT', '1'])
    def test_input_1_invalid_input_2_valid_return(self, _):
        self.assertEqual(1, get_user_choice())
