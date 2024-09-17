import sys
from collections import deque

A, K = map(int, sys.stdin.readline().split())
visited = {}

def BFS(v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        now = queue.popleft()
        
        for i in ['+', '*']:
            nx = now
            if i == '+': nx += 1
            else: nx *= 2

            if 0<=nx<=K and nx not in visited:
                visited[nx] = visited[now] + 1 
                queue.append(nx)

BFS(A)
print(visited[K])