import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [-1 for _ in range(100001)]

def BFS(v):
    queue = deque([v])
    visited[v] = 0

    ans = 0
    while queue:
        now = queue.popleft()

        lst = [now+1, now-1, now*2]
        for i in lst:
            if 0<=i<100001 and (visited[i] == -1 or visited[i] == visited[now]+1):
                if i == K: ans += 1
                queue.append(i)
                visited[i] = visited[now] + 1 
   
    print(visited[K])    
    print(ans)  

if N == K:
    print(0)
    print(1)
else: 
    BFS(N)