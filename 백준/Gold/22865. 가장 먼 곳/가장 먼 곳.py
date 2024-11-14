import sys
import heapq

input = sys.stdin.readline

N = int(input())
A, B, C = map(int, input().split())

M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    D, E, L = map(int, input().split())
    graph[D].append((E, L))
    graph[E].append((D, L))

def dijkstra(num):
    heap = [(0, num)]
    dist = [float("INF") for _ in range(N+1)]
    dist[num] = 0

    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if dist[now_node] < now_cost: continue

        for next, cost in graph[now_node]:
            all_cost = now_cost+cost

            if dist[next] > all_cost:
                dist[next] = all_cost
                heapq.heappush(heap, (all_cost, next))
    
    return dist

A_lst = dijkstra(A)
B_lst = dijkstra(B)
C_lst = dijkstra(C)

ans = (0, 0)
for i in range(1, N+1):
    min_ = min(min(A_lst[i], B_lst[i]), C_lst[i])
    if ans[0] < min_: ans = (min_, i)
    
print(ans[1])