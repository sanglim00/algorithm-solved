import sys

N = int(sys.stdin.readline())
Yes, No = 0, 0
for _ in range(N):
    num = int(sys.stdin.readline())
    if num: Yes+=1
    else: No += 1

print("Junhee is cute!" if Yes>No else "Junhee is not cute!")