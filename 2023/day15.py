import sys

def read_initialization_sequence(filename):
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

    read_initialization_sequence(file)
