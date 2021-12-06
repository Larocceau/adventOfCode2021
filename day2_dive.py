import sys
attributes = sys.argv

fileName  = attributes.pop(1)
file = open(fileName)

lines = file.readlines();

def processLine(line):
    content = line.split(" ");
    if (len(content)>1):
        return content[0], int(content[1][:-1])


itemMap = map(processLine, lines);
movements = list(filter(lambda item: item is not None, itemMap))

forward = 0;
vertical =0;
complexVertical = 0;

for movement in movements:
    if movement[0] == "forward":
        forward += movement[1]
        complexVertical += vertical*movement[1]
    elif movement[0] == "down":
        vertical += movement[1]

    else:
        vertical -= movement[1]

print("forward: ", forward)

print("\nvertical: ", vertical)
print("product: ", forward*vertical)

print("\ncomplex vertical: ", complexVertical)
print("complex product: ", forward*complexVertical)
