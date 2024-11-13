import sys
import heapq

T = int(sys.stdin.readline())
for idx in range(1, T+1):
    N, M = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(M)]
    for _ in range(N):
        x, y, z = map(int, sys.stdin.readline().split())
        graph[x].append((y, z))
        graph[y].append((x, z))
    
    heap = [(0, 0)]

    dist = [(-1, float('INF')) for _ in range(M)]
    dist[0] = (0, 0)

    while heap:
        now_cost, now_node = heapq.heappop(heap)
        if dist[now_node][1] < now_cost: continue

        for next, cost in graph[now_node]:
            all_cost = now_cost + cost
            if dist[next][1] > all_cost:
                dist[next] = (now_node, all_cost)
                heapq.heappush(heap, (all_cost, next))

    if dist[-1][1] == float('INF'):
        print(f"Case #{idx}: -1")
    else:
        ans = []
        now = M-1
        while now > 0:
            ans.append(now)
            now = dist[now][0]
        ans.append(0)
        print(f"Case #{idx}:", end=" ")
        for i in range(len(ans)-1, -1, -1): print(ans[i], end=' ')
        print()