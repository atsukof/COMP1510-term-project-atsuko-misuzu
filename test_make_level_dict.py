from unittest import TestCase

from main import make_level_dict


class Test(TestCase):
    def test_make_level_dict(self):
        expected = {'level 1': {'KEP_max': 2, 'maximum_HP': 5, 'name': 'Kyoto rookie'}, 'level 2': {'KEP_max': 5, 'maximum_HP': 7, 'name': 'Kyoto skilled novice'}, 'level 3': {'KEP_max': 9999, 'maximum_HP': 10, 'name': 'Kyoto expert'}}
        self.assertEqual(expected, make_level_dict())

