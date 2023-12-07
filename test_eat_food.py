from unittest import TestCase
from unittest.mock import patch
import io
from main import eat_food


class Test(TestCase):
    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_yes_eat(self, mock_output, _):
        my_character = {
            'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 3, 'KEP': 0, 'Level': 'level 1', 'Name': 'Chris'
        }
        level_dict = {
            "level 1": {"KEP_max": 2, "maximum_HP": 5, "name": "Kyoto rookie"},
            "level 2": {"KEP_max": 5, "maximum_HP": 7, "name": "Kyoto skilled novice"},
            "level 3": {"KEP_max": 9999, "maximum_HP": 10, "name": "Kyoto expert"},
        }
        eat_food(my_character, level_dict)
        printed_message = mock_output.getvalue()
        expected_message = 'Oishii! Your Current HP was increased by 1\n'

        self.assertEqual(expected_message, printed_message)
        self.assertEqual(4, my_character['Current HP'])

    @patch('builtins.input', side_effect=['y'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_yes_full(self, mock_output, _):
        my_character = {
            'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 5, 'KEP': 0, 'Level': 'level 1', 'Name': 'Chris'
        }
        level_dict = {
            "level 1": {"KEP_max": 2, "maximum_HP": 5, "name": "Kyoto rookie"},
            "level 2": {"KEP_max": 5, "maximum_HP": 7, "name": "Kyoto skilled novice"},
            "level 3": {"KEP_max": 9999, "maximum_HP": 10, "name": "Kyoto expert"},
        }
        eat_food(my_character, level_dict)
        printed_message = mock_output.getvalue()
        expected_message = 'You are full. Your HP is maximum. You could not eat the food.\n'

        self.assertEqual(expected_message, printed_message)
        self.assertEqual(5, my_character['Current HP'])

    @patch('builtins.input', side_effect=['n'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no(self, mock_output, _):
        my_character = {
            'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 4, 'KEP': 0, 'Level': 'level 2', 'Name': 'Chris'
        }
        level_dict = {
            "level 1": {"KEP_max": 2, "maximum_HP": 5, "name": "Kyoto rookie"},
            "level 2": {"KEP_max": 5, "maximum_HP": 7, "name": "Kyoto skilled novice"},
            "level 3": {"KEP_max": 9999, "maximum_HP": 10, "name": "Kyoto expert"},
        }
        eat_food(my_character, level_dict)
        printed_message = mock_output.getvalue()
        expected_message = 'You did\'t eat anything here.\n'

        self.assertEqual(expected_message, printed_message)
        self.assertEqual(4, my_character['Current HP'])

    @patch('builtins.input', side_effect=['abc', 'n'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_other_string_and_no(self, mock_output, _):
        my_character = {
            'X-coordinate': 3, 'Y-coordinate': 3, 'Current HP': 4, 'KEP': 0, 'Level': 'level 2', 'Name': 'Chris'
        }
        level_dict = {
            "level 1": {"KEP_max": 2, "maximum_HP": 5, "name": "Kyoto rookie"},
            "level 2": {"KEP_max": 5, "maximum_HP": 7, "name": "Kyoto skilled novice"},
            "level 3": {"KEP_max": 9999, "maximum_HP": 10, "name": "Kyoto expert"},
        }
        eat_food(my_character, level_dict)
        printed_message = mock_output.getvalue()
        expected_message = 'You can only type "y" or "n". Try again.\nYou did\'t eat anything here.\n'

        self.assertEqual(expected_message, printed_message)
        self.assertEqual(4, my_character['Current HP'])
