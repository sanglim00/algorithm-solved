import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph: i.sort(reverse=True)
visited = [0 for _ in range(n)]
apple = list(map(int, input().split()))

ans = 0
def DFS(v, cnt):
    global ans
    visited[v] = 1

    if apple[v]: ans += 1
    if cnt == k: return

    for i in graph[v]:
        if not visited[i]:
            visited[v] = 1
            DFS(i, cnt+1)

DFS(0, 0)
print(ans)