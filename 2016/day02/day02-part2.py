target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def find_position(digit, board):
    index = 0
    for line in board:
        if digit in line:
            return(index, line.index(digit))
        else:
            index += 1

def decode_instructions(starting_point, instruction):
    for each in instruction:
        if each == 'L':
            x,y = find_position(starting_point, board)
            if y-1 >= 0 and board[x][y-1] != '0':
                starting_point = board[x][y-1]
        elif each == 'R':
            (x,y) = find_position(starting_point, board)
            if y+1 < len(board) and board[x][y+1] != '0':
                starting_point = board[x][y+1]
        elif each == 'U':
            (x,y) = find_position(starting_point, board)
            if x-1 >= 0 and board[x-1][y] != '0':
                starting_point = board[x-1][y]
        else:
            (x,y) = find_position(starting_point, board)
            if x+1 < len(board) and board[x+1][y] != '0':
                starting_point = board[x+1][y]
    return starting_point

starting_point = '5'

board = [['0','0','1','0','0'],
         ['0','2','3','4','0'],
         ['5','6','7','8','9'],
         ['0','A','B','C','0'],
         ['0','0','D','0','0']]
# input_test = ['ULL','RRDDD','LURDL','UUUUD']
code = ""
for each in data:
    starting_point = decode_instructions(starting_point, each)
    code += starting_point

print(code)


