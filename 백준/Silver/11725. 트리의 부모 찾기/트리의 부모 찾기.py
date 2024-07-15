import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

def DFS(graph_, visited, v):
    for i in graph_[v]:
        if not visited[i]:
            visited[i] = v
            DFS(graph_, visited, i)


node_lst = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(N-1):
    n1, n2 = map(int, sys.stdin.readline().split())

    node_lst[n1].append(n2)
    node_lst[n2].append(n1)

DFS(node_lst, visited, 1)

for i in range(2, len(visited)):
    print(visited[i])