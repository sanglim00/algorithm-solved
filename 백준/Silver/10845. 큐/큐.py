import sys

my_queue = []
N = int(sys.stdin.readline())

for i in range(N):
    _type = sys.stdin.readline().split()
    if _type[0] == 'push':
        my_queue.append(_type[1])
    elif _type[0] == 'pop':
        if my_queue:
            print(my_queue.pop(0))
        else:print(-1)
    elif _type[0] == 'size':
        print(len(my_queue))
    elif _type[0] == 'empty':
        if my_queue: print(0)
        else: print(1)
    elif _type[0] == 'front':
        if my_queue: print(my_queue[0])
        else: print(-1)
    else:
        if my_queue: print(my_queue[-1])
        else: print(-1)

