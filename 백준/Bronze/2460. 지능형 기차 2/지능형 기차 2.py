max_ = 0
now = 0
for _ in range(10):
    out_, in_ = map(int, input().split())
    now -= out_
    now += in_
    max_ = max(max_, now)
print(max_)