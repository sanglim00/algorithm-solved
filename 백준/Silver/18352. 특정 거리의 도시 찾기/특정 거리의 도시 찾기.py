import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

graph_ = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(M):
    A, B  = map(int, sys.stdin.readline().split())
    graph_[A].append(B)

for i in graph_: i.sort()

def BFS(graph_, visited, v):
    queue = deque([(v)])
    visited[v] = 0
   
    while queue:
        now = queue.popleft()
        for i in graph_[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[now] +1
                  
BFS(graph_, visited, X)

check = True
for i in range(1, len(visited)):
    if i != X and visited[i] == K:
        check = False
        print(i)

if check: print(-1)