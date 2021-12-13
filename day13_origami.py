import sys

attributes = sys.argv

fileName  = attributes.pop(1)
file = open(fileName)

folds = []
points = []

for line in file:
    if len(line) <=1:
        continue
    if "fold" in line:
        (axis, location) = line.split("=")
        folds.append({"axis":0 if "x" in axis else 1, "location":int(location)})
    else:
        (x, y) = line.split(",")
        points.append([int(x), int(y)])
print("points: ", len(points))


print("points: ", points)
print("folds: ", folds)

def show(points):
    maxX = max([point[0] for point in points])+1
    maxY= max([point[1] for point in points])+1

    for y in range(maxY):
        print("".join(["#" if [x,y] in points else " "  for x in range(maxX)]))

def foldPoint(point, fold):
    otherAxis = abs(fold["axis"]-1)

    if point[fold["axis"]] == fold["location"]:
        return None

    elif point[fold["axis"]] > fold["location"]:
        newPoint = [None,None]
        newPoint[otherAxis] = point[otherAxis]
        newPoint[fold["axis"]] = point[fold["axis"]] - 2*(point[fold["axis"]]-fold["location"])


        return newPoint

    return point

def fold(points, fold):
    output = []
    for point in points:
        folded = foldPoint(point, fold)
        if folded is not None and folded not in output:
            output.append(folded)
    return output




for instruction in folds:
    points = fold(points, instruction)

show(points)
