import sys

num = int(sys.stdin.readline())

lst = []

for i in range(num):
    _type = sys.stdin.readline().split()
    if _type[0] == 'push': lst.append(_type[1])
    elif _type[0] == "top": 
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    elif _type[0] =='size': print(len(lst))
    elif _type[0] == 'empty': 
        if len(lst) == 0: print(1)
        else: print(0)
    elif _type[0] == 'pop': 
        if len(lst) != 0:
            print(lst[-1])
            del lst[-1]
        else:
            print(-1)
    
    