target_input = open("input.txt" , "r")
notes = target_input.read().split("\n")
del notes[-1]

def chinese_remainder(divisors, remainders):
    total = 0
    prod = 1
    for each in divisors:
        prod = prod * each
    for divisor, remainder in zip(divisors, remainders):
        exclusive_prod = prod // divisor
        total += remainder * factor_calculator(exclusive_prod, divisor) * exclusive_prod
    return total % prod
  
def factor_calculator(prod, divisor):
    last_divisor = divisor
    last_factor, next_factor = 0, 1
    if divisor == 1: return 1
    while prod > 1:
        quocient = prod // divisor
        prod, divisor = divisor, prod%divisor
        last_factor, next_factor = next_factor - quocient * last_factor, last_factor
    if next_factor < 0: next_factor += last_divisor
    return next_factor
 

bus_list = notes[1].split(',')
remainders = []
buses = []
for bus in bus_list:
    if not bus == "x":
        remainders.append(int(bus) - bus_list.index(bus))
        buses.append(int(bus))

print(chinese_remainder(buses, remainders))

