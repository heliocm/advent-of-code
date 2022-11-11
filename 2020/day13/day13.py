target_input = open("input.txt" , "r")
notes = target_input.read().split("\n")
del notes[-1]

timestamp = int(notes[0])
possible_bus = notes[1].split(',')
waiting_time = 10000
chosen_bus = 0
for bus_id in possible_bus:
    if not bus_id == "x":
        if ( int(bus_id) - (timestamp % int(bus_id)) ) < waiting_time:
            waiting_time = int(bus_id) - (timestamp % int(bus_id))
            chosen_bus = int(bus_id)

print(waiting_time * chosen_bus)