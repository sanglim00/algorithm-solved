from collections import deque

N, K = map(int, input().split())

if N == K == 1:
    print(0)
    print(1)
    exit()

visited = {}

dx = ['-', '+', '*']

queue = deque([N])
visited[N] = 0

ans = []
while queue:
    now = queue.popleft()
    if now == K: break

    for i in dx:
        nx = now
        if i == '-': nx -= 1
        elif i == '+': nx += 1
        else: nx *= 2

        if 0<=nx<10**6+1 and nx not in visited:
            visited[nx] = visited[now] + 1
            queue.append(nx)

            if nx == now-1: ans.append(('-', nx))
            elif nx == now+1: ans.append(('+', nx))
            else: ans.append(('*', nx))

ans = ans[::-1]
now = K
answer = []
for i in ans:
    if i[1] != now: continue
    answer.append(now)

    if i[0] == '-': now += 1
    elif i[0] == '+': now -= 1
    else: now = int(now/2)
answer.append(now)

# output
print(visited[K])
while answer: print(answer.pop(), end=' ')
print()