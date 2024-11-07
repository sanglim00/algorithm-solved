import sys

N, K = map(int, sys.stdin.readline().split())

score = []
for _ in range(N):
    idx, gold, silver, copper = map(int, sys.stdin.readline().split())
    score.append((idx,  gold*100 + silver*10 + copper))

score.sort(key=lambda x: x[1], reverse=True)

idx = 1
for i in range(1, len(score)):
    if K == i: 
        print(idx)
        break
    if score[i-1][1] == score[i][1]: continue
    idx += 1