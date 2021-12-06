def calculateNumberOfChanges(values, frameSize):
    decrements = 0;
    increments = 0;

    for index in range(0,len(values)-frameSize):

        if values[index+frameSize] < values[index]:
            decrements += 1

        elif values[index+frameSize] > values[index]:
            increments += 1

    return increments, decrements





import sys
attributes = sys.argv

fileName  = attributes.pop(1)
frameSize = int(attributes.pop(1))
file = open(fileName)

lines = file.readlines();
values = list(map(lambda line: int(line), lines))

result = calculateNumberOfChanges(values, frameSize)

print(values);
print("total datapoints: %i" % len(values))
print("increments: %s" % result[0])
print("decrements: %s" % result[1])
