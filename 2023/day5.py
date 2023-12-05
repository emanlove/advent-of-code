import sys

def read_almanac(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    # read seeds
    _, *seeds = lines[0].split()
    seeds = [int(s) for s in seeds]

    # maps
    maps = {}
    for line in lines[2:]:
        if line.endswith(' map:'):
            map_name,_ = line.split(' map:')
            if map_name not in maps:  # assuming `if` not necessary as I would expect just one line/section for a map
                maps[map_name] = []
        elif line != '':
            destination_range_start, source_range_start, range_length = line.split()
            # print(f"{map_name}: {destination_range_start} {source_range_start} {range_length}")
            maps[map_name].append( (int(source_range_start), int(destination_range_start), int(range_length)) )
        else:
            continue

    # As the categories are hard code and the same for the sample and problem data I am not going
    # to make these generic
    # print(f"{maps}")
    locations = []
    for seed in seeds:
        # seed-to-soil
        soil = map_source_to_destination(maps['seed-to-soil'], seed)
        # soil-to-fertilizer
        fertilizer = map_source_to_destination(maps['soil-to-fertilizer'], soil)
        # fertilizer-to-water
        water = map_source_to_destination(maps['fertilizer-to-water'], fertilizer)
        # water-to-light
        light = map_source_to_destination(maps['water-to-light'], water)
        # light-to-temperature
        temperature = map_source_to_destination(maps['light-to-temperature'], light)
        # temperature-to-humidity
        humidity = map_source_to_destination(maps['temperature-to-humidity'], temperature)
        # humidity-to-location
        location = map_source_to_destination(maps['humidity-to-location'], humidity)

        locations.append(location)
    
    print(f"The lowest location number that corresponds to any of the initial seed numbers is {min(locations)}")

def map_source_to_destination(named_map, source):
    for mapping in named_map:
        start = mapping[0]; end = mapping[0]+mapping[2]; dest_start = mapping[1]
        if start <= source < end:
            destination = source-start+dest_start
            return destination
    return source




if __name__ == "__main__":
    file = sys.argv[1]

    read_almanac(file)
