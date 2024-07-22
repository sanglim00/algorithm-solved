import sys

N = int(sys.stdin.readline())

for _ in range(N):
    dp = [0 for _ in range(11)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[4] = 7

    num = int(sys.stdin.readline())

    for i in range(5, num+1):
        sum_ = 0
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[num])