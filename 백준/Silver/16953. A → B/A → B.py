import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

visited = {}
px = ['*', '+']

def BFS(visited, v):
    queue = deque([v])
    visited[v] = 1
    
    while queue:
        now = queue.popleft()
        nx = now
        if nx == B:break
        for i in px:
            if i == '*': nx = now * 2
            elif i == '+': nx = int(now*10+1)
            if 0<nx<=B and nx not in visited:
                queue.append(nx)
                visited[nx] = visited[now] + 1

BFS(visited, A)
print(visited[B] if B in visited else -1)