import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
px = ['-', '+', '*']

def BFS(visited, v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        now = queue.popleft()
        nx = now
        if nx == K: break
        for i in range(3):
            if px[i] == '-': nx = now - 1
            elif px[i] == '+': nx = now + 1
            elif px[i] == '*': nx = now * 2
            if 0<=nx<100001:
                if visited[nx] == -1:
                    queue.append(nx)
                    visited[nx] = visited[now] + 1
                    
graph_ = [0 for _ in range(100001)]
visited = [-1 for _ in range(100001)]

BFS(visited, N)
print(visited[K])