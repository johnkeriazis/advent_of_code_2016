from pprint import pformat

key_pad = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

def security_code_generator(input_rows):
    row = 1
    col = 1

    result = ''
    for input_row in input_rows:
        for move in input_row:
            if move == 'U' and row > 0:
                row -= 1
            elif move == 'D' and row < 2:
                row += 1
            elif move == 'L' and col > 0:
                col -= 1
            elif move == 'R' and col < 2:
                col += 1
        result += key_pad[row][col]

    return result

input_rows = []
with open('d0201.txt') as f:
    for line in f.readlines():
        input_rows.append(line)


print security_code_generator(input_rows)

##print pformat(input_rows)
#
#ctr = 1
#for row in input_rows:
#    print ctr
#    for c in row:
#        print c
#    ctr += 1
#    print '--'
