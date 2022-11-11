target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

image_enhancement_algorithm = data[0]

del data[0]
del data[0]

image = data

def bin2int (binary):
    return int(binary, 2)

def prepareOutput(image, enhance_round):
    new_image = []
    for i in range(len(image)+2):
        if enhance_round % 2 == 0:
            new_image.append('#'*(len(image)+2)) if i == 0 or i == (len(image) + 1) else new_image.append('#'+image[i-1]+'#')
        else:
            new_image.append('.'*(len(image)+2)) if i == 0 or i == (len(image) + 1) else new_image.append('.'+image[i-1]+'.')
    return new_image
#input nxn retorna n+1xn+1
def enhanceImage(image, enhance_round):
    new_image = prepareOutput(image, enhance_round)
    copy = []
    grid_elements = {(x,y) for x in range(len(new_image)) for y in range(len(new_image[0]))}
    for x in range(len(new_image)):
        new_line = ''
        for y in range(len(new_image[0])):
            binary = ''
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if (i,j) in grid_elements:
                        binary += '1' if new_image[i][j] == '#' else '0'
                    else:
                        if enhance_round % 2 == 0:
                            binary += '1'
                        else:
                            binary += '0'
            index = bin2int(binary)
            new_line += image_enhancement_algorithm[index]
        copy.append(new_line)
    return copy

for i in range(1,51):
    answer = enhanceImage(image, i)
    image = answer[:]

lit = 0
for each in answer:
    lit += each.count('#')
print(lit)