target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def expandBoard(board):
    newboard=[]
    for each in data:
        i = 1
        newline = ''
        while i <= 5:
            for char in each:
                if int(char)+i-1 < 10:
                    newline += str(int(char)+i-1)
                else:
                    newline += str((int(char)+i-1) - 10 + 1)
            i+= 1
        newboard.append(newline)
    finalboard = []
    i = 1
    while i <= 5:
        for each in newboard:
            finalline = ''
            for char in each:
                if int(char)+i-1 < 10:
                    finalline += str(int(char)+i-1)
                else:
                    finalline += str((int(char)+i-1) - 10 + 1)
            finalboard.append(finalline)
        i += 1            
    return finalboard
board = expandBoard(data)
riskboard = []
for x in range(len(board)):
    risk = []
    for y in range(len(board[0])):
        risk.append(10000)
    riskboard.append(risk)

def updateRisk(position, risk):
    (x, y) = position
    riskboard[x][y] = risk

def calcRisk(position):
    (x, y) = position
    if x == 0 and y == 0:
        risk = 0
    elif x == 0 and y == len(board[0])-1:
        risk = int(board[x][y]) + min(riskboard[x][y-1], riskboard[x+1][y])
    elif x == 0:
        risk = int(board[x][y]) + min(riskboard[x][y-1], riskboard[x][y+1], riskboard[x+1][y])
    elif y == 0 and x == len(board)-1:
        risk = int(board[x][y]) + min(riskboard[x][y+1], riskboard[x-1][y])
    elif y == 0:
        risk = int(board[x][y]) + min(riskboard[x-1][y], riskboard[x][y+1], riskboard[x+1][y])
    elif y == len(board[0])-1 and x == len(board)-1:
        risk = int(board[x][y]) + min(riskboard[x][y-1], riskboard[x-1][y])
    elif x == len(board)-1:
        risk = int(board[x][y]) + min(riskboard[x][y-1], riskboard[x][y+1], riskboard[x-1][y])
    elif y == len(board[0])-1:
        risk = int(board[x][y]) + min(riskboard[x][y-1], riskboard[x-1][y], riskboard[x+1][y])
    else:
        risk = int(board[x][y]) + min(riskboard[x][y-1], riskboard[x][y+1], riskboard[x+1][y], riskboard[x-1][y])
    
    updateRisk((x, y), risk)

i = 0
while i <= len(board)+len(board[0]):
    for x in range(len(board)):
        for y in range(len(board[0])):
            calcRisk((x,y))
    i += 1

print(riskboard[-1][-1])