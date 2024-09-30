import sys

N = int(sys.stdin.readline())

if N == 1:
    print(0, 1)
else:
    dpA = [0 for _ in range(N+1)]
    dpB = [0 for _ in range(N+1)]
    dpA[1] = 0
    dpB[1] = 1
    dpA[2] = 1
    dpB[2] = 1

    for i in range(3, N+1):
        dpA[i] = dpA[i-2]+dpA[i-1]
        dpB[i] = dpB[i-2]+dpB[i-1]

    print(dpA[N], dpB[N])