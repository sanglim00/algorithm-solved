import sys

str_ = sys.stdin.readline().rstrip()
lst = str_.split('-')

if len(lst) == 1:
    ans = 0
    for i in str_.split('+'): ans += int(i)
    print(ans)
else:
    tmp = lst[0].split('+')
    ans = 0
    if len(tmp) == 1:
        ans = int(lst[0])
    else:
        ans = int(tmp[0])

    for i in range(1, len(tmp)): ans += int(tmp[i])
        
    for i in range(1, len(lst)):
        sum_ = 0
        for j in lst[i].split('+'): 
            sum_ += int(j)
        ans -= sum_
    print(ans)