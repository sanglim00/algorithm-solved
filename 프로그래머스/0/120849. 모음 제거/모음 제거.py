def solution(my_string):
    answer = ''
    lst = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in lst:
            answer+=i
    return answer