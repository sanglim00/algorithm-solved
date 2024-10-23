N = int(input())

for i in range(N):
    print(' '* (N-1-i)+"*"*(i+1)+'*'*i)

for i in range(N):
    print(' '* (i+1)+"*"*(N-1-i)+'*'*(N-2-i))