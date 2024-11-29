import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

graph_ = [[] for _ in range(N+1)]
visited = [(0, -1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph_[u].append(v)
    graph_[v].append(u)

for i in graph_: i.sort()

def BFS(v):
    idx = 1
    queue = deque([v])
    visited[v] = (idx, 0)


    while queue:
        now = queue.popleft()

        for i in graph_[now]:
            if visited[i][1] == -1:
                idx +=1
                visited[i] = ( idx, visited[now][1]+1)
                queue.append(i)
                
BFS(R)
ans = 0

for i in range(1, N+1): 
    ans += visited[i][0]*visited[i][1]
print(ans)