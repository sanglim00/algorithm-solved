def solution(num_list):
    ans1 = 1
    ans2 = 0
    
    for i in num_list: ans1 *= i
    ans2 = sum(num_list)**2
    
    
    return 1 if ans1<ans2 else 0