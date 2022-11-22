target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def makeboard():
    board = []
    for i in range(6):
        board.append('.'*50)
    return board
def rect(x,y,board):
    new_board = []
    for j in range(len(board)):
        if j < y:
            row = list(board[j])
            for i in range(x):
                row[i] = '#'
            row = ''.join(row)
            new_board.append(row)
        else:
            new_board.append(board[j])
    return new_board

def rotate_column(x, value, board):
    new_board = []
    for each in board:
        new_board.append(list(each))
    old_column = []
    for y in range(len(new_board)):
        old_column.append(new_board[y][x])
    new_column = old_column[value*-1:] + old_column[:value*-1]
    for y in range(len(new_board)):
        new_board[y][x] = new_column[y]
    rotated_board = []
    for each in new_board:
        rotated_board.append(''.join(each))
    return rotated_board

def rotate_row(y, value, board):
    new_board = []
    for each in board:
        new_board.append(list(each))
    old_row = []
    for x in range(len(new_board[y])):
        old_row.append(new_board[y][x])
    new_row = old_row[value*-1:] + old_row[:value*-1]
    for x in range(len(new_board[y])):
        new_board[y][x] = new_row[x]
    rotated_board = []
    for each in new_board:
        rotated_board.append(''.join(each))
    return rotated_board

def execute_operation(operation, board):
    command = operation.split(' ')
    if command[0] == 'rect':
        values = command[1].split('x')
        new_board = rect(int(values[0]), int(values[1]), board)
    if command[0] == 'rotate':
        if command[1] == 'row':
            new_board = rotate_row(int(command[2][command[2].index('=')+1:]), int(command[4]), board)
        elif command[1] == 'column':
            new_board = rotate_column(int(command[2][command[2].index('=')+1:]), int(command[4]), board)
    return new_board

def print_board(board):
    for each in board:
        print(each)

board = makeboard()

for each in data:
    board = execute_operation(each, board)
answer = 0
for each in board:
    answer += each.count('#')
print(answer)


