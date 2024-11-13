import sys
import heapq

def dijkstra(num, friends):
    heap = [(0, num)]

    dist = [float('INF') for _ in range(N+1)]
    dist[num] = 0

    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if dist[now_node] < now_cost: continue

        for next, cost in graph[now_node]:
            all_cost = now_cost + cost
            if dist[next] > all_cost:
                dist[next] = all_cost
                heapq.heappush(heap, (all_cost, next))
    
    sum_ = 0
    for i in friends: sum_ += dist[i]
    return sum_


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    K = int(sys.stdin.readline())
    friends = list(map(int, sys.stdin.readline().split()))
    
    ans = (float("INF"), -1)
    for i in range(1, N+1):
        now = dijkstra(i, friends)
        if ans[0] > now: ans = (now, i)
    
    print(ans[1])