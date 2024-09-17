import sys
from collections import deque

N = int(sys.stdin.readline())
graph_ = list(map(int, sys.stdin.readline().split()))
visited = [-1 for _ in range(N)]


def BFS(v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        now = queue.popleft()
        for i in range(1, graph_[now]+1):
            nx = now + i
            if 0<=nx<N and visited[nx] == -1:
                visited[nx] = visited[now] + 1
                queue.append(nx)

BFS(0)
if N == 1: print(0)
elif visited[-1]: print(visited[-1])
else: print(-1)