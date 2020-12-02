import sys

def read_passwords(filename):
    with open(filename,'r') as fh:
        passwords = [line.rstrip('\n') for line in fh]

    return passwords

def password_check(passwords):
    num_correct_passwords = 0

    for password in passwords:
        rule,entry = password.split(': ')

        min_max,letter = rule.split()
        min,max = min_max.split('-')
        min_occurance = int(min)
        max_occurance = int(max)
        letter = rule[-1]

        if min_occurance <= entry.count(letter) <= max_occurance:
            num_correct_passwords += 1

    return num_correct_passwords

def proper_tobaggan_password_check(passwords):
    num_correct_passwords = 0

    for password in passwords:
        rule,entry = password.split(': ')

        pos1_pos2,letter = rule.split()
        pos1Str,pos2Str = pos1_pos2.split('-')
        pos1 = int(pos1Str)-1
        pos2 = int(pos2Str)-1
        letter = rule[-1]

        if (entry[pos1]==letter) ^ (entry[pos2]==letter):
            num_correct_passwords += 1

    return num_correct_passwords


if __name__ == "__main__":
    file = sys.argv[1]
    pwds = read_passwords(file)
    correct = password_check(pwds)
    print(f"There are {correct} correct passwords in the db.")

    proper = proper_tobaggan_password_check(pwds)
    print(f"There are {proper} proper passwords as per Toboggan Corp rules.")
