while True:
    num = int(input())
    if num == 0: break
    ans = 0
    for i in range(1, num+1):
        ans += i
    print(ans)