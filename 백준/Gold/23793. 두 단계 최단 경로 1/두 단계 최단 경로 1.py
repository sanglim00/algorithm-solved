import sys
import heapq

input = sys.stdin.readline
INF = float("INF")

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

X, Y, Z = map(int, input().split())

def dijkstra(num, check = False):
    heap = [(0, num)]
    dist = [INF for _ in range(N+1)]
    dist[num] = 0

    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if dist[now_node] < now_cost: continue

        for next, cost in graph[now_node]:
            if check and (next == Y): continue
            all_cost = now_cost + cost

            if dist[next] > all_cost:
                dist[next] = all_cost
                heapq.heappush(heap, (all_cost, next))

    return dist

XY = dijkstra(X)
YZ = dijkstra(Y)
XZ = dijkstra(X, True)

ans = XY[Y]+YZ[Z] if XY[Y]+YZ[Z] != INF else -1
ans2 = XZ[Z] if XZ[Z] != INF else -1

print(ans, ans2)