import io
from unittest import TestCase
from unittest.mock import patch
from main import monk_game_instruction


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monk_game_instruction(self, mock_output):
        monk_game_instruction()
        printed = mock_output.getvalue()
        expected = (
            'The monk has challenged you to a game! It\'s a game using Hanafuda(花札), '
            'a traditional Japanese card game.\n'
            'Out of four beautifully illustrated cards, the monk selects two.\n\n'
            'Your task is to guess which cards the monk is holding.\n'
            'The four cards feature drawings of 1. boar(猪), 2. deer(鹿), 3. butterfly(蝶), and 4. crane(鶴).\n\n'
            'Choose two of them and provide your answer one by one (the order does not matter).\n'
        )
        self.assertEqual(expected, printed)
