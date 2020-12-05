def isValid(number):
    hasTwoAdjacent = False
    digits = list(str(number))

    pairs = list(zip(digits[:-1],digits[1:]))
    
    for pair in pairs:
        if pair[1] < pair[0]:
            return False
        if pair[0]==pair[1]:
            hasTwoAdjacent = True

    return hasTwoAdjacent

def isValidWithComplexRules(number):
    hasTwoAdjacent = [None] * 9
    counts = [0] * 9
    digits = list(str(number))

    pairs = list(zip(digits[:-1],digits[1:]))

    for pair in pairs:
        if pair[1] < pair[0]:
            return False

    for digit in digits:
        counts[int(digit)-1] += 1

    return any(True for c in counts if c==2)

if __name__ == "__main__":

    first=254032
    last=789860

    numbers = list(range(first,last+1))

    numValidNumbers = 0
    numValidNumbersWithComplexRules = 0
    for number in numbers:
        if isValid(number):
            numValidNumbers +=1
        if isValidWithComplexRules(number):
            numValidNumbersWithComplexRules += 1
    print(f"The number of valid numbers in the range is {numValidNumbers}")
    print(f"The number of valid numbers using the complex rule set is {numValidNumbersWithComplexRules}")
