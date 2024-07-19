import sys

N = int(sys.stdin.readline())
ans = 0

for _ in range(N):
    str_ = sys.stdin.readline().strip()

    myDict = {}
    before_ = ''
    check = False
    for i in str_:
        if i not in myDict:
            myDict[i] = 1
            before_ = i
        elif i != before_:
            check = True
            break
        else:
            check = False
        
        
    if not check:
        ans += 1
print(ans)
        