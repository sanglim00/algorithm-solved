import sys

while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0: break
    sk, sy = [], []
    for _ in range(N):
        num = int(sys.stdin.readline())
        sk.append(num)
    for _ in range(M):
        num = int(sys.stdin.readline())
        sy.append(num)

    ans = 0
    a = sk.pop()
    b = sy.pop()
    while sk or sy:
        if a == b: 
            ans += 1
            a = sk.pop()
            b = sy.pop()    
        elif a > b and sk: a = sk.pop()
        elif sy: b = sy.pop()

        if not sk and sy: b = sy.pop()    
        if not sy and sk: a = sk.pop()
    
    if a == b: ans += 1
    print(ans)