import sys

N, M  = map(int, sys.stdin.readline().split())
graph_ = [0 for _ in range(9)]
visited = [0 for _ in range(9)]

def backtracking(start, idx):
    if idx == M: 
        for i in range(M):
            print(graph_[i], end=' ')
        print()
        return
    
    for i in range(start, N+1):
        if not visited[i]:
            visited[i] = 1
            graph_[idx] = i
            backtracking(i+1, idx+1)
            visited[i] = 0

backtracking(1, 0)