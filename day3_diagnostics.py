import sys
attributes = sys.argv

fileName  = attributes.pop(1)
file = open(fileName)

getLineContent = lambda line: [int(digit) for digit in line[:-1]]

totals =  getLineContent(file.readline())
length = 1


for line in file:
    length +=1
    content = getLineContent(line)
    for(index, value) in enumerate(content):
        totals[index]+=value

gamma = 0;
epsilon = 0;

worth = 1
for total in reversed(totals):
    if total > .5*length:
        gamma += worth
    else:
        epsilon += worth
    worth *= 2

print("gamma", gamma)
print("epsilon", epsilon)
print("consumption", gamma*epsilon)
