import sys

attributes = sys.argv

fileName  = attributes.pop(1)
file = open(fileName)

crabs = [int(value) for value in file.read().split(",")]


calcComplicatedCost = lambda cost: 1/2*(cost-1) * cost + cost


simpleCost = [0]*max(crabs)
complexCost = [0]*max(crabs)

for crab in crabs:
    for pointId in range(len(simpleCost)):
        simpleCost[pointId] += abs(crab-pointId)
        complexCost[pointId] += calcComplicatedCost(abs(crab-pointId))

print("best simple fuel consumption: ", min(simpleCost))
print("best complex fuel consumption: ", min(complexCost))
