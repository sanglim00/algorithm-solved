T = int(input())

dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1


for _ in range(T):
    N = int(input())

    if N < 3:
        print(dp[N])
        continue

    for i in range(4, N+1):
        dp[i] = dp[i-3]+dp[i-2]
    
    print(dp[N])