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
for first_food in data:
    ingredients, allergens = get_info(first_food)
    if frozenset(allergens) in subgroup:
        subgroup[frozenset(allergens)] = ingredients.intersection(subgroup[frozenset(allergens)])
    else:
        subgroup[frozenset(allergens)] = ingredients

list_allergens = set()
for key, value in subgroup.items():
    for key2, value in subgroup.items():
        if set(key) != set(key2) and len(set(key)) == 1 and set(key).issubset(set(key2)):
            subgroup[key] = subgroup[key].intersection(subgroup[key2])
    if len(set(key)) == 1:
        for each in subgroup[key]:
            list_allergens.add(each)

count = 0
for food in data:
    ingredients, allergens = get_info(food)
    for each in ingredients:
        if each not in list_allergens:
            count += 1

print(count)