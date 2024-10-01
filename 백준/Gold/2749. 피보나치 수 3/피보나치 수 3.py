import sys

N = int(sys.stdin.readline())
dp = {}
dp[0] = 0
dp[1] = 1

mod = 10**6
p = mod//10*15

for i in range(2, p):
    dp[i] = (dp[i-2]+dp[i-1])%mod

print(dp[N%p])