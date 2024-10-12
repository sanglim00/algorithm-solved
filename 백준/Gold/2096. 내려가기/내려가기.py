import sys

N = int(sys.stdin.readline())

dp = [[0, 0, 0], [0, 0, 0]]
dp2 = [[0, 0, 0], [0, 0, 0]]

a, b, c = map(int, sys.stdin.readline().split())

dp[0][0] = dp2[0][0] = a
dp[0][1] = dp2[0][1] = b
dp[0][2] = dp2[0][2] = c

for _ in range(1, N):
    a, b, c = map(int, sys.stdin.readline().split())

    dp[1][0] = max(dp[0][0], dp[0][1]) + a
    dp[1][1] = max(max(dp[0][0], dp[0][1]), dp[0][2]) + b
    dp[1][2] = max(dp[0][1], dp[0][2]) + c

    dp2[1][0] = min(dp2[0][0], dp2[0][1]) + a
    dp2[1][1] = min(min(dp2[0][0], dp2[0][1]), dp2[0][2]) + b
    dp2[1][2] = min(dp2[0][1], dp2[0][2]) + c

    dp[0][0] = dp[1][0]
    dp[0][1] = dp[1][1]
    dp[0][2] = dp[1][2]

    dp2[0][0] = dp2[1][0]
    dp2[0][1] = dp2[1][1]
    dp2[0][2] = dp2[1][2]

print(max(dp[0]), min(dp2[0]))