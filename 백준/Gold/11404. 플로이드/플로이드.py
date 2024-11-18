import sys
import heapq

input = sys.stdin.readline
INF = float("INF")

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

def dijkstra(num):
    heap = [(0, num)]
    dist = [INF for _ in range(n+1)]
    dist[num] = 0

    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if dist[now_node] < now_cost: continue

        for next, cost in graph[now_node]:
            all_cost = now_cost + cost
            
            if dist[next] > all_cost:
                dist[next] = all_cost
                heapq.heappush(heap, (all_cost, next))
    
    for i in range(1, n+1): 
        print(dist[i] if dist[i] != INF else 0, end=' ')
    print()

for i in range(1, n+1): dijkstra(i)