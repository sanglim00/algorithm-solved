import sys

N, M = map(int, sys.stdin.readline().split())

# 입력값 저장
graph_ = []
graph_.append([0 for _ in range(N)])
for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    graph_.append(lst)

# 1차원 누적합 계산
sum_ = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1): sum_[i][1] = graph_[i][0]

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_[i][j] = sum_[i][j-1]+graph_[i][j-1]

# 2차원 누적합 계산
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1): dp[1][i] = sum_[1][i]

for i in range(2, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j]+sum_[i][j]

# 계산
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    if y1 ==1 and x1 ==1 and y2==N and x2==N: 
        print(dp[-1][-1])
    else:
        ans = dp[x2][y2] - (dp[x2][y1-1] + dp[x1-1][y2]) + dp[x1-1][y1-1]
        print(ans)
