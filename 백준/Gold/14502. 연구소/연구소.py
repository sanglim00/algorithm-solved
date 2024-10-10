import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph_ = []
for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    graph_.append(lst)

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

ans = 0

def BFS():
    global ans
    queue = deque([])

    copy_graph_ = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    # 바이러스 위치 큐에 넣기
    for i in range(N):
        for j in range(M):
            copy_graph_[i][j] = graph_[i][j]
            if copy_graph_[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 1


    # 바이러스 퍼트리기
    while queue:
        now = queue.popleft()
        copy_graph_[now[0]][now[1]] = 2

        for i in range(4):
            ny, nx = now[0]+dy[i], now[1]+dx[i]

            if 0<=ny<N and 0<=nx<M:
                if copy_graph_[ny][nx] == 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

    cnt = 0
    # 안전구역 카운트
    for i in range(N):
        for j in range(M):
            if copy_graph_[i][j] == 0:
                cnt += 1
    
    # 안전구역 max값 업데이트
    ans = max(ans, cnt)


def checkBFS(check, nx, ny):
    if check == 3: 
        BFS()
        return

    for i in range(nx, N):
        for j in range(ny, M):
            if graph_[i][j] == 0:
                graph_[i][j] = 1
                checkBFS(check+1, i, j)
                graph_[i][j] = 0
        ny = 0

checkBFS(0, 0, 0)
print(ans)