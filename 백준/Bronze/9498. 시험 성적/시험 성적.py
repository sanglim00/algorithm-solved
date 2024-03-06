import sys

num = int(sys.stdin.readline())
if num > 89: print('A')
elif num > 79: print('B')
elif num > 69: print('C')
elif num > 59: print('D')
else: print('F')