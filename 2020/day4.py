import sys

ALL_REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
NORTH_POLE_VALID_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def loadPassports(passfile):
    passports = []
    with open(passfile,'r') as fh:
        lines = fh.readlines()

    buffer = ''
    for line in lines:
        if line =='\n':
            buffer = buffer.rstrip()
            pdict = passportLineToDict(buffer)
            passports.append(pdict)
            buffer = ''
        else:
            
            buffer += line.strip('\n')

            if not buffer.endswith(' '):
                buffer += ' '
        
    return passports

def passportLineToDict(pline):
    kvpairs = pline.split(' ')
    return dict([pair.split(':') for pair in kvpairs])
    
if __name__ == "__main__":
    file = sys.argv[1]

    passports = loadPassports(file)

    numValidPassports = 0
    for passport in passports:
        if all(1 if np_field in passport.keys() else 0 for np_field in NORTH_POLE_VALID_FIELDS):
            numValidPassports += 1

    print(f'Number of "North Pole" valid passports: {numValidPassports}')

