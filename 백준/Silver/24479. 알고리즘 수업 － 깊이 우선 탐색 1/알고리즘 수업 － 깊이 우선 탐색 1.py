import sys
sys.setrecursionlimit(100001)

N, M, R = map(int, sys.stdin.readline().split())
graph_ = [[] for _ in range(N+1)]
visited = [[] for _ in range(N+1)]

order = [0 for _ in range(N+1)]
idx = 1

def DFS(graph_, visited, v):
    global idx
    visited[v] = 1
    order[v] = idx

    for i in graph_[v]:
        if not visited[i]:
            idx += 1
            DFS(graph_, visited, i)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph_[u].append(v)
    graph_[v].append(u)

for i in graph_: i.sort()
DFS(graph_, visited, R)

for i in range(1, N+1):
    print(order[i])
