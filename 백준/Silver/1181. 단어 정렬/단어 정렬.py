import sys

num = int(sys.stdin.readline())

lst = []
for i in range(num):
    string = sys.stdin.readline().strip()
    lst.append(string)

lst = list(set(lst))
lst.sort()
lst.sort(key=lambda x: len(x))
for i in lst: print(i)
