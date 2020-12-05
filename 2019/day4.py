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

if __name__ == "__main__":

    first=254032
    last=789860
    
    numbers = list(range(first,last+1))
    
    numValidNumbers = 0
    for number in numbers:
        if isValid(number):
            numValidNumbers +=1
    
    print(f"The number of valid numbers in the range is {numValidNumbers}")
