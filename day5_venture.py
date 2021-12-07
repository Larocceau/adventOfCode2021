import sys

attributes = sys.argv

fileName  = attributes.pop(1)
file = open(fileName)

lineToPoints = lambda line: [[ int(point) for point in points.split(",")] for points in line.split("->")]

class Grid:
    grid = [[0]]
    def __str__(self):
        output = ""
        for line in self.grid:
            output += ("".join([str(item)if item is not 0 else "." for item in line])+"\n")
        return output

    def countCrossings(self):
        crossings = 0;
        for line in self.grid:
            for point in line:
                if point >1:
                    crossings +=1
        return crossings

    def insertPoint(self, point):
        x = point[0]
        y = point[1]
        try:
            self.grid[y][x] +=1
        except IndexError as e:
            while len(self.grid)<=y:
                self.grid.append([0]*len(self.grid[0]))
            while len(self.grid[-1])<=x:
                for lines in self.grid:
                    lines.append(0);
            self.grid[y][x] +=1

    def insertLine(self, point1, point2):
        if point1[0] == point2[0]:
            for index in range(min(point1[1], point2[1]), max(point1[1], point2[1])+ 1):
                point = (point1[0], index)
                grid.insertPoint(point)
        elif point1[1] == point2[1]:
            for index in range(min(point1[0], point2[0]), max(point1[0], point2[0])+1):
                grid.insertPoint((index, point1[1]))
        else:
            print(point1, point2)
            startPoint, endPoint = (point1, point2)if point1[0] < point2[0] else (point2, point1)
            grade = (endPoint[1] - startPoint[1])/(endPoint[0]-startPoint[0])
            for index in range(endPoint[0]  -  startPoint[0]+1):
                grid.insertPoint((startPoint[0]+index, int(startPoint[1]+index*grade)))





grid = Grid()
for line in file:
    grid.insertLine(*lineToPoints(line))



print(grid)
print(grid.countCrossings())
