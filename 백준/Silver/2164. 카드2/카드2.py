import sys
from collections import deque   

N = int(sys.stdin.readline())
queue = deque(i for i in range(1, N+1))

while len(queue) != 1:
    queue.popleft()
    if len(queue) == 1: break
    now = queue.popleft()
    queue.append(now)

print(queue[0])