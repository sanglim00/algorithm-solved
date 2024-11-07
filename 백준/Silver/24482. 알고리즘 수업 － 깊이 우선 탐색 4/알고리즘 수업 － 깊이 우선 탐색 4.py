import sys
sys.setrecursionlimit(10**6)

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph: i.sort(reverse=True)

visited = [-1 for _ in range(N+1)]

def DFS(v, idx):
    visited[v] = idx

    for i in graph[v]:
        if visited[i] == -1:
            DFS(i, idx+1)

DFS(R, 0)
for i in range(1, N+1): print(visited[i])