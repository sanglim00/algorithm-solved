import sys

num = list(sys.stdin.readline().strip())

for i in range(len(num)):
    for j in range(len(num)):
        if int(num[i]) > int(num[j]):
            num[i], num[j] = num[j], num[i]

print("".join(num)) 
