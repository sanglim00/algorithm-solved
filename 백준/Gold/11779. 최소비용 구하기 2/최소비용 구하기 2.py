import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
dist = [(-1, float('INF')) for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((c, e))

v1, v2 = map(int, sys.stdin.readline().split())

heap = [(0, v1)]
dist[v1] = (0, 0)

while heap:
    n_cost, n_node = heapq.heappop(heap)

    if dist[n_node][1] < n_cost: continue

    for cost, node in graph[n_node]:
        all_cost = n_cost + cost

        if all_cost < dist[node][1]:
            dist[node] = (n_node, all_cost)

            heapq.heappush(heap, (all_cost, node))

st = []
now = v2
while now != v1:
    st.append(now)
    now = dist[now][0]
st.append(v1)

print(dist[v2][1])
print(len(st))
while st: print(st.pop(), end=' ')
print()