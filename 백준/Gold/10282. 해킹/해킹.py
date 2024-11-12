import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    n, d, c = map(int, sys.stdin.readline().split())
    
    computer = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        computer[b].append((a, s))
    
    heap = [(c, 0)]
    dist = [float('INF') for _ in range(n+1)]    
    dist[c] = 0

    while heap:
        n_com, n_time = heapq.heappop(heap)

        if dist[n_com] < n_time: continue

        for next, time in computer[n_com]:
            all_time = n_time + time

            if dist[next] > all_time:
                dist[next] = all_time 
                heapq.heappush(heap, (next, all_time))

    ans_com = ans_time = 0
    for i in range(1, n+1):
        if dist[i] != float("INF"):
            ans_com += 1
            ans_time = max(ans_time, dist[i])
    
    print(ans_com, ans_time)