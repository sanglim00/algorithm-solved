import sys

N = int(sys.stdin.readline())
n_lst = list(map(int, sys.stdin.readline().split()))

myDict = {}
for i in n_lst:
    if i not in myDict:
        myDict[i] = 1

M = int(sys.stdin.readline())
m_lst = list(map(int, sys.stdin.readline().split()))

for i in m_lst:
    if i in myDict:
        print(myDict[i], end=' ')
    else:
        print(0, end=' ')
print()