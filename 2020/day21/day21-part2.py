target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def get_info(food):
    food = food.replace(")", "").replace("(", "").replace(",", "").split(" ")
    ingredients = []
    allergens = []
    for i in range(0, food.index("contains")):
        ingredients.append(food[i])
    for i in range(food.index("contains")+1, len(food)):
        allergens.append(food[i])
    return set(ingredients), set(allergens)

subgroup = {}
allergen_list = {}
for first_food in data:
    ingredients, allergens = get_info(first_food)
    if frozenset(allergens) in subgroup:
        subgroup[frozenset(allergens)] = ingredients.intersection(subgroup[frozenset(allergens)])
    else:
        subgroup[frozenset(allergens)] = ingredients

for key, value in subgroup.items():
    for key2, value in subgroup.items():
        if set(key) != set(key2) and len(set(key)) == 1 and set(key).issubset(set(key2)):
            subgroup[key] = subgroup[key].intersection(subgroup[key2])
    if len(set(key)) == 1:
        for element in set(key):
            allergen_list[element] = subgroup[key]

done = False
while not done:
    for key, value in allergen_list.items():
        if len(value) != 1:
            continue
        else:
            for key2, value2 in allergen_list.items():
                if key != key2:
                    if value.issubset(value2):
                        for each in value:
                            allergen_list[key2].remove(each)
    done = True
    for value in allergen_list.values():
        if len(value) != 1:
            done = False

answer = ""
for i in sorted(allergen_list):
    for each in allergen_list[i]:
        answer += each + ","
answer = answer[:-1]
print(answer)