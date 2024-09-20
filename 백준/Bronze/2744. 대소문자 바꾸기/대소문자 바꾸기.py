import sys

str_ = sys.stdin.readline().rstrip()
for i in str_:
    if i.islower(): print(i.upper(), end='')
    else:print(i.lower(), end='')
print()