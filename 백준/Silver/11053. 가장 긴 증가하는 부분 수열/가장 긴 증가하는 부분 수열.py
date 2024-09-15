import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i):
        if A[j] < A[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))