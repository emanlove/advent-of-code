import sys

def read_schematic(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    nCols = len(lines[0])
    #rows = len(lines)

    schematic = ''.join(lines)
    schematic_range = range(len())
    objs = schematic.split('.')

    part_numbers = {}
    symbols = {}
    any_symbol = []
    pos = 0
    for obj in objs:
        if is_number(obj):
            # ? can we have duplicate part numbers .. assuming yes
            if obj not in part_numbers:
                part_numbers[obj] = []
            part_numbers[obj].append(pos)
            # schematic.find(obj)            
            pos += len(obj)
        elif obj=='':            
            pos += 1
        else:
            if obj not in symbols:
                symbols[obj] = []
            symbols[obj].append(pos)
            any_symbol.append(pos)
            pos += 1  # assuming symbols are single characters and any adjacent symbols are sepearet symbols

    symbol_chars = symbols.keys()

    for part in part_numbers:
        for duplicate_start in part_numbers[part]:
            for index,digit in enumerate(part):
                pos = duplicate_start + index
                adjacent = [pos-nCols-1, pos-nCols, pos-nCols+1,
                             pos-1,                  pos+1,
                             pos+nCols-1, pos+nCols, pos+nCols+1]

                for point in adjacent:
                    if point in schematic_range and schematic[point] in symbol_chars:
                        # add part number to list of valid part numbers
                        pass

    print(f"The sum of all of the part numbers in the engine schematic is ")

def is_number(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False




if __name__ == "__main__":
    file = sys.argv[1]

    read_schematic(file)
