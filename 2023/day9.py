import sys

def read_OASIS_report(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    next_values = []
    for line in lines:
        history = [int(item) for item in line.split()]
        last = [history[-1]]
        while not all_zeros(history):
            history = [history[indx+1]-history[indx] for indx,_ in enumerate(history[:-1])]
            # print(f"{history}")
            last.append(history[-1])
        # print(f"{last}")
        next_values.append(sum(last))

    print(f"The sum of the extrapolated values is {sum(next_values)}")

def all_zeros(dataset):
    return sum(dataset)==0

if __name__ == "__main__":
    file = sys.argv[1]

    read_OASIS_report(file)
