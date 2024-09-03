import sys

M = int(sys.stdin.readline())
mySet = [0 for _ in range(21)]

for _ in range(M):
    command = list(sys.stdin.readline().split())

    if command[0] == 'add': mySet[int(command[1])] = 1
    elif command[0] == 'check':
        print(1 if mySet[int(command[1])]==1 else 0)
    elif command[0] == 'remove':
        mySet[int(command[1])] = 0
    elif command[0] == 'toggle':
        if mySet[int(command[1])]: mySet[int(command[1])] = 0
        else: mySet[int(command[1])] = 1
    elif command[0] == 'all':
        mySet = [1 for _ in range(21)]
    elif command[0] == 'empty':
        mySet = [0 for _ in range(21)]