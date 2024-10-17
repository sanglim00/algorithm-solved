str_ = input().rstrip()

lst = list(str_.split('.'))
ans = ''
for i in range(len(lst)):
    if len(lst[i]) == 2:
        ans += 'BB'
    elif len(lst[i]) == 4:
        ans += 'AAAA'
    elif len(lst[i]) % 4 == 0:
        ans += 'AAAA'*(len(lst[i])//4)
    elif len(lst[i]) % 4 == 2:
        ans += 'AAAA'*(len(lst[i])//4)
        ans += 'BB'
    elif len(lst[i]) % 2:
        ans = '-1'
        break

    if i != len(lst)-1: ans += '.'

print(ans)