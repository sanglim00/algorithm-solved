import sys

num = int(sys.stdin.readline())

for i in range(1, num+1):
    print(f"{' '*(num-i)}{'*'*i}")