import sys

DIR = 4
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    lst = list(map(int, input().split()))
    graph.append(lst)

visited = [[0 for _ in range(N)] for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = float("INF")

def countCost():
    global ans
    
    now_cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                now_cnt += graph[i][j]

    ans = min(ans, now_cnt)

def backtracking(check, pi):
    if check == 3:
        countCost()
        return

    for i in range(pi, N):
        for j in range(N):
            if visited[i][j]: continue

            now = True
            for k in range(DIR):
                ny, nx = i+dy[k], j+dx[k]
                if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                    continue
                else:
                    now = False
                    break
            if now:
                visited[i][j] = 1
                for k in range(DIR):
                    ny, nx = i+dy[k], j+dx[k]
                    visited[ny][nx] = 1
                backtracking(check+1, i)
                visited[i][j] = 0
                for k in range(DIR):
                    ny, nx = i+dy[k], j+dx[k]
                    visited[ny][nx] = 0
            
backtracking(0, 1)
print(ans)