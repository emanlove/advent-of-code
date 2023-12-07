import sys

def read_almanac(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    # read seeds - Part 1
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

def read_almanac_part2(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    # read seed_ranges - Part 2
    _, *srInts = lines[0].split()
    sr = [int(s) for s in srInts]
    # seed_ranges = [ [ sr[i], sr[i]+sr[i+1] ] for i in range(0,len(sr),2)]
    seed_ranges = [ ( sr[i], sr[i+1] ) for i in range(0,len(sr),2)]    
    seeds = [item for ranges in seed_ranges for item in ranges]

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
            # maps[map_name].append( (int(source_range_start), int(destination_range_start), int(range_length)) )
            maps[map_name].append( {'s':int(source_range_start), 'd':int(destination_range_start), 'l':int(range_length) } )
        else:
            continue

    # As the categories are hard code and the same for the sample and problem data I am not going
    # to make these generic

    # seed to soil ...
    # ...

    print(f"The lowest location number that corresponds to any of the initial seed numbers is ...")
    
def map_source_ranges_to_destination_ranges(named_map, source_ranges):
    """Pseodo-code for mapping source to destination

    while there is still maps
    ?while there is still unmapped sources?
      see what source match them
      .. and if a match is found move that part of the source to destination shifted
      else get rid of that portion of the map
    then if there is any remaining unmapped source copy it of to the destination
    
    """

    destination = []
    # while source:
    # while there is still maps
    while named_map:
        s2d = named_map.pop(0)
        # see what source match them
        # for source in sources or while sources??
        for source in source_ranges:
            # check if map out of range for this source ..
            if ( (s2d['s']+s2d['l']) < source[0] ) or ( (source[0]+source[1]) < s2d['s'] ):   # map out of range for this source            
                continue
            # .. else it overlaps
            if s2d['s'] < source[0]:   # map starts before source range  
                # add new map for section leading up to source
                # record start mapped index relative to source = 0
                pass
            else:                      # map starts within source range  
                # record start mapped index relative to source = s2d['s']-source[0] 
                pass

            if (s2d['s']+s2d['l']) > (source[0]+source[1]):    # map ends past source range
                # add new map for section going past source
                # record end mapped index relative to source end = source[0]+source[1]
                # ?? record end mapped index relative to source start = source[1] ??
                pass
            else:                                              # map ends within source range
                # ?? record end mapped index relative to source end = source[0]+source[1] - xxxxx ??
                pass

            # pop source and push to destination

    # while there is still unmapped sources
    #   see what source match them
    #   .. and if a match is found move that part of the source to destination shifted
    #   else get rid of that portion of the map
    # then if there is any remaining unmapped source copy it of to the destination
    #

if __name__ == "__main__":
    file = sys.argv[1]

    read_almanac_part2(file)