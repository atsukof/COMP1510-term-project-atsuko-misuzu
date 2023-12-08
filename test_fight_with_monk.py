import io
from unittest import TestCase
from unittest.mock import patch
from main import fight_with_monk

class Test(TestCase):
    @patch('builtins.input', side_effect=['1', '2'])
    @patch('random.randint', return_value=0)
    def test_user_won(self, _, __):
        self.assertEqual(True, fight_with_monk())

    @patch('builtins.input', side_effect=['1', '2'])
    @patch('random.randint', return_value=1)
    def test_user_lose(self, _, __):
        self.assertEqual(False, fight_with_monk())
