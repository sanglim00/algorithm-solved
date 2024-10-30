from collections import deque

N = int(input())
graph_ = [[] for _ in range(N+1)]

for i in range(1, N+1):
    num = int(input())
    graph_[i].append(num)

ans = 0
max_ = 0
for i in range(1, N+1):
    queue = deque([i])
    visited = [0 for _ in range(N+1)]
    visited[i] = 1

    while queue:
        now = queue.popleft()
        
        for j in graph_[now]:
            if not visited[j]:
                queue.append(j)
                visited[j] = 1
    
    sum_ = sum(visited)
    if sum_ > max_:
        ans = i
        max_ = sum_

print(ans)