import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    num = float(sys.stdin.readline())
    lst.append(num)

dp = [0 for _ in range(N)]
dp[0] = lst[0]

for i in range(1, N):
    dp[i] = max(lst[i], dp[i-1]*lst[i])

print('%.3f' % max(dp))