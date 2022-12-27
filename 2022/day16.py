import sys

def read_scan_output(filename):
    with open(filename,'r') as fh:
        scan_data = [line.rstrip('\n') for line in fh]

    return scan_data

def parse_scan_data(data):
    scan_output = {}
    for line in data:
        valves_and_flows,tunnels_lead_to = line.split('; ')
    
        t_split = 'valves ' if 'valves ' in tunnels_lead_to else 'valve '
        _,to_valves = tunnels_lead_to.split(t_split)
        tunnels = to_valves.split(', ')
        valve_id, flow_rate_str = valves_and_flows.split(' has flow rate=')
        flow_rate = int(flow_rate_str)
        valve = valve_id[len('Valve '):]

        scan_output[valve] = {'rate':flow_rate, 'tunnels':tunnels}

    return scan_output

if __name__ == "__main__":
    file = sys.argv[1]

    data = read_scan_output(file)
    scans = parse_scan_data(data)

    print(f"The answer to part one is {1}")
    part1_ans = 1

    # print(f"The answer to part two is {0}")
    # part2_ans = 0

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

