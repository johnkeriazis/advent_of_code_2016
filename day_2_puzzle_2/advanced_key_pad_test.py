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
        self.assertSecurityCode(['DD'], '5')

    def test_move_past_down_max(self):
        self.assertSecurityCode(['DDDDDDDDD'], '5')

    def test_move_right(self):
        self.assertSecurityCode(['R'], '6')

    def test_move_max_right(self):
        self.assertSecurityCode(['RRRR'], '9')

    def test_move_past_max_right(self):
        self.assertSecurityCode(['RRRRRRRRRR'], '9')

    def test_move_to_first_row_valie(self):
        self.assertSecurityCode(['RRUU'], '1')

    def test_move_to_first_last_row_value(self):
        self.assertSecurityCode(['RRDD'], 'D')

    def test_move_to_invalid_left_position(self):
        self.assertSecurityCode(['RUL'], '2')

    def test_move_to_invalid_right_position(self):
        self.assertSecurityCode(['RRRDR'], 'C')

    def test_example(self):
        input_rows = [
            'ULL',
            'RRDDD',
            'LURDL',
            'UUUUD',
        ]
        self.assertSecurityCode(input_rows, '5DB3')

