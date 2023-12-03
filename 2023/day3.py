import sys

def read_schematic(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    cols = len(lines[0])
    rows = len(lines)

    schematic = ''.join(lines)
    objs = schematic.split('.')

    part_numbers = {}
    symbols = {}
    any_symbol = []
    pos = 0
    for obj in objs:
        if is_number(obj):
            # ? can we have duplicate part numbers
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
            pos += 1  # assuming symbls are single characters and any adjacent symbols are sepearet symbols


    import pdb;pdb.set_trace()

    print(f"the sum of the power of these sets is ")

def is_number(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False




if __name__ == "__main__":
    file = sys.argv[1]

    read_schematic(file)
