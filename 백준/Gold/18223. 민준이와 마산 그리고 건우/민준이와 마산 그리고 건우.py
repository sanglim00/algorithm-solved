import sys
import heapq

V, E, P = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

def dijkstra(num):
    heap = [(0, num)]
    dist = [(-1, -1, float("INF")) for _ in range(V+1)]
    dist[num] = (0, 0, 0)

    while heap:
        now_cost, now_line = heapq.heappop(heap)
        if dist[now_line][2] < now_cost: continue

        for next, cost in graph[now_line]:
            all_cost = now_cost + cost

            if dist[next][2] >= all_cost:
                dist[next] = (now_line, next, all_cost)
                heapq.heappush(heap, (all_cost, next))

    return dist

a = dijkstra(1) 
b = dijkstra(P)

ans1 = a[V][2]
ans2 = a[P][2] + b[V][2]

print("SAVE HIM" if ans1 == ans2 else "GOOD BYE")