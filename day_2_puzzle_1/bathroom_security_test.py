import unittest

from day_2_puzzle_1.bathroom_security import security_code_generator


class SecurityCodeGeneratorTest(unittest.TestCase):

    def assertSecurityCode(self, input_rows, expected):
        actual = security_code_generator(input_rows)
        self.assertEqual(str(expected), actual)

    def test_when_start_at_five_and_no_inputs(self):
        self.assertSecurityCode([[]], 5)

    def test_when_start_at_five_and_and_move_up(self):
        self.assertSecurityCode(['U'], 2)

    def test_when_start_at_five_and_and_move_up_twice(self):
        self.assertSecurityCode(['UU'], 2)

    def test_when_start_at_five_and_and_move_down(self):
        self.assertSecurityCode(['D'], 8)

    def test_when_start_at_five_and_and_move_down_twice(self):
        self.assertSecurityCode(['DD'], 8)

    def test_when_start_at_five_and_and_move_left(self):
        self.assertSecurityCode(['L'], 4)

    def test_when_start_at_five_and_and_move_left_2x(self):
        self.assertSecurityCode(['LL'], 4)

    def test_when_start_at_five_and_and_move_right(self):
        self.assertSecurityCode(['R'], 6)

    def test_when_start_at_five_and_and_move_right_2x(self):
        self.assertSecurityCode(['RR'], 6)

    def test_when_start_at_five_and_and_move_right_and_down(self):
        self.assertSecurityCode(['RD'], 9)

    def test_2d_move_right_then_down(self):
        self.assertSecurityCode(['R', 'D'], '69')

    def test_example_one(self):
        input_rows = [
            'ULL',
            'RRDDD',
            'LURDL',
            'UUUUD'
        ]
        self.assertSecurityCode(input_rows, '1985')
