score = list(map(int, input().split()))
score.sort()
print(abs((score[-1]+score[0])-(score[1]+score[2])))