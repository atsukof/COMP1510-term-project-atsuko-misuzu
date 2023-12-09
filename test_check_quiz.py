from unittest import TestCase
from unittest.mock import patch
from main import check_quiz


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_random_1(self, _):
        self.assertEqual(True, check_quiz())

    @patch('random.randint', return_value=3)
    def test_random_3(self, _):
        self.assertEqual(True, check_quiz())

    @patch('random.randint', return_value=10)
    def test_random_10(self, _):
        self.assertEqual(False, check_quiz())
        