import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

myDict = {}
for i in A: myDict[i] = True
for i in B:
    print(1 if myDict.get(i, 0) else 0)


