import sys
import heapq

input = sys.stdin.readline
INF = float("INF")

N, M = map(int, input().split())
ward = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))

def dijkstra(num):
    heap = [(0, num)]
    dist = [INF for _ in range(N)]
    dist[num] = 0

    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if dist[now_node] < now_cost: continue

        for next, cost in graph[now_node]:
            if ward[next] and next != N-1: continue
            all_cost = now_cost + cost
            
            if dist[next] > all_cost:
                dist[next] = all_cost
                heapq.heappush(heap, (all_cost, next))
    
    print(dist[N-1] if dist[N-1] != INF else -1)
    
dijkstra(0)