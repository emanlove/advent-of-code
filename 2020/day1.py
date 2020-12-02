import sys

def read_expence_report(filename):
    with open(filename,'r') as fh:
        line_items=[int(line.rstrip('\n')) for line in fh]

    return line_items

def find_2020_in_two(reciepts):

    for reciept in reciepts:
        this_reciept = [reciept] * len(reciepts)
        zipped = zip(this_reciept,reciepts)
        pairs = list(zipped)
        sum_pairs = [sum(pair) for pair in pairs]
        try:
            indx = sum_pairs.index(2020)
            return pairs[indx]
        except ValueError:
            pass
    return (None,None)

def find_2020_in_three(reciepts):

    for reciept_one in reciepts:
        for reciept in reciepts:
            reciept_two_list = [reciept] * len(reciepts)
            reciept_one_list = [reciept_one] * len(reciepts)
            zipped = zip(reciept_one_list,reciept_two_list,reciepts)
            triplets = list(zipped)
            sum_triplets = [sum(triplet) for triplet in triplets]
            #print(f"{reciept_one},{reciept}:{sum_triplets}")
            try:
                indx = sum_triplets.index(2020)
                return triplets[indx]
            except ValueError:
                pass
    return (None,None,None)

if __name__ == "__main__":
    file = sys.argv[1]
    report = read_expence_report(file)
    (a,b) = find_2020_in_two(report)
    print(f"The two expenses are: {a}, {b} and their product is {a*b}")
    (a,b,c) = find_2020_in_three(report)
    print(f"The three expenses are: {a}, {b}, {c} and their product is {a*b*c}")
