import sys

N, M = map(int, sys.stdin.readline().split())

arrA = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    arrA.append(row)

arrB = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    arrB.append(row)

for i in range(N):
    for j in range(M):
        print(arrA[i][j] + arrB[i][j], end=' ')
    print()
