import sys

def read_calibration(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    digits = []
    for line in lines:
        nums = [c for c in line if ord(c) < 58]
        digit = int(nums[0]+nums[-1])
        digits.append(digit)

    print(sum(digits))

NUMBER_STRINGS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                '1', '2', '3', '4', '5', '6', '7', '8', '9']
NUMBER_DICT = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9',
                '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
def read_spelled_out_cal(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    digits = []
    for line in lines:
        numstr_on_line = []
        for pos,char in enumerate(line):
            for nstr in NUMBER_DICT:
                l_nstr = len(nstr)
                if line[pos:pos+l_nstr] == nstr:
                    numstr_on_line.append(NUMBER_DICT[nstr])
        digit = int(numstr_on_line[0]+numstr_on_line[-1])
        digits.append(digit)

    print(sum(digits))

if __name__ == "__main__":
    file = sys.argv[1]

    #read_calibration(file)
    read_spelled_out_cal(file)
