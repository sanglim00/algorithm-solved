import sys

myX = []
myY = []
for _ in range(3):
    x, y = map(int, sys.stdin.readline().split())
    if x in myX: myX.remove(x)
    else: myX.append(x)
    if y in myY: myY.remove(y)
    else: myY.append(y)

print(myX[0], myY[0])