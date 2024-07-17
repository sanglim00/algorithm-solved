import sys

N = int(sys.stdin.readline())
mydict = {}

for i in range(N):
    str_ = sys.stdin.readline()
    if str_ in mydict:
        mydict[str_] += 1
    else:
        mydict[str_] = 1

ans = [k for k, v in mydict.items() if max(mydict.values()) == v]
ans.sort()
print(ans[0])