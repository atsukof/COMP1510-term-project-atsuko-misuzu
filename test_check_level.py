from unittest import TestCase
from main import check_level
from unittest.mock import patch
import io


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_before_level_1_after_level_1(self, mock_output):
        my_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0, 'Level': 'level 1', 'Name': 'Atsuko'
        }
        level_dict = {
            'level 1': {'KEP_max': 2, 'maximum_HP': 5, 'name': 'Kyoto rookie'},
            'level 2': {'KEP_max': 5, 'maximum_HP': 7, 'name': 'Kyoto skilled novice'},
            'level 3': {'KEP_max': 9999, 'maximum_HP': 10, 'name': 'Kyoto expert'}
        }

        check_level(my_character, level_dict)
        printed_message = mock_output.getvalue()
        expected_message = 'Now you are Kyoto rookie (level 1).\n'
        expected_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 0, 'Level': 'level 1', 'Name': 'Atsuko'
        }
        self.assertEqual(expected_message, printed_message)
        self.assertEqual(expected_character, my_character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_before_level_1_after_level_2(self, mock_output):
        my_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 3, 'Level': 'level 1', 'Name': 'Atsuko'
        }
        level_dict = {
            'level 1': {'KEP_max': 2, 'maximum_HP': 5, 'name': 'Kyoto rookie'},
            'level 2': {'KEP_max': 5, 'maximum_HP': 7, 'name': 'Kyoto skilled novice'},
            'level 3': {'KEP_max': 9999, 'maximum_HP': 10, 'name': 'Kyoto expert'}
        }
        check_level(my_character, level_dict)
        printed_message = mock_output.getvalue()
        expected_message = 'Now you are Kyoto skilled novice (level 2).\n'
        expected_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 3, 'Level': 'level 2', 'Name': 'Atsuko'
        }
        self.assertEqual(expected_message, printed_message)
        self.assertEqual(expected_character, my_character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_before_level_2_after_level_2(self, mock_output):
        my_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 4, 'Level': 'level 2', 'Name': 'Atsuko'
        }
        level_dict = {
            'level 1': {'KEP_max': 2, 'maximum_HP': 5, 'name': 'Kyoto rookie'},
            'level 2': {'KEP_max': 5, 'maximum_HP': 7, 'name': 'Kyoto skilled novice'},
            'level 3': {'KEP_max': 9999, 'maximum_HP': 10, 'name': 'Kyoto expert'}
        }
        check_level(my_character, level_dict)
        printed_message = mock_output.getvalue()
        expected_message = 'Now you are Kyoto skilled novice (level 2).\n'
        expected_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 4, 'Level': 'level 2', 'Name': 'Atsuko'
        }
        self.assertEqual(expected_message, printed_message)
        self.assertEqual(expected_character, my_character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_before_level_2_after_level_3(self, mock_output):
        my_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 6, 'Level': 'level 2', 'Name': 'Atsuko'
        }
        level_dict = {
            'level 1': {'KEP_max': 2, 'maximum_HP': 5, 'name': 'Kyoto rookie'},
            'level 2': {'KEP_max': 5, 'maximum_HP': 7, 'name': 'Kyoto skilled novice'},
            'level 3': {'KEP_max': 9999, 'maximum_HP': 10, 'name': 'Kyoto expert'}
        }
        check_level(my_character, level_dict)
        printed_message = mock_output.getvalue()
        expected_message = ('You are Kyoto expert (level 3) now! '
                            'You\'re ready to fight with monk at Kinkakuji Temple.\n')
        expected_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 6, 'Level': 'level 3', 'Name': 'Atsuko'
        }
        self.assertEqual(expected_message, printed_message)
        self.assertEqual(expected_character, my_character)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_before_level_3_after_level_3(self, mock_output):
        my_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 7, 'Level': 'level 3', 'Name': 'Atsuko'
        }
        level_dict = {
            'level 1': {'KEP_max': 2, 'maximum_HP': 5, 'name': 'Kyoto rookie'},
            'level 2': {'KEP_max': 5, 'maximum_HP': 7, 'name': 'Kyoto skilled novice'},
            'level 3': {'KEP_max': 9999, 'maximum_HP': 10, 'name': 'Kyoto expert'}
        }
        check_level(my_character, level_dict)
        printed_message = mock_output.getvalue()
        expected_message = ('You are Kyoto expert (level 3) now! '
                            'You\'re ready to fight with monk at Kinkakuji Temple.\n')
        expected_character = {
            'X-coordinate': 4, 'Y-coordinate': 9, 'Current HP': 3, 'KEP': 7, 'Level': 'level 3', 'Name': 'Atsuko'
        }
        self.assertEqual(expected_message, printed_message)
        self.assertEqual(expected_character, my_character)
