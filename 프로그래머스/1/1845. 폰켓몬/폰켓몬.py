def solution(nums):
    num = len(nums)/2
    answer = len(set(nums))
    return answer if answer < num else num