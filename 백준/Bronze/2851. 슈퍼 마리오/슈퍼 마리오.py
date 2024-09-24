import sys

lst = []
for _ in range(10):
    num = int(sys.stdin.readline())
    lst.append(num)

dp = [0 for _ in range(10)]
dp[0] = lst[0]

ans = abs(dp[0]-100)
num = 0
for i in range(1, 10):
    dp[i] = dp[i-1]+lst[i]
    if ans >= abs(dp[i]-100):
        ans = abs(dp[i]-100)
        num = dp[i]

print(num if num else dp[0])