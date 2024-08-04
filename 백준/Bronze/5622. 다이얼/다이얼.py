import sys

str_ = sys.stdin.readline().rstrip()
myDict = {3: 'ABC', 4: 'DEF', 5: 'GHI', 6: 'JKL', 7: 'MNO', 8: 'PQRS', 9: 'TUV', 10: 'WXYZ'}

ans = 0
for i in str_:
    for k, v in myDict.items():
        if i in v:
            ans += k
print(ans)