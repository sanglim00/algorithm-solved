import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, sys.stdin.readline().split())

dist = [float('INF') for _ in range(N+1)]

def dijkstra(i):
    heap = [(0, i)]
    dist[i] = 0

    while heap:
        now_cost, now_y = heapq.heappop(heap)

        if dist[now_y] < now_cost: continue

        for next_x, cost in graph[now_y]:
            all_cost = now_cost + cost

            if dist[next_x] > all_cost:
                dist[next_x] = all_cost
                heapq.heappush(heap, (all_cost, next_x))

dijkstra(s)
print(dist[t])