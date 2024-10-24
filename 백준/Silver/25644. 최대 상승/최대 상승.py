N = int(input())
stock = list(map(int, input().split()))

dp = [0 for _ in range(200001)]
min_ = stock[0]

for i in range(1, N):
    dp[i] = max(dp[i], stock[i]-min_)
    min_ = min(min_, stock[i])

print(max(dp))