import sys

N = int(sys.stdin.readline())
graph_ = [0 for _ in range(N)]
ans = 0

def isPromising(row):
    k = 0

    while k < row:
        if graph_[row] == graph_[k] or abs(graph_[row]-graph_[k]) == row-k:
            return 0
        k += 1
    return 1


def NQueen(row):
    global ans
    
    if row == N:
        ans += 1
        return
    
    for i in range(N):
        graph_[row] = i

        if isPromising(row):
            NQueen(row + 1)

NQueen(0)
print(ans)