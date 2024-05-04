def solution(numbers):
    numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    answer = 0
    
    numbers = sorted(numbers)
    
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    
    return answer