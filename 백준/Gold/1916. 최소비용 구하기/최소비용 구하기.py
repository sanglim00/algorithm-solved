import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph_ = [[] for _ in range(N+1)]
dist = [float('inf') for _ in range(N+1)]

for _ in range(M):
    row = list(map(int, sys.stdin.readline().split()))
    graph_[row[0]].append([row[1], row[2]])

start, end = map(int, sys.stdin.readline().split())

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

BFS(graph_, dist, start)
print(dist[end])