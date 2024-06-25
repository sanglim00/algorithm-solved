import sys

N, M = map(int, sys.stdin.readline().split())

setCostMin = 1001
costMin = 1001

for i in range(M):
    many, one = map(int, sys.stdin.readline().split())
    setCostMin = min(setCostMin, many)
    costMin = min(costMin, one)

ans = N // 6 * setCostMin
ans += N % 6 * costMin
ans2 = (N // 6 + 1) * setCostMin
ans3 = N * costMin

print(min(min(ans, ans2), ans3))
