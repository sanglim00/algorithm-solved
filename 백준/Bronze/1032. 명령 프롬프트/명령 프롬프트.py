import sys

N = int(sys.stdin.readline())
str1 = sys.stdin.readline().rstrip()

for _ in range(N-1):
    str2 = sys.stdin.readline().rstrip()
    for i in range(len(str2)):
        if str1[i] != str2[i]: 
            str1 = str1[:i] + "?" +str1[i+1:]

print(str1)