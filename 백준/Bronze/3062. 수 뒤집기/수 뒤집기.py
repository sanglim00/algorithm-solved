N = int(input())
for _ in range(N):
    num = input().rstrip()
    sum_ = str(int(num) + int(num[::-1]))
    
    ans = 'YES'
    for i in range(len(sum_)//2):
        if sum_[i] != sum_[len(sum_)-1-i]:
            ans = 'NO'
            break
    print(ans)