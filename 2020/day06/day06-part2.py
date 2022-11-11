import numpy as np
target_input = open("input.txt" , "r")
answers = target_input.read().split("\n\n")

result = 0

for group in answers:
    group = group.split("\n")
    group_votes = []
    if group[-1] == '':
        del group[-1]
    first_person = True
    
    for person in group:
        person = list(person)
        if first_person:
            last_person = person
            first_person = False
        
        last_person = np.intersect1d(person, last_person)
        group_votes = last_person
        
    result = result + len(group_votes)

print(result)