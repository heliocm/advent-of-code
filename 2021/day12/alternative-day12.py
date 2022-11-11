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
    if path[-1] != 'end':
        for each in paths[path[-1]]:
            if each.islower() and each not in path and each != 'start':
                next_locations.append(each)
            elif each.isupper():
                next_locations.append(each)
    return(next_locations)

def findPath(partial, graph, paths=[]):
    next_locations = nextLocation(partial, graph)
    if partial[-1] == 'end':
        paths.append(partial)
    for each in next_locations:
        for path in findPath(partial+[each], graph):
                continue
    return paths


graph = buildPath(data)
print(len(findPath(['start'], graph)))

