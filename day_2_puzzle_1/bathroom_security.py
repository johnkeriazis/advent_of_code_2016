

key_pad = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def bathroom_code_generator(inputs):
    row = 1
    col = 1
    for move in inputs:
        if move == 'U' and row > 0:
            row -= 1
        elif move == 'D' and row < 2:
            row += 1
        elif move == 'L' and col > 0:
            col -= 1
        elif move == 'R' and col < 2:
            col += 1

    return key_pad[row][col]
