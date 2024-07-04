import sys
from collections import deque

def DFS(graph_, visited, v):
    visited[v] = 1
    print(v, end=' ')

    for i in graph_[v]:
        if not visited[i]:
            DFS(graph_, visited, i)


def BFS(graph_, visited, v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        now = queue.popleft()
        print(now, end=' ')
        
        for i in graph_[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


N, M, V = map(int, sys.stdin.readline().split())

graph_ = [[] for i in range(N+1)]
visited = [0 for i in range(N+1)]

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph_[start].append(end)
    graph_[end].append(start)

for i in graph_: i.sort()

# DFS 실행
DFS(graph_, visited, V)
print()

# visited 초기화
visited = [0 for i in range(N+1)]

# DFS 실행
BFS(graph_, visited, V)