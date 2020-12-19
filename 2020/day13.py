import sys
from math import gcd
from functools import reduce

def read_bus_schedule(filename):
    with open(filename,'r') as fh:
        schedule = [line.rstrip('\n') for line in fh]

    earliest_departure_time = int(schedule[0])
    all_buses = schedule[1].split(',')
    working_buses = [int(bid) for bid in all_buses if bid!='x']
    bus_slots = [(int(bid),bindx) for bindx,bid in enumerate(all_buses) if bid!='x']
    return earliest_departure_time,working_buses,bus_slots

if __name__ == "__main__":
    file = sys.argv[1]

    departure_time,buses,slots= read_bus_schedule(file)

    mins_past_departure_time=[bus-departure_time%bus for bid,bus in enumerate(buses)]
    earliest_bus_index =mins_past_departure_time.index(min(mins_past_departure_time))
    earliest_bus = buses[earliest_bus_index]
    waiting_time = min(mins_past_departure_time)
    print(f"The earliest bus to make the arrival time of {departure_time} is {earliest_bus}")
    print(f"Solution: {earliest_bus*waiting_time}")

    upper_limit = reduce(lambda x,y: x*y, [bus[0] for bus in slots])
    bus_slot0 = slots[0][0]
    upper_range = int(upper_limit/bus_slot0)
    for multiplier in range(upper_range):
        if all([(bus_slot0*multiplier)%bus[0] == (bus[0]-bus[1]) for bus in slots[1:]]):
            print(f"The earliest timestamp the bus leave again is {bus_slot0*multiplier}")
