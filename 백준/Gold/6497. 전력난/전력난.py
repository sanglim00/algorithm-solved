import sys
import heapq

input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == n == 0: break

    graph = [[] for _ in range(m)]
    visited = [0 for _ in range(m)]

    init_cost = 0
    for i in range(n):
        A, B, C= map(int, input().split())
        graph[A].append((B, C))
        graph[B].append((A, C))
        init_cost += C

    
    

    heap = [(0, 0)]
    sum_cost = 0

    while heap:
        n_cost, n_edge = heapq.heappop(heap)

        if not visited[n_edge]:
            sum_cost += n_cost
            visited[n_edge] = 1

            for e, c in graph[n_edge]:
                if not visited[e]:
                    heapq.heappush(heap, (c, e))

    print(init_cost-sum_cost)