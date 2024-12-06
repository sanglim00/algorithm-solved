lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    str_ = input().rstrip()
    if str_ == '#': break

    ans = 0
    for i in str_:
        if i in lst:
            ans += 1
    
    print(ans)
    