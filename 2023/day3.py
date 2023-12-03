import sys

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def read_schematic(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    nCols = len(lines[0])
    #rows = len(lines)
    
    flattened_schematic = ''.join(lines)

    part_numbers = {}
    symbols = {}
    any_symbol = []

    for row,line in enumerate(lines):
        obj = ''
        pos = None
        for col,char in enumerate(line):
            if char in DIGITS:
                if not obj:
                    pos = col + (row*nCols)
                obj += char
            elif char=='.':
                if obj:  # close out number if there
                    if obj not in part_numbers:
                        part_numbers[obj] = []                    
                    part_numbers[obj].append(pos)
                    obj = ''
                    pos = None
            else:  # symbol
                if obj:  # close out number if there
                    if obj not in part_numbers:
                        part_numbers[obj] = []                    
                    part_numbers[obj].append(pos)
                    obj = ''
                    pos = None
                pos = col + (row*nCols)
                # record individual symbols in case if needed in part 2
                if char not in symbols:
                    symbols[char] = []
                symbols[char].append(pos)
                any_symbol.append(pos)
                pos = None
        # reached end of line and need to ..
        if obj:  # .. close out number if there
            # print(f"{obj}")
            if obj not in part_numbers:
                part_numbers[obj] = []                    
            part_numbers[obj].append(pos)

    # print(f"{flattened_schematic}")
    # import pdb;pdb.set_trace()

    # schematic = ''.join(lines)
    # objs = schematic.split('.')

    # part_numbers = {}
    # symbols = {}
    # any_symbol = []
    # pos = 0
    # for obj in objs:
    #     if is_number(obj):
    #         # ? can we have duplicate part numbers .. assuming yes
    #         if obj not in part_numbers:
    #             part_numbers[obj] = []
    #         part_numbers[obj].append(pos)
    #         # schematic.find(obj)            
    #         pos += len(obj)
    #     elif obj=='':            
    #         pos += 1
    #     else:
    #         if obj not in symbols:
    #             symbols[obj] = []
    #         symbols[obj].append(pos)
    #         any_symbol.append(pos)
    #         pos += 1  # assuming symbols are single characters and any adjacent symbols are sepearet symbols

    symbol_chars = symbols.keys()

    valid_parts = []
    for part in part_numbers:
        for duplicate_start in part_numbers[part]:
            possible_part = valid_part_number_check(part,duplicate_start,flattened_schematic,nCols,symbol_chars)

            if possible_part is not None:
                valid_parts.append(possible_part)
            # for index,digit in enumerate(part):
            #     pos = duplicate_start + index
            #     adjacent = [pos-nCols-1, pos-nCols, pos-nCols+1,
            #                  pos-1,                  pos+1,
            #                  pos+nCols-1, pos+nCols, pos+nCols+1]

            #     for point in adjacent:
            #         if point in schematic_range and schematic[point] in symbol_chars:
            #             # add part number to list of valid part numbers
            #             pass

    print(f"The sum of all of the part numbers in the engine schematic is {sum(valid_parts)}")

    stars =  {indx: [] for indx in symbols['*']}
    possible_gears = {}

    part_numbers_digit_pos = {}
    # import pdb;pdb.set_trace()

    for part in part_numbers:
        if len(part_numbers[part]) > 1:
            print("!!WARNING!! Repeated part number")
        for start in part_numbers[part]:
            part_numbers_digit_pos[start] = { 'positions' : [i for i in range(start,start+len(part))] ,
                                              'part'      : int(part) }

    for star in stars:
        adjacent = set( [star-nCols-1, star-nCols, star-nCols+1,
                         star-1,                   star+1,
                         star+nCols-1, star+nCols, star+nCols+1] )

        # for point in adjacent:
        for start in part_numbers_digit_pos:
            if set(part_numbers_digit_pos[start]['positions']) & adjacent:
                stars[star].append(part_numbers_digit_pos[start]['part'])

    gear_ratios = []
    for star in stars:
        if len(stars[star])==2:
            gear_ratios.append(stars[star][0]*stars[star][1])

    print(f"The sum of all of the gear ratios in your engine schematic is {sum(gear_ratios)}")

def valid_part_number_check(part, start_pos, schematic, nCols, symbol_chars):
    schematic_range = range(len(schematic))
    for index,digit in enumerate(part):
        pos = start_pos + index
        adjacent = [pos-nCols-1, pos-nCols, pos-nCols+1,
                    pos-1,                  pos+1,
                    pos+nCols-1, pos+nCols, pos+nCols+1]

        for point in adjacent:
            if point in schematic_range and schematic[point] in symbol_chars:
                        # add part number to list of valid part numbers
                        return int(part)
    return None

def is_number(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    file = sys.argv[1]

    read_schematic(file)
