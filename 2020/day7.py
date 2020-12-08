import sys

def loadBaggageRules(rulesfile):
    rules = {}
    with open(rulesfile,'r') as fh:
        lines = [line.rstrip('\n') for line in fh]
        #lines = fh.readlines()

    #import pdb;pdb.set_trace()
    for line in lines:
        parent_bags, children_bags = line.split(' contain ')
        *padj,bags = parent_bags.split()
        parent = ''.join(padj)
        rules[parent] = []
         
        child_bags = children_bags.split(',')
        for child_bag in child_bags:
            try:
                child_bag = child_bag.rstrip('.')
                if child_bag.startswith('no other bags'):
                    #import pdb;pdb.set_trace()
                    continue
                countStr,*cadj,bags = child_bag.split()
                count = int(countStr)
                child = ''.join(cadj)
                if child not in rules[parent]:
                    rules[parent].append(child)
                else:
                    print(f"Unexpected rule: Multiple child definitions ({child}) in {parent}")
            except:
                import pdb;pdb.set_trace()
    
    return rules
                 
#def findUniqueNumOutermostBagColors(given_bag,rules):
#    # Initial bas which contain given_bag
#    [
#    for parent_bags in rules:
#        if
#    pass


def bagParents(bag,rules):
    parents = []
    for rule in rules:
        if bag in rules[rule]:
            parents.append(rule)
    return parents

def outmostBag(bag,rules):
    parents = []
    for rule in rules:
        if bag in rules[rule]:
            parents.append(rule)

    if not parents:
        pass
    
def outmostBags(bag,rules):
    outerbags = []
    parents = []
    for rule in rules:
        if bag in rules[rule]:
            parents.append(rule)

    if not parents:
        pass
    
if __name__ == "__main__":
    file = sys.argv[1]

    baggage_rules = loadBaggageRules(file)

    outerbags = []
    needtofindaparent = ['shinygold']

    #import pdb;pdb.set_trace()
    while len(needtofindaparent) > 0:
        child = needtofindaparent.pop()

        parents = bagParents(child,baggage_rules)
        if not parents:
            if child not in outerbags:
                outerbags.append(child)
        else:
            for parent in parents:
                if parent not in outerbags:
                    outerbags.append(parent)
            needtofindaparent += parents

    print(f"The outermost bags include {outerbags}:{len(outerbags)}.")
