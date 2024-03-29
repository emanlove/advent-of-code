import sys

def read_patterns(filename):
    patterns = []
    pattern =[]
    with open(filename,'r') as fh:
        next_line = fh.readline()
        while next_line:
            if next_line == '\n':
                patterns.append(pattern)
                pattern = []
            else:
                pattern.append(next_line.rstrip('\n'))
            next_line = fh.readline()

        patterns.append(pattern)

    return patterns

def find_reflectionPoint_and_score(pattern):
    reflection_indexes = []
    for lindx,line in enumerate(pattern[:-1]):
        if line == pattern[lindx+1] or has_one_difference(line,pattern[lindx+1]):
            reflection_indexes.append(lindx)
    
    if len(reflection_indexes)==0:
        # No reflection
        return None
    
    # if len(reflection_indexes)>1:
    #     print(f"Warning Local reflection; {reflection_indexes}")

    # Part 1 solution:
    # for index in reflection_indexes:
    #     reflect_index = check_reflection(pattern, index)
    #     if reflect_index is not None:
    #         return reflect_index
    # return None

    # Part 2 solution:
    for index in reflection_indexes:
        reflect_index,ndiffs = check_reflection_noting_num_of_diffs(pattern, index)
        if ndiffs == 1:
            return reflect_index
    return None

def check_reflection(pattern, index):
        reflection_index = index
        dist_to_start = reflection_index+1
        dist_to_end = len(pattern)-dist_to_start
        reflect_length = dist_to_end if dist_to_start > dist_to_end else dist_to_start
        # print(f"{len(pattern)}  {dist_to_start}  {dist_to_end}")
        for rindx in range(reflect_length):
            this = reflection_index-rindx; that = reflection_index+rindx+1
            if pattern[this] != pattern[that]:
                return None
        return dist_to_start

def has_one_difference(this,that):
    chars = zip(this,that)
    num_of_differences = sum([1 for c in chars if c[0]!=c[1]])
    if num_of_differences == 1:
        return True
    else:
        return False

def check_reflection_noting_num_of_diffs(pattern, index):
        reflection_index = index
        dist_to_start = reflection_index+1
        dist_to_end = len(pattern)-dist_to_start
        reflect_length = dist_to_end if dist_to_start > dist_to_end else dist_to_start
        # print(f"{len(pattern)}  {dist_to_start}  {dist_to_end}")
        num_of_differences = 0
        for rindx in range(reflect_length):
            this = reflection_index-rindx; that = reflection_index+rindx+1
            if pattern[this] != pattern[that]:
                chars = zip(pattern[this],pattern[that])
                num_of_differences += sum([1 for c in chars if c[0]!=c[1]])
        # print(f"{dist_to_start}  diffs:{num_of_differences}")
        return dist_to_start, num_of_differences

def transform(pattern):
    vertical = []
    nrows = len(pattern); ncols = len(pattern[0])
    flattened = ''.join(pattern)
    for vline in range(ncols):
        vertical.append([flattened[vline+(r*ncols)] for r in range(nrows)])
    return vertical

if __name__ == "__main__":
    file = sys.argv[1]

    patterns = read_patterns(file)
    
    scores = []
    for pattern in patterns:
        score = find_reflectionPoint_and_score(pattern)
        # print(f"{score}")
        if score is not None:
            scores.append(score*100)
        else:
            vertical_reflect = transform(pattern)
            score = find_reflectionPoint_and_score(vertical_reflect)
            if score is None:
                print("WARNING: Pattern has neither horizontal nor vertical reflection!")
            else:
                scores.append(score)

    print(f"The number do you get after summarizing all of your notes is {sum(scores)}")
