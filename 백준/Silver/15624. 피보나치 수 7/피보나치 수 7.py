import sys

N = int(sys.stdin.readline())
if N < 2: print(N)
else:
    dp = [0 for _ in range(N+1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, N+1):
        dp[i] = (dp[i-2]+dp[i-1])%1000000007

    print(dp[-1])