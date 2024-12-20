import sys
import heapq

input = sys.stdin.readline
INF = float("INF")

N = int(input())
graph = []
for _ in range(N):
    lst = list(map(int, input().split()))
    graph.append(lst)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dijkstra(N, graph):
    heap = [(0, 0, 0)]
    dist = [[INF for _ in range(N)] for _ in range(N)]
    dist[0][0] = 0

    while heap:
        now_cost, now_i, now_j = heapq.heappop(heap)
        if dist[now_i][now_j] < now_cost: continue
        
        for i in range(4):
            ny, nx = now_i+dy[i], now_j+dx[i]

            if 0<=ny<N and 0<=nx<N:
                all_cost = max(now_cost, abs(graph[now_i][now_j] - graph[ny][nx]))
                
                if dist[ny][nx] > all_cost:
                    dist[ny][nx] = all_cost
                    heapq.heappush(heap, (all_cost, ny, nx))

    return dist[N-1][N-1]

ans = dijkstra(N, graph)
print(ans)