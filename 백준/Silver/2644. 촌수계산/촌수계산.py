import sys

N = int(sys.stdin.readline())
n1, n2 = map(int, sys.stdin.readline().split())

graph_ = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1) for _ in range(N+1)]

M = int(sys.stdin.readline())

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph_[x].append(y)
    graph_[y].append(x)

def DFS(graph_, visited, v, ans):
    visited[v] = 1
    ans += 1

    for i in graph_[v]:
        if i == n2:
            print(ans)
            sys.exit()
        if not visited[i]:
            DFS(graph_, visited, i, ans)

ans = 0
DFS(graph_, visited, n1, ans)
print(-1)