import sys

_str = list(sys.stdin.readline().strip())
_burst = list(sys.stdin.readline().strip())

lst = []
_len = len(_burst)

for i in _str:
    lst.append(i)
    if lst[len(lst)-_len : len(lst)] == _burst:
        for j in range(_len):
            lst.pop()


print(''.join(lst) if len(''.join(lst)) != 0 else 'FRULA')
