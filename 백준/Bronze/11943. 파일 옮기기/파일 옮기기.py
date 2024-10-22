apple, orange = [], []

for _ in range(2):
    A, O = map(int, input().split())
    apple.append(A)
    orange.append(O)

print(min(apple[0]+orange[1], apple[1]+orange[0]))