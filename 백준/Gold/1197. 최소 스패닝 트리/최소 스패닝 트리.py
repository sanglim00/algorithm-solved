import sys
import heapq

V, E  = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

heap = [(0, 1)]
min_cost = 0

while heap:
    n_cost, n_edge = heapq.heappop(heap)

    if not visited[n_edge]:
        min_cost += n_cost
        visited[n_edge] = 1

        for c, e in graph[n_edge]:
            if not visited[e]:
                heapq.heappush(heap, (c, e))

print(min_cost) 