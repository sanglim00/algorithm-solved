import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
ans_list = [0]

def BFS(graph_, visited, v):
    queue = deque([v])
    visited[v] = 0

    while queue:
        now = queue.popleft()
        for i in graph_[now]:         
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[now] + 1
    ans_list.append(sum(visited))

graph_ = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph_[A].append(B)
    graph_[B].append(A)

for i in graph_: i.sort()

for i in range(1, len(graph_)):
    visited = [0 for _ in range(N+1)]
    BFS(graph_, visited, i)

min_ = float('inf')
ans = 0

for i in range(1, len(ans_list)):
    if ans_list[i] < min_:
        min_ = ans_list[i]
        ans = i

print(ans)