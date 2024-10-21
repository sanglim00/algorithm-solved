num = input().rstrip()

cnt0, cnt1 = 0, 0
now = num[0]
if num[0] == '1': cnt1 += 1
else: cnt0 += 1
for i in range(1, len(num)):
    if num[i] == '0' and num[i] != now:
        cnt0 += 1
        now = '0'
    elif num[i] == '1' and num[i] != now:
        cnt1 += 1
        now = '1'

print(min(cnt0, cnt1))