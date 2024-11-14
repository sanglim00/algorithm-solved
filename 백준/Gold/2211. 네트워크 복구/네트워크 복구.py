import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

heap = [(0, 1)]
dist = [(-1, -1, float("INF")) for _ in range(N+1)]
dist[1] = (0, 0, 0)

while heap:
    now_cost, now_line = heapq.heappop(heap)
    if dist[now_line][2] < now_cost: continue

    for next, cost in graph[now_line]:
        all_cost = now_cost + cost

        if dist[next][2] > all_cost:
            dist[next] = (now_line, next, all_cost)
            heapq.heappush(heap, (all_cost, next))

print(len(dist[2:]))
for i, j, cost in dist[2:]: print(i, j)