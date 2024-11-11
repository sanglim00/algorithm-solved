import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start, end):

    heap = [(start, 0)]
    dist = [float("INF") for _ in range(N+1)]
    dist[start] = 0

    while heap:
        n_node, n_cost = heapq.heappop(heap)

        if dist[n_node] < n_cost: continue

        for  node, cost in graph[n_node]:
            all_cost = n_cost + cost

            if dist[node] > all_cost:
                dist[node] = all_cost
                heapq.heappush(heap, (node, all_cost))
                
    return dist[end]

ans = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
ans2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

print(min(ans, ans2) if min(ans, ans2) < float("INF") else -1)