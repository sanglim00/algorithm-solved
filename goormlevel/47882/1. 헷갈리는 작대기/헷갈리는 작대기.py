import sys

str_ = list(sys.stdin.readline())
ans, ans2, ans3, ans4 = 0, 0, 0, 0

for i in str_:
	if i == '1': ans += 1
	elif i == 'I': ans2 += 1
	elif i == 'l': ans3 += 1
	elif i == '|': ans4 += 1
	else: continue

print(ans)
print(ans2)
print(ans3)
print(ans4)
