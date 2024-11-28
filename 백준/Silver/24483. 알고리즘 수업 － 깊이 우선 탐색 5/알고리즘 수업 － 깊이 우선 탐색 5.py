import sys
sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph: i.sort()

visited = [(0, -1)for _ in range(N+1)]

seq = 1
def DFS(v, idx):
    global seq
    visited[v] = (seq, idx)

    for i in graph[v]:
        if visited[i][1] == -1:
            seq += 1
            DFS(i, idx+1)

DFS(R, 0)
ans = 0
for i in visited[1:]: 
    ans += i[0]*i[1]
print(ans)