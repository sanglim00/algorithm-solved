def solution(m, n, puddles):
    answer = 0
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i, j in puddles:
        dp[j][i] = -1
        
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if dp[i][j] == -1: continue
            
            if dp[i-1][j] != -1: dp[i][j] += dp[i-1][j] 
            if dp[i][j-1] != -1: dp[i][j] += dp[i][j-1]
            
            dp[i][j] %= 1000000007

    answer = dp[n][m]
    return answer