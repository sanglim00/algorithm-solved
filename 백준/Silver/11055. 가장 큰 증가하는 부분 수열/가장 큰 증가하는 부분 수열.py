import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]
dp[0] = lst[0]

for i in range(1, N):
    for j in range(i):
        if lst[j] < lst[i]: 
            dp[i] = max(dp[i], dp[j]+lst[i])
    dp[i] = max(dp[i], lst[i])

print(max(dp))