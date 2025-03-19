lst = list(map(int, input().split()))
lst.sort()

gap1 = lst[1]-lst[0]
gap2 = lst[2]-lst[1]

if gap1 == gap2: print(lst[2]+gap1)
elif gap1 < gap2: print(lst[1] + gap1)
else: print(lst[0]+gap2)