import sys

N, M = map(int, sys.stdin.readline().split())
basket = [i for i in range(N+1)]

for _ in range(M):
    c1, c2 = map(int, sys.stdin.readline().split())
    basket[c1], basket[c2] = basket[c2], basket[c1]

for i in range(1, N+1):
    print(basket[i], end=' ')
print()