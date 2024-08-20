import sys

str_ = sys.stdin.readline().rstrip()
lst = str_.split('_')

ans = ''
check = True

if str_[0].isupper(): check = False
for i in lst:
    if i == '': check = False

if len(lst) != 1:
    for i in lst[0]:
        if i.isupper():
            check = False
            break
        else: ans += i
    for i in range(1, len(lst)):
        if not check: break
        for j in lst[i]:
            if j.isupper(): 
                check =False
                break
        ans += lst[i][0].upper()
        ans += lst[i][1:]
else:
    for i in str_:
        if i.isupper():
            ans += '_'
            ans += i.lower()
        else:
            ans += i
print(ans if check else 'Error!')