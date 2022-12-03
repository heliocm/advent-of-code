target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

data_test = ['value 5 goes to bot 2',
'bot 2 gives low to bot 1 and high to bot 0',
'value 3 goes to bot 1',
'bot 1 gives low to output 1 and high to bot 0',
'bot 0 gives low to output 2 and high to output 0',
'value 2 goes to bot 2']
def separate_values_and_instructions(data):
    values = []
    instructions = []
    for each in data:
        if each.split(' ')[0] == 'value':
            values.append(each)
        else:
            instructions.append(each)
    return values, instructions

def initial_values(values):
    bots = {}
    for each in values:
        each = each.split(' ')
        if each[-1] in bots:
            bots[each[-1]].append(int(each[1]))
        else:
            bots[each[-1]] = [int(each[1])]
    return bots
def get_bot_value(instruction, bots):
    if instruction[-1] in bots:
        bots[instruction[-1]].append(instruction[1])
    else:
        bots[instruction[-1]] = list(instruction[1])
    return bots

def bot_has_two_values(bot, bots):
    if bot in bots and len(bots[bot]) >= 2:
        if microchip_values.issubset(set(bots[bot])):
            print(bot)
        return True
    return False

def distribute_values(instruction, bots, outputs):
    bot = instruction[1]
    low = instruction[6]
    high = instruction[-1]
    if instruction[-2] == 'bot':
        if high in bots:
            bots[high].append(max(bots[bot]))
        else:
            bots[high] = [max(bots[bot])]
    else:
        if high in outputs:
            outputs[high].append(max(bots[bot]))
        else:
            outputs[high] = [max(bots[bot])]
    if instruction[5] == 'bot':
        if low in bots:
            bots[low].append(min(bots[bot]))
        else:
            bots[low] = [min(bots[bot])]
    else:
        if low in outputs:
            outputs[low].append(min(bots[bot]))
        else:
            outputs[low] = [min(bots[bot])]
    bots.pop(bot)
    return bots, outputs

# instructions = data
# microchip_values = {'61', '17'}
# bots = {}
# outputs = {}
# while(len(instructions)) != 0:
#     new_instructions = []
#     for each in instructions:
#         each = each.split(' ')
#         if each[0] == 'value':
#             bots = get_bot_value(each, bots)
#         else:
#             if bot_has_two_values(each[1], bots):
#                 bots, outputs = distribute_values(each, bots, outputs)
#             else:
#                 new_instructions.append(' '.join(each))
#     instructions = new_instructions

values, instructions = separate_values_and_instructions(data)
outputs = {}
microchip_values = {61, 17}

bots = initial_values(values)
print(bots)
while(len(instructions) != 0):
    new_instructions = []
    for each in instructions:
        each = each.split(' ')
        if bot_has_two_values(each[1], bots):
            bots, outputs = distribute_values(each, bots, outputs)
        else:
            new_instructions.append(' '.join(each))
    instructions = new_instructions

print(outputs)
print(outputs['0'][0]*outputs['1'][0]*outputs['2'][0])