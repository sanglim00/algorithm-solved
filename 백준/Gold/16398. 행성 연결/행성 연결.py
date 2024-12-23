import sys
import heapq

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]
visited = [0 for _ in range(N)]

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if i != j:
            graph[i].append((j, lst[j]))


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

print(sum_cost)