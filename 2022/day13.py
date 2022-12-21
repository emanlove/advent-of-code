import sys

def read_packets(filename):
    with open(filename,'r') as fh:
        data = fh.readlines()
    
    packet_strs = ''.join(data).split('\n\n')
    pair_strs = [p.split('\n') for p in packet_strs]
    packets = [eval(s) for pair in pair_strs for s in pair]
    pair_of_packets = [packets[x:x+2] for x in range(0,len(packets),2)]
    # .. such ugly parsing

    return pair_of_packets

def compare(left,right,is_inorder):
    if is_inorder == False:
        return is_inorder
    
    for lindx,litem in enumerate(left):
        # check if right runs out of items first
        if lindx == len(right):
            is_inorder = False
            return is_inorder

        ritem = right[lindx]

        if (isinstance(litem,list) and isinstance(ritem,list)):   # .. thinking here I may zip up left and right
            is_inorder = compare(litem,right[lindx],is_inorder)
        elif (isinstance(litem,int) and isinstance(ritem,int)):
            if litem > ritem:
                is_inorder = False
                return is_inorder
        else:
            if isinstance(litem,int):
                litem = [litem]
            if isinstance(ritem,int):
                ritem = [ritem]
            
            is_inorder = compare(litem,ritem,is_inorder)

    return is_inorder

if __name__ == "__main__":
    file = sys.argv[1]

    packets  = read_packets(file)

    num_of_packets_in_right_order = 0
    packets_in_right_order = []
    for pindx,pair in enumerate(packets):
        # import pdb;pdb.set_trace()
        inorder = compare(pair[0],pair[1],True)
        if inorder:
            num_of_packets_in_right_order += 1
            packets_in_right_order.append(pindx+1)
    
    print(f"The number of packets that are in the right order is {num_of_packets_in_right_order}")
    print(f"The packets that are in the right order are {packets_in_right_order}")
    part1_ans = sum(packets_in_right_order)

    # print(f"The total number of unique positions the last knot visited is {num_unique_pos_last_knot_visited}")
    # part2_ans = num_unique_pos_last_knot_visited

    if len(sys.argv) >= 3:
        if int(sys.argv[2]) == part1_ans:
            print(f"Answer for part 1 is correct!")
    if len(sys.argv) == 4:
        if int(sys.argv[3]) == part2_ans:
            print(f"Answer for part 2 is correct!")

