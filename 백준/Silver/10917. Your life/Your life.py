import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

visited = [-1 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

for i in graph: i.sort()

def BFS(v):
    queue = deque([v])
    visited[v] = 0

    max_ = -1

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now]+1
                max_ = max(max_, visited[i])
                queue.append(i)

    print(visited[N])

BFS(1)