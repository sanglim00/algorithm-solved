import sys
from collections import deque

N = int(sys.stdin.readline())

graph_ = list(map(int, sys.stdin.readline().split()))
graph_.insert(0, 0)

visited = [-1 for _ in range(10001)]
a, b = map(int, sys.stdin.readline().split())

def BFS(graph_, visited, v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        now = queue.popleft()
        num = graph_[now]
        for i in range(now%num, N+1, num):
            nx = i
            if 0<nx<=N and visited[nx] == -1:
                queue.append(nx)
                visited[nx] = visited[now] + 1


BFS(graph_, visited, a)
print(visited[b])