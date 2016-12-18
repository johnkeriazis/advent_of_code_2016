key_pad = [
    [None, None, '1', None, None],
    [None, '2',  '3', '4',  None],
    ['5',  '6',  '7', '8',  '9'],
    [None, 'A',  'B', 'C',  None],
    [None, None, 'D', None, None],
]


def is_valid_cell(row, col):
    return key_pad[row][col] is not None

def up(row, col):
    if row > 0 and is_valid_cell(row -1, col):
        row -= 1
    return row

def down(row, col):
    if row < 4 and is_valid_cell(row + 1, col):
        row += 1
    return row

def left(row, col):
    if col > 0 and is_valid_cell(row, col -1):
        col -= 1
    return col


def advanced_security_code_generator(input_rows):
    row = 2
    col = 0

    result = ''
    for input_row in input_rows:
        for move in input_row:
            if move == 'U':
                row = up(row, col)
            elif move == 'D':
                row = down(row, col)
            elif move == 'L':
                col = left(row, col)
            elif move == 'R':
                col = right(row, col)
        result += key_pad[row][col]

    return result if bool(result) else key_pad[row][col]


def right(row, col):
    if col < 4 and is_valid_cell(row, col + 1):
        col += 1
    return col




