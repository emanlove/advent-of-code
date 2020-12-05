import sys

def loadDeclarationForms(formfile):
    forms = []
    with open(formfile,'r') as fh:
        lines = fh.readlines()

    if lines[-1] != '\n':
        lines.append('\n')
        
    buffer = []
    for line in lines:
        if line =='\n':
            forms.append(buffer)
            buffer = []
        else:
            buffer.append(line.strip('\n'))
        
    return forms

def numQuestionsAnswerYesTo(group):
    numYes = 0
    a_zCHARS = [chr(ord('a')+i) for i in range(26)]

    individuals = [set(indv) for indv in group]
    agreedUponQuestions = list(individuals[0].intersection(*individuals))
    
    for question in agreedUponQuestions:
        if question in a_zCHARS:
            numYes += 1
            a_zCHARS.pop(a_zCHARS.index(question))

    return numYes

if __name__ == "__main__":
    file = sys.argv[1]

    declaration_forms = loadDeclarationForms(file)

    total_yeses = sum(numQuestionsAnswerYesTo(group) for group in declaration_forms)
    print(f"The total number of questions answered by all groups is {total_yeses}")
