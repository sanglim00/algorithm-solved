import sys
from collections import deque

N = int(sys.stdin.readline())

graph_ = list(map(int, sys.stdin.readline().split()))
graph_.insert(0, 0)

visited = [0 for _ in range(N+1)]
start = int(sys.stdin.readline())

def BFS(graph_, visited, v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        now = queue.popleft()
        num = graph_[now]
        dx = [-num, num]
        for i in range(2):
            nx = now + dx[i]
            if 0<nx<N+1:
                if not visited[nx]:
                    queue.append(nx)
                    visited[nx] = 1
        
BFS(graph_, visited, start)
print(sum(visited[1:]))