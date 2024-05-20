import sys

a, b = sys.stdin.readline().split()

myDict = {}
ans = 0
ansList = []

for i in range(int(a)):
    name = sys.stdin.readline()
    myDict[name] = 1

for i in range(int(b)):
    name = sys.stdin.readline()
    if name in myDict:
        ansList.append(name)
        ans += 1


ansList.sort()
print(ans)
for i in ansList:
    print(i.strip())