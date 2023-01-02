import sys
from copy import deepcopy

def read_encrypted_file(filename):
    with open(filename,'r') as fh:
        encrypted_file = [line.rstrip('\n') for line in fh]
    
    # encrypted_file = [[int(pos) for pos in cord.split(',')] for cord in lines]

    return encrypted_file

if __name__ == "__main__":
    file = sys.argv[1]

    efile = read_encrypted_file(file)
    decrypted_file = deepcopy(efile)

    # print(f"{len(efile)}")
    # print(f"{decrypted_file}")
    for num in efile:
        indx = decrypted_file.index(num)
        move_by = int(num)
        # move_by -=  1 if move_by < 0 else 0
        decrypted_file.pop(indx)
        insert_at = (indx + move_by) % len(decrypted_file)
        # insert_at -= 1 if insert_at < 0 else 0
        decrypted_file.insert(insert_at,num)

        # print(f"{num} moves to {decrypted_file} = {indx} {move_by} {insert_at}")

    indx_0 = decrypted_file.index('0')
    th1000 = int(decrypted_file[(indx_0 + 1000) % len(efile)])
    th2000 = int(decrypted_file[(indx_0 + 2000) % len(efile)])
    th3000 = int(decrypted_file[(indx_0 + 3000) % len(efile)])
    print(f"1000th [{th1000}]   2000th [{th2000}]   3000th [{th3000}]")
    sum_grove_coordinates = th1000+th2000+th3000

    print(f"The sum of the three numbers that form the grove coordinates is {sum_grove_coordinates}")
    part1_ans = sum_grove_coordinates

    # print(f"The answer to part two is {0}")
    # part2_ans = 0

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

