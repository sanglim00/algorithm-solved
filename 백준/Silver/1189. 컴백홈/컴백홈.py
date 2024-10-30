import sys

R, C, K = map(int, sys.stdin.readline().split())
graph_ = []
for _ in range(R):
    row = list(sys.stdin.readline().rstrip())
    graph_.append(row)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[0 for _ in range(C)] for _ in range(R)]
ans = 0
def DFS(v, now):
    global ans
    
    if now == K-1:
        if v[0] == 0 and v[1] == C-1: ans += 1
        return

    for i in range(4):
        ny, nx = v[0]+dy[i], v[1]+dx[i]
        if 0<=ny<R and 0<=nx<C:
            if graph_[ny][nx] != 'T' and not visited[ny][nx]:
                visited[ny][nx] = 1
                DFS((ny, nx), now+1)
                visited[ny][nx] = 0

visited[R-1][0] = 1
now = 0
DFS((R-1, 0), now)
print(ans)