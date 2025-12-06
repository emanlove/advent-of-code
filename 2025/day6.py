import sys
import math

def read_math_problems(filename):

    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    math_problems = []
    for line in lines:
        math_problems.append([d for d in line.split(' ') if d])

    return math_problems

def perform_cephalopod_math(problems):
    results = []
    num_problems = len(problems[0])
    for indx in range(num_problems):
        op = problems[-1][indx]
        data = [int(s[indx]) for s in problems[:-1]]
        match op:
            case '*':
                result = math.prod(data)
            case '+':
                result = sum(data)
        results.append(result)

    return sum(results)

if __name__ == "__main__":
    file = sys.argv[1]

    data = read_math_problems(file)
    total = perform_cephalopod_math(data)
    print(f"The total result of the math problems is {total}")
