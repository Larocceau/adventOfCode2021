import sys

attributes = sys.argv

fileName  = attributes.pop(1)
file = open(fileName)

risk = 0


data = [[{"depth": int(item), "lowPoint": True} for item in line[:-1]] for line in file]

for locations, topLocations  in zip(data,[[None]*len(data[0])] + data[:-1]):

    for location, previousLocation, topLocation in zip( locations, [None] + locations[:-1], topLocations):
        for adjecentLocation in [previousLocation, topLocation]:
            if adjecentLocation:
                if adjecentLocation["depth"] > location["depth"]:
                    adjecentLocation["lowPoint"] = False
                else:
                    location["lowPoint"] = False


for row in data:
    for depth in row:
        risk +=  depth["depth"]+1 if depth["lowPoint"] else 0

print("risk: ", risk)
