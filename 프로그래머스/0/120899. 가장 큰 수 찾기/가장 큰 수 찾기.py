def solution(array):
    answer = []
    max_, idx = 0, 0
    for i in range(len(array)):
        if max_ < array[i]:
            max_ = array[i]
            idx = i
    answer.append(max_)
    answer.append(idx)
    return answer