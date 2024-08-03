import sys

N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    lst.append(row)

if N == 1:
    print(lst[0][0])
else:
    dp = [[0]*i for i in range(1, 500+1)]

    dp[0][0] = lst[0][0]
    dp[1][0] = dp[0][0] + lst[1][0]
    dp[1][1] = dp[0][0] + lst[1][1]

    for i in range(2, N):
        dp[i][0]=dp[i-1][0]+lst[i][0]
        for j in range(1, len(lst[i])-1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+lst[i][j]
        dp[i][-1]= dp[i-1][-1]+lst[i][-1]
        
    print(max(dp[N-1]))