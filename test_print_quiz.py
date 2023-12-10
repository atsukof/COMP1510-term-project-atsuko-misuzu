import io
from unittest import TestCase
from unittest.mock import patch
from main import print_quiz


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_quiz(self, mock_output):
        quiz_dictionary = {
            "number": 10,
            "quiz": "What is the highest peak in Japan?",
            "1": "Mount Fuji",
            "2": "Mount Ena",
            "3": "Mount Aso",
            "4": "Mount Baker",
            "ans": "1"
          }
        print_quiz(quiz_dictionary)
        quiz_printed = mock_output.getvalue()
        expected_message = ('What is the highest peak in Japan?\n'
                            '1. Mount Fuji\n'
                            '2. Mount Ena\n'
                            '3. Mount Aso\n'
                            '4. Mount Baker\n')
        self.assertEqual(expected_message, quiz_printed)
