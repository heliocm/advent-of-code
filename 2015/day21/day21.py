target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

def battle(player, enemy):
    while player['Hit Points'] > 0 and enemy['Hit Points'] > 0:
        damage = player['Damage'] - enemy['Armor']
        if damage <= 0 : damage = 1
        enemy['Hit Points'] -= damage
        if enemy['Hit Points'] <= 0: return 'Win'

        damage = enemy['Damage'] - player['Armor']
        if damage <= 0 : damage = 1
        player['Hit Points'] -= damage
        if player['Hit Points'] <= 0: return 'Loss'

store_input = open("store.txt", "r")
store_data = store_input.read().split("\n\n")

weapons = {}
armors = {}
rings = {}
for i in range(0, len(store_data)):
    store_data[i] = store_data[i].split("\n")
    for each in store_data[i]:
        each = each.split()
        if each[1].isnumeric():
            if i == 0: weapons[each[0]] = [int(each[1]), int(each[2]), int(each[3])] 
            if i == 1: armors[each[0]] = [int(each[1]), int(each[2]), int(each[3])]
            if i == 2: rings[each[0]] = [int(each[1]), int(each[2]), int(each[3])] 

armors['NoArmor'] = [0, 0, 0]
rings['NoLeft'] = [0, 0, 0]
rings['NoRight'] = [0, 0, 0]

lowest = 10000
for weapon in weapons:
    for armor in armors:
        for left_ring in rings:
            for right_ring in rings:
                if left_ring != right_ring:
                    boss = {}
                    for each in data:
                        each = each.split(': ')
                        boss[each[0]] = int(each[-1])
                    player = {
                        'Hit Points': 100,
                        'Damage': weapons[weapon][1] + rings[left_ring][1] + rings[right_ring][1],
                        'Armor': armors[armor][2] + rings[left_ring][2] + rings[right_ring][2]
                    }
                    cost = weapons[weapon][0] + armors[armor][0] + rings[left_ring][0] + rings[right_ring][0]
                    if battle(player,boss) == 'Win':
                        if cost < lowest: lowest = cost

print(lowest)