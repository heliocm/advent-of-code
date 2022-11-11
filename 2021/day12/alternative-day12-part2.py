target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def buildPath(data):
    paths = {}
    for each in data:
        each = each.split("-")
        for location in each:
            if location not in paths:
                paths[location] = [cave for cave in each]
                paths[location].remove(location)
            else:
                for cave in each:
                    paths[location].append(cave)
                paths[location].remove(location)
    return paths

def nextLocation(path, paths):
    next_locations = []
    repeat_small = False
    for each in path:
        if each.islower() and path.count(each) > 1:
            repeat_small = True
    if path[-1] != 'end':
        for each in paths[path[-1]]:
            if each.islower() and each not in path and each != 'start':
                next_locations.append(each)
            elif each.islower() and not repeat_small and each != 'start':
                next_locations.append(each)
            elif each.isupper():
                next_locations.append(each)
    return(next_locations)

# def findPath(partial, graph, paths=0):
#     next_locations = nextLocation(partial, graph)
#     if partial[-1] == 'end':
#         paths += 1
#     if next_locations != []:
#         for each in next_locations:
#             for path in findPath(partial+[each], graph):
#                 continue
#     return paths

def calcPaths(partial, graph, answer = 0):
    next_locations = nextLocation(partial, graph)
    if partial[-1] == 'end':
        answer += 1
    if next_locations != []:
        for each in next_locations:
            answer += calcPaths(partial+[each], graph)
    return answer

graph = buildPath(data)
print(calcPaths(['start'], graph))

