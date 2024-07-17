import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y])

lst.sort(key=lambda x: (x[1], x[0]))
for x, y in lst: print(x, y)