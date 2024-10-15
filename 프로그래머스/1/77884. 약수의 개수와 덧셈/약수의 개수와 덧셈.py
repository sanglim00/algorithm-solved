def check_num(num):
    ans = 0
    for i in range(1, num+1):
        if num % i == 0:
            ans += 1
    
    return ans
    
    
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        answer += -i if check_num(i) % 2 else i
        
    return answer