import sys

num = int(sys.stdin.readline())

for i in range(num):
    string = sys.stdin.readline()
    print(f"{string[0]}{string.strip()[-1]}")