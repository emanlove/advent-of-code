import sys, copy

def read_xmas_data(filename):
    with open(filename,'r') as fh:
        xmas_data = [int(line.rstrip('\n')) for line in fh]

    return xmas_data

def matches_check_sum(check_sum,preamble):

    for nindex,number in enumerate(preamble):
        additors = copy.deepcopy(preamble)
        additors.pop(nindex)
        adding = [number] * len(additors)

        summations = [sum(pair) for pair in list(zip(additors,adding))]

        if any(total for total in summations if total==check_sum):
            return True

    return False

def matches_contiguous_set(expected_sum,data):
    """Brute Force Method for finding the contiguous sum.
    """
    start_pos = 0
    end_pos = 1
    contiguous_sum = 0
    
    while True:

        while (contiguous_sum < expected_sum) and (end_pos <= len(data)):
            contiguous_sum = sum(data[start_pos:end_pos])
            end_pos += 1
            print(f"{start_pos}:{end_pos}:{contiguous_sum}")
        
        if contiguous_sum == expected_sum:
            min_csum = min(data[start_pos:end_pos-1])
            max_csum = max(data[start_pos:end_pos-1])
            return min_csum,max_csum,data[start_pos],data[end_pos-1],start_pos,end_pos-1
        else:
            start_pos += 1
            end_pos = start_pos+1
            contiguous_sum = 0
            
        if start_pos > len(data):
            import pdb;pdb.set_trace()
        
if __name__ == "__main__":
    file = sys.argv[1]
    preambleLen = int(sys.argv[2])
    looking_for = int(sys.argv[3])

    xmas_data = read_xmas_data(file)

    start_pos = 0

    for check_pos in range(preambleLen,len(xmas_data)+1):
        preamble = xmas_data[check_pos-preambleLen:check_pos]
        check_sum = xmas_data[check_pos]

        if not matches_check_sum(check_sum,preamble):
            print(f"Unable to find pair to sum to {check_sum}")
            break

    csmin,csmax,sval,endval,spos,epos = matches_contiguous_set(looking_for,xmas_data)
    #print(f"The sum of the start and end contiguous set is {sval+endval}")
    print(f"The sum of the min and mx within contiguous set is {csmin+csmax}")
