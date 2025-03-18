alpha = list(map(int, input().split()))
alpha.sort()
A = alpha[0]
B = alpha[1]
C = alpha[2]

str_ = input().rstrip()
for i in str_:
    if i == 'A': print(A, end=" ")
    elif i == 'B': print(B, end=" ")
    else: print(C, end=" ")