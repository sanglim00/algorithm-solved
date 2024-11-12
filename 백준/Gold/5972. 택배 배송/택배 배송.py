import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


heap = [(1, 0)]
dist = [float('INF') for _ in range(N+1)]    
dist[1] = 0

while heap:
    n_node, n_cost = heapq.heappop(heap)

    if dist[n_node] < n_cost: continue

    for next, cost in graph[n_node]:
        all_cost = n_cost + cost

        if dist[next] > all_cost:
            dist[next] = all_cost 
            heapq.heappush(heap, (next, all_cost))

print(dist[-1])