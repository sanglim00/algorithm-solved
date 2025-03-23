import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

visited = [-1 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in graph: i.sort()

def BFS(v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now]+1
                queue.append(i)

BFS(1)
max_ = max(visited[1:])
check = True
cnt = 0
for i in range(1, N+1):
    if visited[i] == max_ and check:
        print(i, max_, end=" ")
        check = False
    if visited[i] == max_:
        cnt += 1
print(cnt)