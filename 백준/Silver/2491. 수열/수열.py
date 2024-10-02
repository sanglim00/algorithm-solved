import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
max_dp = [1 for _ in range(N)]
min_dp = [1 for _ in range(N)]

for i in range(1, N):
    if lst[i-1] <= lst[i]:
        max_dp[i] = max_dp[i-1]+1
    if lst[i-1] >= lst[i]:
        min_dp[i] = min_dp[i-1]+1
        
max_ = max(max_dp)
min_ = max(min_dp)
print(max(max_, min_))