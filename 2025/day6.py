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

def read_math_problems_as_cephalopod(filename):

    # assumes all lines are same length
    # my editor would add spaces at end of my test data file
    # and thus incorrectly calculates part 2 for that data file
    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    operators = lines[-1]
    operator_columns = [(indx,oper) for indx,oper in enumerate(operators) if oper !=' ']

    indexs = [indx for indx,_ in operator_columns] + [len(lines[0])]
    problem_columns = [(s,e) for s,e in zip(indexs[:-1],indexs[1:])]
    problem_map = [(r,o) for r,o in zip(problem_columns, [o for _, o in operator_columns])]

    print(f"{problem_map}")
    results = []
    for problem in problem_map:
        data = []
        start,end, oper = problem[0][0], problem[0][1], problem[1]
        for col in range(start,end):
            digit_str = ''.join([l[col] for l in lines[:-1]])
            digit_str = digit_str.strip()
            if digit_str:
                data.append(int(digit_str))
        print(f"{oper} {data}")
        match oper:
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
    true_data = read_math_problems_as_cephalopod(file)
    print(f"The total result using cephalopod math is {true_data}")
