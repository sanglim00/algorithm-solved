import sys
from collections import deque

def BFS(node, visited, v):
    queue = deque([v])
    visited[v] = 1

    while queue:
        now = queue.popleft()
        for i in node[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

N, M = map(int, sys.stdin.readline().split())

node = [[] for i in range(N+1)]
visited = [0 for i in range(N+1)]

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    node[u].append(v)
    node[v].append(u)

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        BFS(node, visited, i)
        ans += 1
print(ans)



