import sys

h, m = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())


if (m + time) % 60 == 0:
    h = h + (m + time)//60
    if h > 23:
        print(h-24, 0)
    else:
        print(h, 0)
elif m +time < 60:
    print(h, m+time)
else:
    tmp = m + time
    h = h + tmp // 60
    m = tmp % 60
    if h > 23:
        print(h-24, m)
    else:
        print(h, m)