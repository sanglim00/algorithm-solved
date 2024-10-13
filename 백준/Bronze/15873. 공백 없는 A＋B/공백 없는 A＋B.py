import sys

N = sys.stdin.readline().rstrip()
if len(N) == 4: print(20)
elif int(N)%10: print(int(N)%10 + int(N)//10)
else: print(int(N[0])+int(N[1:]))