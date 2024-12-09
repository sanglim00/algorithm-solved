import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p_list = list(input().rstrip())
    n = int(input())
    n_list = list(input().rstrip())
    lst = []
    
    now_str = ''
    for i in n_list:
        if i == '[' or i == ',' or i == ']':
            if len(now_str):
                lst.append(now_str)
            now_str = ''
        else:
            now_str += i

    now = True
    ans = ''
    start, end =  0, len(lst)
    for i in p_list:
        if i == 'R':
            now = not now
        elif i == 'D' and start>=end:
            ans = 'error'
            break
        elif i == 'D' and now:
            start+=1
        elif i == 'D' and not now:
            end-=1
    
    if ans == "error" or start > end: 
        print('error')
    elif start == end:
        print('[]')
    elif now:
        ans = '['
        for i in range(start, end):
            ans+=lst[i]
            ans+=','
        ans = ans[:-1]+']'
        print(ans)
    else:
        ans = '['
        for i in range(end-1, start-1, -1):
            ans+=lst[i]
            ans+=','
        ans = ans[:-1]+']'
        print(ans)