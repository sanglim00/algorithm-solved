def solution(number, k):
    lst = []
    
    for i in number:
        while k > 0 and lst and lst[-1] < i:
            lst.pop()
            k -= 1
        lst.append(i)
    
    answer = ''.join(lst[:len(lst) - k])
    return answer