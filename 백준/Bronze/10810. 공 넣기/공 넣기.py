import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0 for _ in range(N+1)]

for _ in range(M):
    start, end, num = map(int, sys.stdin.readline().split())
    for j in range(start, end+1):
        basket[j] = num

for i in range(1, N+1): print(basket[i], end=' ')
print()