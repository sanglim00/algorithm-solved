import sys

h, m = map(int, sys.stdin.readline().split())

if m < 45:
    if h == 0:
        print(24-1+h, 60+m-45)
    elif h == 1:
        print(0, 60+m-45)
    else:
        print(h-1, 60+m-45)
else:
    print(h, m-45)
