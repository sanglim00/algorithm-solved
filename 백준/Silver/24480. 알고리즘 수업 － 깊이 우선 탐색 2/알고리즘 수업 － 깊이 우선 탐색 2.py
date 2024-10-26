import sys
sys.setrecursionlimit(10**6)
N, M, R = map(int, sys.stdin.readline().split())

graph_ = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph_[u].append(v)
    graph_[v].append(u)

for i in graph_: i.sort(reverse=True)
visited = [0 for _ in range(N+1)]

idx = 1
def DFS(v):
    global idx
    visited[v] = idx

    for i in graph_[v]:
        if not visited[i]:
            idx += 1
            DFS(i)

DFS(R)
for i in range(1, len(visited)):
    print(visited[i])