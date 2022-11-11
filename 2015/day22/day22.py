target_input = open("input.txt" , "r")
data = target_input.read().split("\n")
del data[-1]

#[Cost, Dmg = 0 and Effect = 1, Turns. 0 for instant, Damage, Heal, Mana]
spellbook = {
    'Magic Missile': [],
    'Drain': [],
    'Shield': [],
    'Poison': [],
    'Recharge': []
}
def isAlive(character):
    if character['Hit Points'] <= 0:
        return False
    return True

def battle(player, enemy):
    while isAlive(player) and isAlive(enemy):
        damage = player['Damage'] - enemy['Armor']
        if damage <= 0 : damage = 1
        enemy['Hit Points'] -= damage
        if enemy['Hit Points'] <= 0: return 'Win'

        damage = enemy['Damage'] - player['Armor']
        if damage <= 0 : damage = 1
        player['Hit Points'] -= damage
        if player['Hit Points'] <= 0: return 'Loss'

boss = {}
for each in data:
    each = each.split(': ')
    boss[each[0]] = int(each[-1])

print(isAlive(boss))