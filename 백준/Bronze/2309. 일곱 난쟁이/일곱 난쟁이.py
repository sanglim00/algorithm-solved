import sys

lst = []
for _ in range(9):
    num = int(sys.stdin.readline())
    lst.append(num)

lst.sort()
sum_ = sum(lst)-100

idx, idx2 = 0, 0
for i in range(9):
    for j in range(i, 9):
        if i == j: continue
        if lst[i] + lst[j] == sum_:
            idx, idx2 = i, j
            break

for i in range(9):
    if i != idx and i != idx2:
        print(lst[i])