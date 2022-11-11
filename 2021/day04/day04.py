def findWinningBoard(board, drawnumbers):
    for row in board:
        if set(row).issubset(set(drawnumbers)):
            return board, row
    for i in range(0,len(board)):
        column = []
        for row in board:
            column.append(row[i])
        if set(column).issubset(set(drawnumbers)):
            return board, column
    return 0

target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

numbers = tuple([int(number) for number in data[0].split(",")])
print(numbers)
del data[0]

i = 0
boards = []
while i < len(data):
    shape = data[i+1:i+6]
    board = []
    for each in shape:
        row = each.split(" ")
        while len(row) > 5:
            row.remove('')
        numeric_row = tuple([int(number) for number in row])
        board.append(numeric_row)
    boards.append(board)
    i = i+6
drawn = numbers[:5]
drawing = True
i=0
while drawing :
    for board in boards:
        result = findWinningBoard(board, drawn)
        if result != 0:
            drawing = False
            break
    if result == 0:
        i += 1
        drawn = numbers[:5+i]

print(result)
print(drawn[-1])
answer = 0
for each in result[0]:
    for number in each:
        if number not in drawn:
            answer += number
print(answer*drawn[-1])

    
