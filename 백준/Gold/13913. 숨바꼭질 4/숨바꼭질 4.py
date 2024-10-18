from collections import deque

N, K = map(int, input().split())

# 방문 처리
visited = {}
# 이동 방향
dx = ['-', '+', '*']

queue = deque([N])
visited[N] = 0

move = []
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
			
            # 이동 방법을 계산하기 위함
            if nx == now-1: move.append(('-', nx))
            elif nx == now+1: move.append(('+', nx))
            else: move.append(('*', nx))

move = move[::-1]

now = K # 도착 위치 -> 시작 위치 계산을 위함
answer = []
for i in move:
    if i[1] != now: continue
    answer.append(now)

    if i[0] == '-': now += 1
    elif i[0] == '+': now -= 1
    else: now = int(now/2)

answer.append(now) # 처음 시작 위치 추가

# output
print(visited[K])
while answer: print(answer.pop(), end=' ')
print()
