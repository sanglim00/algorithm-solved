import sys

N = int(sys.stdin.readline())
colors = []
dp = [[0 for _ in range(3)] for _ in range(N)]

for i in range(N):
    color = list(map(int, sys.stdin.readline().split()))
    colors.append(color)

dp[0] = colors[0]
for i in range(1, N):
    dp[i][0] = colors[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = colors[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = colors[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))