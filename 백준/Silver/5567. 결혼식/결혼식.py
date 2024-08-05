import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph_ = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(M):
    A, B  = map(int, sys.stdin.readline().split())
    graph_[A].append(B)
    graph_[B].append(A)

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
                  
BFS(graph_, visited, 1)

ans = 0
for i in range(2, len(visited)):
    if 0< visited[i] and visited[i] < 3:
        ans += 1
print(ans)