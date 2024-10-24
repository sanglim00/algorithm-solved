N = int(input())

INF = float('INF')

dp = [INF for _ in range(100001)]
dp[2] = 1
dp[5] = 1

for i in range(4, N+1):
    if dp[i-2] != INF: dp[i] = min(dp[i], dp[i-2] + 1)
    if dp[i-5] != INF: dp[i] = min(dp[i], dp[i-5] + 1)
        
print(dp[N] if dp[N] != INF else -1)