import sys
from collections import deque

N = int(sys.stdin.readline())
graph_ = [[] for _ in range(N+1)]
check = [[0 for _ in range(N+1)] for _ in range(N+1)]

def BFS(graph_, visited, v):
    queue = deque([v])
    
    while queue:
        now = queue.popleft()
        for i in graph_[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                check[v][i] = 1

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(len(row)):
        if row[j] == 1:
            graph_[i+1].append(j+1)

for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    BFS(graph_, visited, i)

for i in range(1, len(check)):
    for j in range(1, len(check)):
        print(check[i][j], end=' ')
    print()