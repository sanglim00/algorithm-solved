import sys
from collections import deque

def BFS(graph, visited, v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        now = queue.popleft()
        
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
    

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))

    graph = [[] for _ in range(N+1)]
    for i in range(N):
        graph[i+1].append(lst[i])

    visited = [0 for _ in range(N+1)]

    ans = 0
    for i in range(1, N+1):
        if not visited[i]:
            ans += 1
            BFS(graph, visited, i)
    print(ans)