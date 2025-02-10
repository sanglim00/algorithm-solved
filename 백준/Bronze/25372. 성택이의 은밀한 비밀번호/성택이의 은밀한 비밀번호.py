N = int(input())
for _ in range(N):
    pw = input().rstrip()
    if 6<=len(pw)<=9: print('yes')
    else: print('no')