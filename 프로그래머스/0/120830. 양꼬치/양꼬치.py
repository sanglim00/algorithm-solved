def solution(n, k):
    answer = 0
    num = n // 10
    k -= num
    answer = n * 12000 + k * 2000
    return answer