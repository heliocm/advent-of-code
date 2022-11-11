target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

board = data
riskboard = []
for x in range(len(data)):
    risk = []
    for y in range(len(data[0])):
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

i = 1
while i <= len(data)+len(data[0]):
    for x in range(len(data)):
        for y in range(len(data[0])):
            calcRisk((x,y))
    i += 1

print(riskboard[len(data)-1][len(data[0])-1])
