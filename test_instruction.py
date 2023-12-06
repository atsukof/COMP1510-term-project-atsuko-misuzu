import io
from unittest import TestCase
from unittest.mock import patch

from main import instruction


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_instruction(self, mock_output):
        instruction()
        the_game_print_this = mock_output.getvalue()
        expected_message = ('Through this game, you can explore Kyoto which is one of our most favourite cities.\n'
                            'Your mission is to go to Kinkakuji temple, and defeat a monk.\n'
                            'To fight with a monk, answer random quizzes correctly '
                            'to earn Kyoto Experience Points(KEP).'
                            'The quizzes are about Japan.\n'
                            'If you answer incorrectly, your HP will decrease by 1.'
                            'Before your HP becomes 0, you need to find food and eat.\n'
                            'Let\'s begin!\n')
        self.assertEqual(expected_message, the_game_print_this)
