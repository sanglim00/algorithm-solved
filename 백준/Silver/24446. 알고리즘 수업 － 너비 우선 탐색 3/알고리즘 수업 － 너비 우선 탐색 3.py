import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

graph_ = [[] for _ in range(N+1)]
visited = [-1 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph_[u].append(v)
    graph_[v].append(u)

for i in graph_: i.sort()

def BFS(v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        now = queue.popleft()

        for i in graph_[now]:
            if visited[i] == -1:
                visited[i] = visited[now]+1
                queue.append(i)
                
BFS(R)
for i in range(1, N+1): print(visited[i])