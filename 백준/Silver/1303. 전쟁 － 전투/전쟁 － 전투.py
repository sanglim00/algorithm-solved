import sys

N, M = map(int, sys.stdin.readline().split())
graph_ = []
visited = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(M):
    row = list(sys.stdin.readline().rstrip())
    graph_.append(row)

W_sum, B_sum = 0, 0 # 부분합 계산
W_score, B_score = 0, 0 # 전체 위력의 합 계산

px = [1, -1, 0, 0]
py = [0, 0, 1, -1]
def DFS(visited, v, t):
    global W_sum, B_sum
    visited[v[0]][v[1]] = 1
    
    for i in range(4):
        ny, nx = v[0]+py[i], v[1]+px[i]
        if 0<=ny<M and 0<=nx<N:
            if not visited[ny][nx] and graph_[ny][nx] == t:
                if t == 'W': W_sum += 1
                else: B_sum += 1
                DFS(visited, (ny, nx), t)

           
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            t = graph_[i][j]
            if t == 'W': W_sum += 1
            else: B_sum += 1
            DFS(visited, (i, j), t) 
            if t == 'W': 
                W_score += W_sum**2
                W_sum = 0
            else: 
                B_score += B_sum**2
                B_sum = 0
            
print(W_score, B_score)