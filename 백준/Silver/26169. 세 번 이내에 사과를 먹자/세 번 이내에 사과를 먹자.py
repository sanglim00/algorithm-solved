import sys

input = sys.stdin.readline
NUM = 5

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

check = 0
def backtracking(graph, visited, py, px, cnt, now):
    global check

    if cnt > 1 and now < 4: 
        check = 1
        return check 
    
    visited[py][px] = 1
    
    for i in range(4):
        ny, nx = py+dy[i], px+dx[i]

        if 0<=ny<NUM and 0<=nx<NUM:
            if not visited[ny][nx] and graph[ny][nx] != -1:
                visited[ny][nx] = 1
                if graph[ny][nx]: cnt += 1
                backtracking(graph, visited, ny, nx, cnt, now+1)
                if graph[ny][nx]: cnt -= 1
                visited[ny][nx] = 0

    return check

graph = []
for _ in range(NUM):
    lst = list(map(int, input().split()))
    graph.append(lst)

R, C = map(int, input().split())

visited = [[0 for _ in range(NUM)] for _ in range(NUM)]
ans = backtracking(graph, visited, R, C, 0, 0)
print(ans) 