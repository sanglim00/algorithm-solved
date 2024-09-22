import sys

N, M  = map(int, sys.stdin.readline().split())
graph_ = [0 for _ in range(9)]

def backtracking(start, idx):
    if idx == M: 
        for i in range(M):
            print(graph_[i], end=' ')
        print()
        return
    
    for i in range(start, N):
        graph_[idx] = i+1
        backtracking(i, idx+1)

backtracking(0, 0)