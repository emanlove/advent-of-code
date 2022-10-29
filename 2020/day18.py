import sys
import re

def solve(exp):
    tight = exp.replace(' ','')
    # lft = char_indexs(exp,'(')
    # rgt = char_indexs(exp,')')
    exp_indxd_w_spaces=re.split('([\(\+\*\)])',tight)
    exp_indxd=[i for i in exp_indxd_w_spaces if i !=' ']

    lft = char_indexs(exp_indxd,'(')
    rgt = char_indexs(exp_indxd,')')

    initial_pairs_zipped = zip(lft,rgt)
    initial_pairs=list(initial_pairs_zipped)

    #import pdb;pdb.set_trace()

    if initial_pairs:
        sorted=sort_pairs(initial_pairs)
        print(f"{exp}: {sorted}")

    return 0
# def sort_pairs(pairs,start_indx):
#     sorted_pairs = []
#     for current_pair in pairs[start_indx:]:
#         if current_pair[0] < 

def sort_pairs(pairs):
    print(f"{pairs}")
    sorted_pairs = [pairs[0]]
    print(f"{sorted_pairs}")
    for indx in range(1,len(pairs)):        
        if pairs[indx][0] < sorted_pairs[indx-1][1]:
            if pairs[indx][1] < sorted_pairs[indx-1][1]:
                sorted_pairs.append((sorted_pairs[indx-1][0],sorted_pairs[indx-1][1]))
                sorted_pairs[indx-1]=(pairs[indx][0],pairs[indx][1])
                print(f"{sorted_pairs}")
            else:
                sorted_pairs.append((sorted_pairs[indx-1][0],pairs[indx][1]))
                sorted_pairs[indx-1]=(pairs[indx][0],sorted_pairs[indx-1][1])
                print(f"{sorted_pairs}")
        else:
            sorted_pairs.append((pairs[indx][0],pairs[indx][1]))
            print(f"{sorted_pairs}")
    return sorted_pairs

# def sort_pairs(pairs):
#     print(f"{pairs}")
#     sorted_pairs = [pairs[0]]
#     print(f"{sorted_pairs}")
#     for indx in range(1,len(pairs)):        
#         if pairs[indx][0] < pairs[indx-1][1]:
#             if pairs[indx][1] < pairs[indx-1][1]:
#                 sorted_pairs[indx-1]=(pairs[indx][0],pairs[indx][1])
#                 sorted_pairs.append((pairs[indx-1][0],pairs[indx-1][1]))
#                 print(f"{sorted_pairs}")
#             else:
#                 sorted_pairs[indx-1]=(pairs[indx][0],pairs[indx-1][1])
#                 sorted_pairs.append((pairs[indx-1][0],pairs[indx][1]))
#                 print(f"{sorted_pairs}")
#         else:
#             sorted_pairs.append((pairs[indx][0],pairs[indx][1]))
#             print(f"{sorted_pairs}")
#     return sorted_pairs
    
    # for symbol in exp_indxd:
    #     if symbol=='(':
    #         pass
    #     elif symbol==')':


    # import pdb;pdb.set_trace()

def char_indexs(string, char):
    return [indx for indx, c in enumerate(string) if c==char]

def read_expression(filename):
    with open(filename,'r') as fh:
        expressions = [line.rstrip('\n') for line in fh]

    return expressions

if __name__ == "__main__":
    file = sys.argv[1]

    math_expressions = read_expression(file)
    results = []
    for expression in math_expressions:
        result = solve(expression)
        results.append(result)
    print(f"The sum of the resultuing values is {sum(results)}")