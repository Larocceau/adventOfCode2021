import sys

def neighbours(cord, list):
    locations = [(cord[0], cord[1]+1), (cord[0], cord[1]-1), (cord[0]-1, cord[1]),(cord[0]+1, cord[1])]
    for location in locations:
        if location[0] >= 0 and location[1] >=0:
            try:
                print(list[location[0]][location[1]])
                yield list[location[0]][location[1]]
            except IndexError:
                pass



attributes = sys.argv

fileName  = attributes.pop(1)
file = open(fileName)
grid = []

for line in file:
    grid.append([int(item) for item in list(line)[:-1]])

for line in grid:
    print(line)

sumOfLows = 0

for line in range(len(grid)):
    for position in range(len(grid[0])):
        positionValue = grid[line][position];
        if all([neighbour >positionValue for neighbour in neighbours((line, position), grid)]):
            print("new low of %i at (%i, %i)" % (positionValue, line, position))
            sumOfLows += positionValue +1

print("sum of lows :", sumOfLows)
