import sys

dp = [0 for _ in range(90+1)]
dp[0] = 0
dp[1] = 1
dp[2] = 1

num = int(sys.stdin.readline())

for i in range(3, num+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[num])
