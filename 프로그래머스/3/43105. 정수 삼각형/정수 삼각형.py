def solution(triangle):
    answer = 0
    N = len(triangle)
    
    dp = [[] for _ in range(N)]

    dp[0].append(triangle[0][0])
    dp[1].append(dp[0][0] + triangle[1][0])
    dp[1].append(dp[0][0] + triangle[1][1])

    for i in range(2, N):
        dp[i].append(dp[i-1][0]+triangle[i][0])
        for j in range(1, len(triangle[i])-1):
            dp[i].append(max(dp[i-1][j-1], dp[i-1][j])+triangle[i][j])
        dp[i].append(dp[i-1][-1]+triangle[i][-1])
    
    return max(dp[N-1])