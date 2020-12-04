"""

-  byr (Birth Year) - four digits; at least 1920 and at most 2002.
-  iyr (Issue Year) - four digits; at least 2010 and at most 2020.
-  eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
-  hgt (Height) - a number followed by either cm or in:
-      If cm, the number must be at least 150 and at most 193.
-      If in, the number must be at least 59 and at most 76.
-  hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
-  ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
-  pid (Passport ID) - a nine-digit number, including leading zeroes.
-  cid (Country ID) - ignored, missing or not.

"""
import sys, re

ALL_REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
NORTH_POLE_VALID_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def isValidBirthYear(value):
    match = re.fullmatch(r'^(\d\d\d\d)$',value)
    if not match:
        return False
    birthYear = int(match.group(0))

    return 1920 <= birthYear <= 2002

def isValidIssueYear(value):
    match = re.fullmatch(r'^(\d\d\d\d)$',value)
    if not match:
        return False
    issueYear = int(match.group(0))

    return 2010 <= issueYear <= 2020

def isValidExpirationYear(value):
    match = re.fullmatch(r'^(\d\d\d\d)$',value)
    if not match:
        return False
    expirationYear = int(match.group(0))

    return 2020 <= expirationYear <= 2030

def isValidHeight(value):
    match = re.fullmatch(r'^(\d+)(cm|in)$',value)
    if not match:
        return False

    heightStr,units = match.groups()
    height = int(heightStr)

    if units=='cm':
        return 150 <= height <= 193

    if units=='in':
        return 59 <= height <= 76

def isValidHairColor(value):
    match = re.fullmatch(r'^#([0-9a-f]{6})$',value)
    if not match:
        return False

    return True

def isValidEyeColor(value):
    match = re.fullmatch(r'^(amb|blu|brn|gry|grn|hzl|oth){1}$',value)
    if not match:
        return False

    return True

def isValidPassportID(value):
    match = re.fullmatch(r'^(\d{9})$',value)
    if not match:
        return False

    return True

def isPassportValid(passport):
    if not isValidBirthYear(passport['byr']):
        return False

    if not isValidIssueYear(passport['iyr']):
        return False

    if not isValidExpirationYear(passport['eyr']):
        return False

    if not isValidHeight(passport['hgt']):
        return False

    if not isValidHairColor(passport['hcl']):
        return False

    if not isValidEyeColor(passport['ecl']):
        return False

    if not isValidPassportID(passport['pid']):
        return False

    return True

def hasAllExpectedFields(passport):
    return all(1 if np_field in passport.keys() else 0 for np_field in NORTH_POLE_VALID_FIELDS)

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
        if hasAllExpectedFields(passport):
            numValidPassports += 1

    print(f'Number of "North Pole" valid passports: {numValidPassports}')

    numProperValidPassports = 0
    for passport in passports:
        if hasAllExpectedFields(passport) and isPassportValid(passport):
            numProperValidPassports += 1

    print(f'Number of deeply valid passports: {numProperValidPassports}')
