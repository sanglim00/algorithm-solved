import sys

str_ = sys.stdin.readline().rstrip()

myDict = {}
for i in str_.upper():
    if i in myDict:
        myDict[i] += 1
    else:
        myDict[i] = 1

cnt = [k for k, v in myDict.items() if max(myDict.values()) == v]
print(cnt[0] if len(cnt) == 1 else '?')
