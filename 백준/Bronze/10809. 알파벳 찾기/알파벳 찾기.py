import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'
str_ = sys.stdin.readline()

myDict = {}
for i in range(len(str_)):
    if str_[i] not in myDict:
        myDict[str_[i]] = i

for i in alpha:
    if i in myDict:
        print(myDict[i], end=' ')
    else:
        print(-1, end=' ')
print()