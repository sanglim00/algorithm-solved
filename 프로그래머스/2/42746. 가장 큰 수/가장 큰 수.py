def solution(numbers):

    if sum(numbers) == 0:
        return str(0)
    numbers= list(map(str, numbers))
    numbers.sort(key=lambda x : str(x * 3), reverse=True)
    
    answer = ''.join(numbers)
    
    return answer