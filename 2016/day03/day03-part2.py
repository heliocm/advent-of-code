target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]
triangles = 0
lines = 0
for each in data:
    if lines == 0:
        group = [[],[],[]]
    elements = []
    for element in each.split(' '):
        if element.isnumeric():
            elements.append(element)
    for i in range(3):
        group[i].append(elements[i])
    lines += 1
    if lines == 3:
        for each in group:
            print(each)
            not_triangle = False
            for i in [-1,0,1]:
                if int(each[i]) + int(each[i+1]) <= int(each[i-1]):
                    not_triangle = True
            triangles += 0 if not_triangle else 1
        lines = 0
print(triangles)