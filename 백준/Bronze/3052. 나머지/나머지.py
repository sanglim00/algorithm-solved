import sys

myDict = {}
for _ in range(10):
    num = int(sys.stdin.readline())
    if num%42 in myDict:
        myDict[num%42] += 1
    else:
        myDict[num%42] = 1

print(len(myDict))