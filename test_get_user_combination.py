import io
from unittest import TestCase
from unittest.mock import patch
from main import get_user_combination


class Test(TestCase):
    @patch('builtins.input', side_effect=['1', '2'])
    def test_valid_input(self, _):
        expected = [1, 2]
        self.assertEqual(expected, get_user_combination())

    @patch('builtins.input', side_effect=['CST', '3', '4'])
    def test_invalid_input_return(self, _):
        expected = [3, 4]
        self.assertEqual(expected, get_user_combination())

    @patch('builtins.input', side_effect=['COMP1510', '1', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_input_print(self, mock_output, _):
        get_user_combination()
        the_game_printed_this = mock_output.getvalue()
        expected_message = 'You can only input numbers in 1-4. Try again.\n'
        self.assertEqual(expected_message, the_game_printed_this)

