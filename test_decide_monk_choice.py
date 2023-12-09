from unittest import TestCase
from unittest.mock import patch
from main import decide_monk_choice


class Test(TestCase):
    @patch('random.randint', return_value=0)
    def test_decide_monk_choice(self, _):
        cards = {1: 'boar', 2: 'deer', 3: 'butterfly', 4: 'crane'}
        expected = {1, 2}
        self.assertEqual(expected, decide_monk_choice(cards))
