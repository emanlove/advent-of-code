import sys

def read_condition_records(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    for line in lines:
        symbolic,numeric = line.split()
        n_record = [int(n) for n in numeric.split(',')]

        len_record = len(symbolic)
        num_nrecords = len(n_record)
        sum_nrecords = sum(n_record)
        print(f"{line}  {len_record}  {sum_nrecords}  {num_nrecords}  {len_record-(sum_nrecords+num_nrecords-1)}")
        # import pdb;pdb.set_trace()

    print(f"The sum of how many different arrangements is ")


if __name__ == "__main__":
    file = sys.argv[1]

    read_condition_records(file)
