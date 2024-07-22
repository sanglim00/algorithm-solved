import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(1000+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5

for i in range(5, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N]%10007)
