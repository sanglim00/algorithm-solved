def solution(s):
    s = s.split(' ')
    min_, max_ = float("INF"), -float("INF")
    for i in s:
        max_ = max(max_, int(i))
        min_ = min(min_, int(i))
    return f"{min_} {max_}"