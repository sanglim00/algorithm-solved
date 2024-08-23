import sys

score = []
for _ in range(5):
    num = int(sys.stdin.readline())
    score.append(num if num >39 else 40)

print(sum(score) // 5)