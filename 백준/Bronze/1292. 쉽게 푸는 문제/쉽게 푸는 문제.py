import sys

A, B = map(int, sys.stdin.readline().split())
arr = [0]

for i in range(1, B+1):
    for j in range(i):
        arr.append(i)

print(sum(arr[A:B+1]))
