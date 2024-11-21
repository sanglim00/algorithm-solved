import sys
import heapq

input = sys.stdin.readline
INF = float("INF")

def dijkstra(start, N, E, graph):
    heap = [(0, start)]
    dist = [INF for _ in range(N+1)]
    dist[start] = 0

    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if dist[now_node] < now_cost: continue

        for next, cost in graph[now_node]:
            all_cost = now_cost + cost

            if dist[next] > all_cost:
                dist[next] = all_cost
                heapq.heappush(heap, (all_cost, next))

    return dist[E]

N = int(input())
E = int(input())
T = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))

dist = [0]
for i in range(1, N+1):
    dist.append(dijkstra(i, N, E, graph))

ans = 0
for i in dist[1:]:
    if i <= T:
        ans += 1
print(ans)