import sys

lst = []
N = int(sys.stdin.readline())

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y])

lst.sort(key=lambda x :(x[0], x[1]))
for i in lst: print(i[0], i[1])
