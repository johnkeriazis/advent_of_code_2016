import unittest

from day_2_puzzle_1.bathroom_security import bathroom_code_generator


class BathroomSecurityTest(unittest.TestCase):

    def test_when_start_at_five_and_no_inputs(self):
        actual = bathroom_code_generator([])
        self.assertEqual(5, actual)

    def test_when_start_at_five_and_and_move_up(self):
        actual = bathroom_code_generator(['U'])
        self.assertEqual(2, actual)
