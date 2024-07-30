import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

str_ = str(A*B*C)
myDict = {}

for i in str_:
    if i in myDict: myDict[i] += 1
    else: myDict[i] = 1

for i in range(10):
    if str(i) in myDict: print(myDict[str(i)])
    else: print(0)