target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]
triangles = 0
for each in data:
    elements = []
    not_triangle = False
    for element in each.split(' '):
        if element.isnumeric():
            elements.append(element)
    print(elements)
    for i in [-1,0,1]:
        if int(elements[i]) + int(elements[i+1]) <= int(elements[i-1]):
            not_triangle = True
    triangles += 0 if not_triangle else 1
print(triangles)