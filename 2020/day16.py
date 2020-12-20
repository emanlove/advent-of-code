import sys

def read_notes(filename):

    rules = {}
    nearby_tickets = []
    with open(filename,'r') as notes:
        for line in notes:
            if line.startswith('your ticket'):
                my_ticketStr = next(notes)
                my_ticket = [int(field) for field in my_ticketStr.rstrip('\n').split(',')]
            elif line.startswith('nearby tickets'):
                #while True:
                #    next_ticket = next(notes)
                #    #yield next_ticket
                #    nearby_tickets.append(next_ticket.rstrip('\n'))
                next_ticket = next(notes)
                while next_ticket:
                    fieldsStr = next_ticket.rstrip('\n').split(',')
                    nearby_tickets.append([int(field) for field in fieldsStr])
                    try:
                        next_ticket = next(notes)
                    except StopIteration:
                        break
            else:
                rule,*ranges = line.rstrip('\n').split(': ')
                if ranges:
                    # assuming (as input and test dates does) every rule has `... or ...`
                    lower,upper = ranges[0].split(' or ')
                    lstart,lend = lower.split('-')
                    ustart,uend = upper.split('-')
                    rules[rule]=list(range(int(lstart),int(lend)+1)) + list(range(int(ustart),int(uend)+1))

    return rules,my_ticket,nearby_tickets

if __name__ == "__main__":
    file = sys.argv[1]

    rules,my_ticket,nearby_tickets = read_notes(file)

    all_rules = [value for rule in rules for value in rules[rule]]
    all_rules_unique = list(set(all_rules))

    error_rate = 0
    valid_nearby_tickets = []
    for nearby_ticket in nearby_tickets:
        all_fields_valid = True
        for field in nearby_ticket:
            if field not in all_rules_unique:
                error_rate += field
                all_fields_valid = False
        if all_fields_valid:
            valid_nearby_tickets.append(nearby_ticket)
            
    print(f"The ticket scanning error rate is {error_rate}")

    ordered_ticket_fields = []
    for position,value in enumerate(my_ticket):
        fieldValues = [value] + [nearby_ticket[position] for nearby_ticket in valid_nearby_tickets]

        for rule in rules:
            # Here I prefer to pop the dictionary value but that is not possible. So instead
            # I just check to see if this rule is already accepted.
            if rule in ordered_ticket_fields:
                continue
            if all(True if fieldValue in rules[rule] else False for fieldValue in fieldValues):
                #rules.pop(rule)  #
                ordered_ticket_fields.append(rule)
            
    print(f"The ticket fields are {ordered_ticket_fields}")
    print(f"Your ticket: {[(field,my_ticket[index]) for index,field in enumerate(ordered_ticket_fields)]}")
