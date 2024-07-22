import sys

dpZero = [0 for _ in range(40+1)]
dpZero[0] = 1
dpZero[1] = 0
dpZero[2] = 1

dpOne = [0 for _ in range(40+1)]
dpOne[0] = 0
dpOne[1] = 1
dpOne[2] = 1

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())

    for i in range(3, num+1):
        dpZero[i] = dpZero[i-1] + dpZero[i-2]
        dpOne[i] = dpOne[i-1] + dpOne[i-2]
    
    print(dpZero[num], dpOne[num])
