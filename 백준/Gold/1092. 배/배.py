import sys

N = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))

crane.sort(reverse=True)
box.sort(reverse=True)

ans = 0

if crane[0] < box[0]:
    print(-1)
else:
    while len(box):
        for i in range(len(crane)):
            for j in range(len(box)):
                if crane[i] >= box[j]:
                    del box[j]
                    break
        ans += 1
    print(ans)