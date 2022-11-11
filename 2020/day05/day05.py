target_input = open("input.txt" , "r")
airplane = target_input.read().split("\n")
del airplane[-1]
#print(airplane)

major_id = 0

for seat in airplane:
    row_indicator = seat[:7]
    column_indicator = seat[-3:]
    row = []
    for i in range(128):
        row.append(i)
    last_index = len(row)
    middle_index = last_index // 2
    for letter in list(row_indicator):
        if letter == 'F':
            row = row[:middle_index]
        if letter == 'B':
            row = row[middle_index:]
        middle_index = middle_index // 2
    column = []
    for i in range(8):
        column.append(i)
    last_index = len(column)
    middle_index = last_index // 2
    for letter in list(column_indicator):
        if letter == 'L':
            column = column[:middle_index]
        if letter == 'R':
            column = column[middle_index:]
        middle_index = middle_index // 2
    
    seat_id = row[0] * 8 + column[0]
    if seat_id > major_id:
        major_id = seat_id

print(major_id)