import sys

lst = []
for _ in range(5):
    num = int(sys.stdin.readline())
    lst.append(num)

print(sum(lst)//5)
print(sorted(lst)[2])