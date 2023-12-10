import sys

def read_OASIS_report(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    print(f"Number of lines: {len(lines)}")    
    next_values = []
    for line in lines:
        # print("--------------------")
        history = [int(item) for item in line.split()]
        # print(f"{history}")
        # import pdb;pdb.set_trace()
        last = [history[-1]]
        while not all_zeros(history):
            history = [history[indx+1]-history[indx] for indx,_ in enumerate(history[:-1])]
            # print(f"{history}")
            last.append(history[-1])
        # print(f"{last}")        
        next_values.append(sum(last))
        last = []

    print(f"Number of values: {len(next_values)}")
    print(f"The sum of the extrapolated values is {sum(next_values)}")

def all_zeros(dataset):
    for item in dataset:
        if item != 0:
            return False
    return True
    # return all([1 for item in dataset if item==0])
    # return sum(dataset)==0

if __name__ == "__main__":
    file = sys.argv[1]

    read_OASIS_report(file)
