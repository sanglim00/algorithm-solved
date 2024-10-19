from itertools import combinations
def solution(nums):
    answer = 0

    for i in combinations(nums, 3):
        sum_ = sum(i)
        now = True
        for j in range(2, sum_):
            if sum_ % j == 0:
                now = False
                break
        if now: answer += 1

    return answer