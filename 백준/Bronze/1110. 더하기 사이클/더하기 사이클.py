import sys

num = sys.stdin.readline().strip()
after = 0
check = 0

if len(str(num)) == 1: term = "0" + num
else: term = num

while num != after:
    tmp = str(sum(list(map(int, str(int(term))))))
    tmp2 = list(term)[-1]
    after = str(int(tmp2 + str(int(tmp)%10)))
    term = tmp2 + str(int(tmp)%10)
    check += 1
    
print(check)