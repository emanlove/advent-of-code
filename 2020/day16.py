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
    matching_fields = {}
    for position,value in enumerate(my_ticket):
        fieldValues = [value] + [nearby_ticket[position] for nearby_ticket in valid_nearby_tickets]

        for rule in rules:
            # Here I prefer to pop the dictionary value but that is not possible. So instead
            # I just check to see if this rule is already accepted.
            #if rule in ordered_ticket_fields:
            #    continue
            #import pdb;pdb.set_trace()
            if all(True if fieldValue in rules[rule] else False for fieldValue in fieldValues):
                #rules.pop(rule)  #
                ordered_ticket_fields.append(rule)
                if position not in matching_fields:
                    matching_fields[position] = []
                matching_fields[position].append(rule)
    print(f"The ticket fields are {ordered_ticket_fields}")
    #print(f"Your ticket: {[(field,my_ticket[index]) for index,field in enumerate(ordered_ticket_fields)]}")
    
    # sorted([(len(matching_fields[match]),matching_fields[match]) for match in matching_fields])

#>>> sm = sorted([(len(matching_fields[match]),matching_fields[match]) for match in matching_fields])
#>>> for m in sm:
#...    print(m)
#...
#(1, ['arrival platform'])
#(2, ['arrival platform', 'class'])
#(3, ['arrival platform', 'class', 'seat'])
#(4, ['arrival platform', 'class', 'seat', 'wagon'])
#(5, ['arrival platform', 'class', 'row', 'seat', 'wagon'])
#(6, ['arrival location', 'arrival platform', 'class', 'row', 'seat', 'wagon'])
#(7, ['arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'wagon'])
#(8, ['arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon'])
#(9, ['departure station', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon'])
#(10, ['departure station', 'departure platform', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon'])
#(11, ['departure station', 'departure platform', 'departure track', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon'])
#(12, ['departure location', 'departure station', 'departure platform', 'departure track', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon'])
#(13, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon'])
#(14, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon'])
#(15, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'train', 'type', 'wagon'])
#(16, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival platform', 'class', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon'])
#(17, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival platform', 'class', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone'])
#(18, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'class', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone'])
#(19, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'arrival track', 'class', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone'])
#(20, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'arrival track', 'class', 'duration', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone'])
#>>>
#>>> fa = []
#>>> fas = set(fa)
#>>> for s in sm:
#...     ss=set(s[1])
#...     u = ss - fas
#...     print(list(u))
#...
#['arrival platform']
#['class', 'arrival platform']
#['class', 'seat', 'arrival platform']
#['class', 'seat', 'wagon', 'arrival platform']
#['seat', 'wagon', 'row', 'class', 'arrival platform']
#['seat', 'wagon', 'row', 'class', 'arrival location', 'arrival platform']
#['seat', 'price', 'wagon', 'row', 'class', 'arrival location', 'arrival platform']
#['price', 'class', 'arrival location', 'arrival platform', 'seat', 'wagon', 'row', 'type']
#['price', 'class', 'arrival location', 'arrival platform', 'seat', 'wagon', 'row', 'departure station', 'type']
#['departure platform', 'price', 'class', 'arrival location', 'arrival platform', 'seat', 'wagon', 'row', 'departure station', 'type']
#['departure platform', 'departure track', 'price', 'class', 'arrival location', 'arrival platform', 'seat', 'wagon', 'row', 'departure station', 'type']
#['departure platform', 'departure location', 'departure track', 'price', 'class', 'arrival location', 'arrival platform', 'seat', 'wagon', 'row', 'departure station', 'type']
#['departure platform', 'departure location', 'departure track', 'price', 'class', 'arrival location', 'arrival platform', 'seat', 'wagon', 'row', 'departure date', 'departure station', 'type']
#['departure platform', 'departure location', 'departure track', 'price', 'class', 'arrival location', 'arrival platform', 'seat', 'wagon', 'row', 'departure time', 'departure date', 'departure station', 'type']
#['departure platform', 'departure location', 'departure track', 'price', 'train', 'class', 'arrival location', 'arrival platform', 'seat', 'wagon', 'row', 'departure time', 'departure date', 'departure station', 'type']
#['departure platform', 'departure location', 'price', 'class', 'arrival platform', 'wagon', 'departure date', 'departure station', 'type', 'departure track', 'train', 'arrival location', 'route', 'seat', 'row', 'departure time']
#['departure platform', 'departure location', 'price', 'class', 'arrival platform', 'wagon', 'zone', 'departure date', 'departure station', 'type', 'departure track', 'train', 'arrival location', 'route', 'seat', 'row', 'departure time']
#['departure platform', 'departure location', 'price', 'class', 'arrival platform', 'wagon', 'zone', 'departure date', 'departure station', 'type', 'departure track', 'train', 'arrival location', 'route', 'seat', 'arrival station', 'row', 'departure time']
#['departure platform', 'departure location', 'price', 'class', 'arrival platform', 'wagon', 'zone', 'departure date', 'departure station', 'type', 'departure track', 'train', 'arrival track', 'arrival location', 'route', 'seat', 'arrival station', 'row', 'departure time']
#['departure platform', 'departure location', 'price', 'class', 'arrival platform', 'wagon', 'zone', 'departure date', 'departure station', 'type', 'departure track', 'train', 'arrival track', 'arrival location', 'route', 'seat', 'duration', 'arrival station', 'row', 'departure time']
#>>> for s in sm:
#...     ss=set(s[1])
#...     u = ss - fas
#...     print(list(u))
#...     fa += list(u)
#...     fas = set(fa)
#...
#['arrival platform']
#['class']
#['seat']
#['wagon']
#['row']
#['arrival location']
#['price']
#['type']
#['departure station']
#['departure platform']
#['departure track']
#['departure location']
#['departure date']
#['departure time']
#['train']
#['route']
#['zone']
#['arrival station']
#['arrival track']
#['duration']
#>>> for i,s in enumerate(sm):
#...     ss=set(s[1])
#...     u = ss - fas
#...     print(f"{i}:{list(u)}")
#...     fa += list(u)
#...     fas = set(fa)
#...
#0:[]
#1:[]
#2:[]
#3:[]
#4:[]
#5:[]
#6:[]
#7:[]
#8:[]
#9:[]
#10:[]
#11:[]
#12:[]
#13:[]
#14:[]
#15:[]
#16:[]
#17:[]
#18:[]
#19:[]
#>>> fa = []
#>>> fas = set(fa)
#>>> sm
#[(1, ['arrival platform']), (2, ['arrival platform', 'class']), (3, ['arrival platform', 'class', 'seat']), (4, ['arrival platform', 'class', 'seat', 'wagon']), (5, ['arrival platform', 'class', 'row', 'seat', 'wagon']), (6, ['arrival location', 'arrival platform', 'class', 'row', 'seat', 'wagon']), (7, ['arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'wagon']), (8, ['arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon']), (9, ['departure station', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon']), (10, ['departure station', 'departure platform', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon']), (11, ['departure station', 'departure platform', 'departure track', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon']), (12, ['departure location', 'departure station', 'departure platform', 'departure track', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon']), (13, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon']), (14, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'type', 'wagon']), (15, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival platform', 'class', 'price', 'row', 'seat', 'train', 'type', 'wagon']), (16, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival platform', 'class', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon']), (17, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival platform', 'class', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone']), (18, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'class', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone']), (19, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'arrival track', 'class', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone']), (20, ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'arrival track', 'class', 'duration', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone'])]
#>>> for s in sm:
#...     ss=set(s[1])
#KeyboardInterrupt
#>>> for i,s in enumerate(sm):
#...     ss=set(s[1])
#...     u = ss - fas
#...     print(f"{i}:{list(u)}")
#...     fa += list(u)
#...     fas = set(fa)
#...
#0:['arrival platform']
#1:['class']
#2:['seat']
#3:['wagon']
#4:['row']
#5:['arrival location']
#6:['price']
#7:['type']
#8:['departure station']
#9:['departure platform']
#10:['departure track']
#11:['departure location']
#12:['departure date']
#13:['departure time']
#14:['train']
#15:['route']
#16:['zone']
#17:['arrival station']
#18:['arrival track']
#19:['duration']
#>>> my_ticket[9:14]
#[53, 89, 167, 227, 79]
#>>> my_ticket[8:14]
#[127, 53, 89, 167, 227, 79]
#>>> from functools import reduce
#>>> reduce(lambda x,y: x*y, my_ticket[8:14])
#1794068482849
#>>>

#>>> [(field,len(matching_fields[field])) for field in matching_fields]
#[(0, 1), (1, 8), (2, 7), (3, 4), (4, 10), (5, 3), (6, 15), (7, 17), (8, 6), (9, 5), (10, 12), (11, 16), (12, 20), (13, 2), (14, 11), (15, 14), (16, 18), (17, 13), (18, 9), (19, 19)]
#>>> my_ticket
#[223, 139, 211, 131, 113, 197, 151, 193, 127, 53, 89, 167, 227, 79, 163, 199, 191, 83, 137, 149]
#>>> d_fields=[my_ticket[i] for i in [1,18,4,14,10,17]]
#>>> from functools import reduce
#>>> reduce(lambda x,y: x*y, d_fields)
#2591012536579
#>>> d_fields
#[139, 137, 113, 163, 89, 83]
#>>>

# !! Corect Answer !!

#>>> d_fields=[my_ticket[i] for i in [18,4,14,10,17,15]]
#>>> d_fields
#[137, 113, 163, 89, 83, 199]
#>>> reduce(lambda x,y: x*y, d_fields)
#3709435214239
#>>>
