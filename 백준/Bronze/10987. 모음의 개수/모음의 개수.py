str_ = input().rstrip()

mySet = {'a', 'e', 'i', 'o', 'u'}
ans = 0
for i in str_:
    if i in mySet: ans += 1

print(ans)