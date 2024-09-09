import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

graph_ = []
for _ in range(N):
    row = list(sys.stdin.readline().rstrip())
    graph_.append(row)

px = [1, -1, 0, 0]
py = [0, 0, 1, -1]
def DFS(graph_, visited, v, now, now2):
    visited[v[0]][v[1]] = 1
    
    for i in range(4):
        ny, nx = v[0]+py[i], v[1]+px[i]
        if 0<=ny<N and 0<=nx<N:
            if not visited[ny][nx] and (graph_[ny][nx] == now or graph_[ny][nx] == now2):
                DFS(graph_, visited, (ny, nx), now, now2)
    

visited = [[0 for _ in range(N)] for _ in range(N)]
now, now2 = graph_[0][0], graph_[0][0]
ans = []
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            now, now2 = graph_[i][j], graph_[i][j]
            DFS(graph_, visited, (i, j), now, now2)
            ans.append(now)
            
            
visited = [[0 for _ in range(N)] for _ in range(N)]
if graph_[0][0] == 'R' or graph_[0][0] =='G': now, now2 = 'R', 'G'
else: now, now2 = 'B', 'B'
ans2 = []
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            if now != 'R' and (graph_[i][j] == 'R' or graph_[i][j] =='G'): now, now2 = 'R', 'G'
            elif now != 'B' and graph_[i][j] == 'B': now, now2 = 'B', 'B'
            DFS(graph_, visited, (i, j), now, now2)
            ans2.append(now)
            

print(len(ans), len(ans2))