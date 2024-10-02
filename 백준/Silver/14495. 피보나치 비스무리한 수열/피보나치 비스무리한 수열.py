import sys

N = int(sys.stdin.readline())

if N< 3: print(1)
else:
    dp = [0 for _ in range(N)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for i in range(3, N):
        dp[i] = dp[i-3]+dp[i-1]

    print(dp[-1])