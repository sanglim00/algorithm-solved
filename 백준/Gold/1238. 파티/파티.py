import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append((end, time))

def dijkstra(start):
    
    heap = [(start, 0)]
    dist = [float("INF") for _ in range(N+1)]
    dist[start] = 0

    while heap:
        n_node, n_time = heapq.heappop(heap)

        if dist[n_node] < n_time: continue

        for  node, time in graph[n_node]:
            all_time = n_time + time

            if dist[node] > all_time:
                dist[node] = all_time
                heapq.heappush(heap, (node, all_time))
    
    return dist

check = [0 for _ in range(N+1)]
for i in range(1, N+1): check[i] = dijkstra(i)[X]
lst = dijkstra(X)
for i in range(1, N+1): check[i] += lst[i]

print(max(check[1:]))