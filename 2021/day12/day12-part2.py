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
        count = 0
        answer = []
        for each in possible_paths:
            if each[-1] == 'end':
                count += 1
                answer.append(each)
        print(growing, count)
    answer.sort()
    # for each in answer:
        # print(each)

paths = buildPath(data)
print(paths)
findPaths(paths)
print('parei')
# print(nextLocation(['start', 'A', 'b', 'A', 'c', 'A'],paths))