import sys
import heapq

def BFS(graph_, dist, start):
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        cost, now = heapq.heappop(hq)

        if dist[now] < cost: continue

        for end in graph_[now]:
            sum_ = cost + end[1]

            if sum_ < dist[end[0]]:
                dist[end[0]] = sum_
                heapq.heappush(hq, (sum_, end[0]))

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph_ = [[] for _ in range(V+1)]
dist = [float("INF") for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph_[u].append([v, w])

BFS(graph_, dist, K)
dist[K] = 0
for i in range(1, len(dist)): 
    print("INF" if dist[i] == float('inf') else dist[i])