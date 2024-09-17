import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

graph_ = [0 for _ in range(F+1)]
visited = [-1 for _ in range(F+1)]

def BFS(v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        now = queue.popleft()
        for i in ['U', 'D']:
            nx = now
            if i == 'U': nx += U
            else: nx -= D
            if 0<nx<=F and visited[nx] == -1:
                queue.append(nx)
                visited[nx] = visited[now] + 1

BFS(S)
print(visited[G] if visited[G] != -1 else "use the stairs")