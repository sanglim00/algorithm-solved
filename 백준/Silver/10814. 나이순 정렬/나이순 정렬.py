import sys

lst = []
N = int(sys.stdin.readline())

for i in range(N):
    x, y = sys.stdin.readline().split()
    lst.append([x, y, i])

lst.sort(key=lambda x :(int(x[0]), x[2]))
for i in lst: print(i[0], i[1])
