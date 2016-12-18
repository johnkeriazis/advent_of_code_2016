import unittest
from day_2_puzzle_2.advanced_key_pad import advanced_security_code_generator


class AdvancedKeypadTest(unittest.TestCase):
    def assertSecurityCode(self, input_rows, expected):
        actual = advanced_security_code_generator(input_rows)
        self.assertEquals(expected, actual)

    def test_move_with_no_inputs(self):
        self.assertSecurityCode([], '5')

    def test_move_when_input_is_out_of_bounds_coordinate(self):
        self.assertSecurityCode(['L'], '5')

    def test_move_when_input_is_out_of_bounds_value(self):
        self.assertSecurityCode(['U'], '5')

    def test_move_when_input_is_out_of_bounds_value(self):
        self.assertSecurityCode(['D'], '5')
