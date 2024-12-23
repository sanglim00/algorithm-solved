import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    A, B, C= map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

heap = [(0, 1)]
min_cost, max_cost = 0, 0

while heap:
    n_cost, n_edge = heapq.heappop(heap)

    if not visited[n_edge]:
        min_cost += n_cost
        max_cost = max(max_cost, n_cost)
        visited[n_edge] = 1

        for e, c in graph[n_edge]:
            if not visited[e]:
                heapq.heappush(heap, (c, e))

print(min_cost-max_cost)