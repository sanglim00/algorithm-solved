def solution(numbers, direction):
    answer = []
    if direction == 'right':
        now = numbers.pop()
        numbers.insert(0, now)
    else:
        now = numbers.pop(0)
        numbers.append(now)
    return numbers