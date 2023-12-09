from main import get_random_quiz
from unittest import TestCase
from unittest.mock import patch


class Test(TestCase):
    @patch('random.randint', return_value=10)
    def test_get_random_quiz(self, _):
        expected = {
            "number": 10,
            "quiz": "What is the highest peak in Japan?",
            "1": "Mount Fuji",
            "2": "Mount Ena",
            "3": "Mount Aso",
            "4": "Mount Baker",
            "ans": "1"
        }
        self.assertEqual(expected, get_random_quiz())

