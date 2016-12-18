key_pad = [
    [None, None, '1', None, None],
    [None, '2',  '3', '4',  None],
    ['5',  '6',  '7', '8',  '9'],
    [None, 'A',  'B', 'C',  None],
    [None, None, 'D', None, None],
]


def up(row, col):
    if row > 0 and key_pad[row -1][col] is not None:
        row -= 1
    return row


def advanced_security_code_generator(input_rows):
    row = 2
    col = 0

    result = ''
    for input_row in input_rows:
        for move in input_row:
            if move == 'U':
                row = up(row, col)
            elif move == 'D' and row < 2:
                row += 1
            elif move == 'L' and col > 0:
                col -= 1
            elif move == 'R' and col < 2:
                col += 1
        result += key_pad[row][col]

    return result if bool(result) else key_pad[row][col]