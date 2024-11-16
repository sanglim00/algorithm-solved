import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(M):
    lst = list(sys.stdin.readline().rstrip())
    graph.append(lst)

visited = [[float("INF") for _ in range(N)] for _ in range(M)]
visited[0][0] = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# cost, i, j
heap = [(0, 0, 0)]
while heap:
    now_cost, now_i, now_j = heapq.heappop(heap)

    for j in range(4):
        ny, nx = now_i + dy[j], now_j + dx[j]
 
        if 0<=ny<M and 0<=nx<N:
            all_cost = now_cost + int(graph[ny][nx])
            if visited[ny][nx] > all_cost:
                visited[ny][nx] = all_cost
                heapq.heappush(heap, (all_cost, ny, nx))

print(visited[M-1][N-1])