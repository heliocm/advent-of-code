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

def findPaths(paths):
    possible_paths = [ ['start'] + [each] for each in paths['start']]
    growing = True
    while growing:
        next_paths = []
        for each in possible_paths:
            next_locations = nextLocation(each, paths)
            if len(next_locations) > 0:
                for next_location in next_locations:
                    if each+[next_location] not in next_paths:
                        next_paths.append(each + [next_location])
            else:
                next_paths.append(each)
        if possible_paths == next_paths:
            growing = False
        else:
            possible_paths = next_paths
        # print(possible_paths)
        # possible_paths = next_paths
        # print(possible_paths)
        # growing += 1
        count = 0
        for each in possible_paths:
            if each[-1] == 'end':
                count += 1
        print(growing, count)


paths = buildPath(data)
print(paths)
findPaths(paths)