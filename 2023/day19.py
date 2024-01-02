"""
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

in{s<1351:px,qqz}
px  s<1351
qqz s>=1351 (or s>1350)
...

in{s<1351:px,qqz}
px  s<1351
qqz s>1350
-------
Level 2
px{a<2006:qkq,m>2090:A,rfg}
 [px] qkq  [s<1351] a<2006
 [px] A    [s<1351] a>2005 m>2090
 [px] rfg  [s<1351] a>2005 m<2091
qqz{s>2770:qs,m<1801:hdj,R}
 [qqz] qs  [s>1350] s>2770
~[qqz] qs   s>2770
 [qqz] hdj [s>1350] s<2771 m<1801
 [qqz] A   [s>1350] s<2771 m>1800
-------
Level 3
qkq{x<1416:A,crn}
 [px qkq] A   [s<1351 a<2006] x<1416
 [px qkq] crn [s<1351 a<2006] x>1415
rfg{s<537:gd,x>2440:R,A}
 [px rfg] gd  [s<1351 a>2005 m<2091] s<537
~[px rfg] gd  [a>2005 m<2091] s<537
 [px rfg] R   [s<1351 a>2005 m<2091] s>536 x>2440
 [px rfg] A   [s<1351 a>2005 m<2091] s>536 x<2441
qs{s>3448:A,lnx}
 [qqz qs] A   [s>1350 s>2770] s>3448
~[qqz qs] A    s>3448
 [qqz qs] lnx [s>1350 s>2770] s<3449
hdj{m>838:A,pv}
 [qqz hdj] A  [s>1350 s<2771 m<1801] m>838
 [qqz hdj] pv [s>1350 s<2771 m<1801] m<839
-------
Level 4
crn{x>2662:A,R}
 [px qkq crn] A   [s<1351 a<2006 x>1415] x>2662
 [px qkq crn] R   [s<1351 a<2006 x>1415] x<2663
gd{a>3333:R,R}
 [px rfg gd] R   [s<1351 a>2005 m<2091 s<537] a>3333
 [px rfg gd] R   [s<1351 a>2005 m<2091 s<537] a<3334
~ any gd rejected
lnx{m>1548:A,A}
 [qqz qs lnx] A   [s>1350 s>2770 s<3449] m>1548
 [qqz qs lnx] A   [s>1350 s>2770 s<3449] m<1549
~ any lnx accepted
pv{a>1716:R,A}
 [qqz hdj pv] R   [s>1350 s<2771 m<1801 m<839] a>1716
 [qqz hdj pv] A   [s>1350 s<2771 m<1801 m<839] a<1717
"""
import sys
import re

def read_rules_and_parts(filename):
    with open(filename,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
    
    divider = [i for i,l in enumerate(lines) if l==''][0]

    # parse rules
    rules = {}
    for line in lines[:divider]:
        name,ruleset_line = line.split('{')
        rules[name] = []
        ruleset = ruleset_line[:-1].split(',')
        for rule in ruleset[:-1]:
            condition,action = rule.split(':')
            category,value = re.split('[<>]',condition)
            value = int(value)
            operation = condition[len(category)]
            r = {'cat': category, 'oper': operation, 'val': value}
            print(f"[ {rule} ]  {category}  {operation}  {value}  {action}")            
        final_action = ruleset[-1]
        print(f"{final_action}")
    
    # parse parts
    parts = []
    for line in lines[divider+1:]:
        categories = line[1:-1].split(',')
        part = {kv[0]:kv[1] for kv in (c.split('=') for c in categories)}
        # for c in categories:
        #     category, rating = c.split('=')
        #     rating = int(rating)
        parts.append(part)

    # import pdb;pdb.set_trace()
    for part in parts:

    print(f"the sum of the power of these sets is ")

if __name__ == "__main__":
    file = sys.argv[1]

    read_rules_and_parts(file)
    # import pdb;pdb.set_trace()
