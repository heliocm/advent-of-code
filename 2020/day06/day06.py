import numpy as np
target_input = open("input.txt" , "r")
answers = target_input.read().split("\n\n")

result = 0

for group in answers:
    group = group.split("\n")
    group_votes = []
    if group[-1] == '':
        del group[-1]
    
    for person in group:
        person = list(person)
        for each in np.setdiff1d(person, group_votes):
            group_votes.append(each)
        
    result = result + len(group_votes)

print(result)