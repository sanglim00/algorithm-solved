import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [[(-1, float('INF')) for _ in range(N+1)] for _ in range(N+1)]

def dijkstra(i, j):
    heap = [(0, i, j)]
    dist[i][j] = (0, 0)

    while heap:
        now_cost, now_y, now_x = heapq.heappop(heap)

        if dist[now_y][now_x][1] < now_cost: continue

        for next_x, cost in graph[now_y]:
            all_cost = now_cost + cost

            if dist[next_x][now_x][1] > all_cost:
                dist[next_x][now_x] = (now_y, all_cost)
                heapq.heappush(heap, (all_cost, now_x, next_x))

for i in range(1, N+1): dijkstra(i, i)
for i in range(1, N+1):
    for j in range(1, N+1):
        print(dist[i][j][0] if i != j else '-', end=' ')
    print()
print()