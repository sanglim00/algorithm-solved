import sys

def DFS(computer, visited, v):
    visited[v] = 1

    for i in computer[v]:
        if not visited[i]:
            DFS(computer, visited, i)
    
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

computer = [[]for i in range(N+1)]
visited = [0 for i in range(N+1)]

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    computer[start].append(end)
    computer[end].append(start)

DFS(computer, visited, 1)
print(sum(visited)-1)