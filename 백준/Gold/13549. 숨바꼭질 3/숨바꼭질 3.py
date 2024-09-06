import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dx = ['*', '-', '+']

def BFS(visited, v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        now = queue.popleft()
        if now == K: break

        for i in dx:
            check = False
            nx = now
            if i == '*': 
                check = True 
                nx = now * 2
            elif i == '-': nx = now - 1
            elif i == '+': nx = now + 1   
            
            if 0<=nx<=100000 and visited[nx] == -1:
                queue.append(nx)
                if check: visited[nx] = visited[now]
                else: visited[nx] = visited[now] + 1


visited = [-1 for _ in range(100001)]

BFS(visited, N)
print(visited[K])