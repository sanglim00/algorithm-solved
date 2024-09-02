import sys

N = int(sys.stdin.readline())
lst = []

for i in range(1, N+1):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y, i])

for i in range(len(lst)):
    num = 1
    for j in range(len(lst)):
        if i == j: continue
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            num += 1
    lst[i].append(num)

for i in lst: print(i[3], end=" ")
print()