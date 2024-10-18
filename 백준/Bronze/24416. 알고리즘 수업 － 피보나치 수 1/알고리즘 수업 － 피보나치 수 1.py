N = int(input())

dp_= 0
def fibonacci(n):
    global dp_
    dp = [0 for _ in range(N+1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        dp_ += 1
        dp[i] = dp[i-2] + dp[i-1]

    return dp[N]

print(fibonacci(N), dp_)