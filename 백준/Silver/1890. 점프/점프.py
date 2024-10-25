N = int(input())

graph_ = []
for _ in range(N):
    row = list(map(int, input().split()))
    graph_.append(row)

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0]=1
for i in range(N):
    for j in range(N):
        if i == j == N-1: break
        num = graph_[i][j]
        if num == 0: continue
        if i + num < N: dp[i+num][j] += dp[i][j]
        if j + num < N: dp[i][j+num] += dp[i][j]

print(dp[-1][-1])