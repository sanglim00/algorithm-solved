import sys

myDict = {
    'c=': 'č',
    'c-': 'ć',
    'dz=': 'dž',
    'd-': 'đ',
    'lj': 'lj',
    'nj': 'nj',
    's=': 'š',
    'z=': 'ž'
}

s = sys.stdin.readline().strip()
ans = 0
for i in myDict:
    if i in s:
        while i in s:
            s = s.replace(i, ' ', 1)
            ans += 1
    
for i in s:
    if i != ' ':
        ans += 1

print(ans)