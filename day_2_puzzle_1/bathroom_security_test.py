import unittest

from day_2_puzzle_1.bathroom_security import bathroom_code_generator


class BathroomSecurityTest(unittest.TestCase):

    def test_when_start_at_five_and_no_inputs(self):
        actual = bathroom_code_generator([])
        self.assertEqual(5, actual)

    def test_when_start_at_five_and_and_move_up(self):
        actual = bathroom_code_generator(['U'])
        self.assertEqual(2, actual)

    def test_when_start_at_five_and_and_move_up_twice(self):
        actual = bathroom_code_generator(['U', 'U'])
        self.assertEqual(2, actual)

    def test_when_start_at_five_and_and_move_down(self):
        actual = bathroom_code_generator(['D'])
        self.assertEqual(8, actual)

    def test_when_start_at_five_and_and_move_down_twice(self):
        actual = bathroom_code_generator(['D', 'D'])
        self.assertEqual(8, actual)

    def test_when_start_at_five_and_and_move_left(self):
        actual = bathroom_code_generator(['L'])
        self.assertEqual(4, actual)

    def test_when_start_at_five_and_and_move_left_2x(self):
        actual = bathroom_code_generator(['L', 'L'])
        self.assertEqual(4, actual)

    def test_when_start_at_five_and_and_move_right(self):
        actual = bathroom_code_generator(['R'])
        self.assertEqual(6, actual)

    def test_when_start_at_five_and_and_move_right_2x(self):
        actual = bathroom_code_generator(['R', 'R'])
        self.assertEqual(6, actual)
