import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]
dp[1] = N

check = False
for i in range(2, N+1):
    if dp[i-1]-3>=0:
        dp[i] = dp[i-1]-3
    else: dp[i] = dp[i-1]-1
    if dp[i]<=0: break
    check = not check

if check: print('CY')
else: print('SK')