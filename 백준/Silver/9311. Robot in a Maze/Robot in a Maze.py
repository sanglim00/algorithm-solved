import sys
from collections import deque

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS(graph, visited, si, sj):
    queue = deque([(si, sj)])
    visited[si][sj] = 0

    while queue:
        now = queue.popleft()

        for i in range(4):
            ny, nx = now[0]+dy[i], now[1]+dx[i]

            if 0<=ny<N and 0<=nx<M:
                if visited[ny][nx] == -1 and graph[ny][nx] != 'X':
                    queue.append((ny, nx))
                    visited[ny][nx] = visited[now[0]][now[1]] + 1

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = []

    si, sj = 0, 0

    for i in range(N):
        lst = list(input().rstrip())
        graph.append(lst)
        for j in range(M):
            if lst[j] == 'S': 
                si, sj = i, j 
                break

    visited = [[-1 for _ in range(M)] for _ in range(N)]
    BFS(graph, visited, si, sj)

    ans = float("INF")
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'G' and visited[i][j] != -1:
                ans = min(ans, visited[i][j])
    
    print(f"Shortest Path: {ans}" if ans != float("INF") else "No Exit")