import sys
attributes = sys.argv

fileName  = attributes.pop(1)
file = open(fileName)

getLineContent = lambda line: [int(digit) for digit in line[:-1]]

def mergeNumberArray(numberArray):
    return "".join([str(digit) for digit in numberArray])

def findByCommonBitRate(values):
    totals= [0]*len(values[0])
    for value in values:
        for i in range(len(value)):
            totals[i] += 1 if value[i] == 1 else -1;
    return [1 if total >0 else 0 for total in totals]

def findByBitCriteria(values, findFrequent=True, findLeastFrequent=False):

    total =0
    for value in values:
        total += 1 if value[0] == 1 else -1;

    frequentBit = 1 if total >= 0 else 0;

    candidFrequent = []
    candidNonFrequent = []


    for value in values:
        if value[0] ==frequentBit and findFrequent:
            candidFrequent.append(value[1:])
        elif value[0] != frequentBit and findLeastFrequent:
            candidNonFrequent.append(value[1:])

    frequent = None
    if findFrequent:
        frequent =  [frequentBit] + (candidFrequent[0] if len(candidFrequent)==1 else findByBitCriteria(candidFrequent));
    if findLeastFrequent:
        nonFrequent = [abs(frequentBit-1)] + (candidNonFrequent[0] if len(candidNonFrequent)==1 else findByBitCriteria(candidNonFrequent, False, True));

    if findFrequent and findLeastFrequent:
        return frequent, nonFrequent
    elif findFrequent:
        return frequent
    else:
        return nonFrequent


data = [getLineContent(line) for line in file]


oxygenArray, scrubberArray = findByBitCriteria(data, True, True)

oxygen = int(mergeNumberArray(oxygenArray),2)
scrubber = int(mergeNumberArray(scrubberArray),2)

gammaArray = findByCommonBitRate(data)
gamma = int(mergeNumberArray(gammaArray),2)
epsilon = int(mergeNumberArray([1 if digit == 0 else 0 for digit in gammaArray]),2)

print("Gamma: ", gamma)
print("Epsilon: ", epsilon)
print("Power consumption", gamma*epsilon)

print("\nOxygen: ", oxygen)
print("Scrubber: ", scrubber)
print("Life support: ", scrubber*oxygen)
