import sys

N = int(sys.stdin.readline())
myDict = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}
ans = []
for _ in range(N):
    str_ = sys.stdin.readline().rstrip()

    num = ''
    for i in str_:
        if i in myDict: num += i
        else:
            if num != '': 
                ans.append(num)
                num = ''
    if num != '': ans.append(num)

ans = list(map(int, ans))
ans.sort()
for i in ans: print(int(i))