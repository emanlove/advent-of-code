import sys

def blindly_read_initialization_sequence(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    steps = lines[0].split(',')
    results = []
    for step in steps:
        result = run_HASH_algorithm(step)
        results.append(result)

    print(f"The sum of the results is {sum(results)}")

def run_HASH_algorithm(string):
    current = 0
    for char in string:
        ascii = ord(char)
        current += ascii
        current *= 17
        current %= 256

    return current

if __name__ == "__main__":
    file = sys.argv[1]

    blindly_read_initialization_sequence(file)

import re
from collections import OrderedDict

REMOVE = '-'
INSERT = '='

def read_initialization_sequence(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    steps = lines[0].split(',')

    boxes = {n:OrderedDict() for n in range(256)}
    for step in steps:
        hashed_box, focal_length_str = re.split('[-=]',step)
        operation = step[len(hashed_box)]   # might be able to get the matching char out of re
        box = run_HASH_algorithm(hashed_box)

        if operation == REMOVE:
            if hashed_box in boxes[box]:
                del boxes[box][hashed_box]
        elif operation == INSERT:
            focal_length = int(focal_length_str)
            boxes[box][hashed_box] = focal_length
        else:
            print(f"!!WARNING!! unknown operation - {operation}")

    focusing_power = []
    for zero_box_indx, box in enumerate(boxes):
        for zero_lense_indx, lense in enumerate(boxes[box]):
            lense_power = (zero_box_indx+1)*(zero_lense_indx+1)*boxes[box][lense]
            focusing_power.append(lense_power)
    
    print(f"The total focusing power of the resulting lens configuration is {sum(focusing_power)}")

if __name__ == "__main__":
    file = sys.argv[1]

    read_initialization_sequence(file)
